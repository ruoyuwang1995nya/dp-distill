import dpdata
import json
import numpy as np
import glob
import os
from pathlib import Path
from typing import (
    List,
    Union,
)

from dflow.python import OP, OPIO, Artifact, BigParameter, OPIOSign, Parameter


class Inference(OP):
    r"""Collect data for direct inference"""

    @classmethod
    def get_input_sign(cls):
        return OPIOSign(
            {
                "systems": Artifact(List[Path]),
                "model": Artifact(Path),
                "type_map": Parameter(List),
                "inference_config": BigParameter(dict),
            }
        )

    @classmethod
    def get_output_sign(cls):
        return OPIOSign(
            {
                "labeled_systems": Artifact(List[Path]),
                "dp_test": Artifact(List[Path]),  # BigParameter(List[dict]),
                "root_labeled_systems": Artifact(Path),
                "report": Artifact(Path),
            }
        )

    @OP.exec_sign_check
    def execute(
        self,
        ip: OPIO,
    ) -> OPIO:
        r"""Execute the OP.

        Parameters
        ----------
        ip : dict
            Input dict with components:

        Returns
        -------
        op : dict
            Output dict with components:
            - `dp_test`: result for dp_test
            - `task_names`: (`List[str]`) The name of tasks. Will be used as the identities of the tasks. The names of different tasks are different.
            - `task_paths`: (`Artifact(List[Path])`) The parepared working paths of the tasks. Contains all input files needed to start the LAMMPS simulation. The order fo the Paths should be consistent with `op["task_names"]`
        """
        # List of system pathes
        systems = ip["systems"]
        model_path = ip["model"]
        type_map = ip["type_map"]
        config = ip["inference_config"]
        if len(type_map) > 0:
            config["type_map"] = type_map

        task = config.pop("task", "inference")
        res = {}
        for sys in systems:
            res[sys.name] = {
                task: eval_model.tasks(task, model_path, sys, name=sys.name, **config)
            }
        # details of dp_test
        dp_test_detail = []
        report = {}
        for sys, v in res.items():
            report[sys] = v.get("dp_test", {})
            report[sys].pop("sys_name", None)
            detail_fls = [
                Path(file) for file in glob.glob(f"{sys}.*") if os.path.isfile(file)
            ]
            dp_test_detail.extend(detail_fls)
        with open("report.json", "w") as fp:
            json.dump(report, fp, indent=4)

        labeled_system_key = task if task != "dp_test" else "inference"
        return OPIO(
            {
                "labeled_systems": [v.get(labeled_system_key) for k, v in res.items()],
                "dp_test": dp_test_detail,
                "root_labeled_systems": Path(config.get("prefix", "systems")),
                "report": Path("report.json"),
            }
        )


class eval_model:
    def __init__(
        self,
        model=None,
        data=None,
        labeled_data=None,
        **kwargs,
    ):
        self._model = None
        self._data = None
        self._labeled_data = None
        if model:
            self.load_model(model)
        if data:
            self.read_data(data, **kwargs)
        if labeled_data:
            self.read_labeled_data(labeled_data, **kwargs)

    @property
    def model(self):
        return self._model

    @property
    def data(self):
        return self._data

    @property
    def labeled_data(self):
        return self._labeled_data

    def load_model(self, model: Path):
        self.model_path = model
        from deepmd.infer import DeepPot

        print("Loading model")
        self._model = DeepPot(model)
        print("Model loaded")

    def read_data(self, data, fmt="deepmd/npy", **kwargs):
        self._data = dpdata.System(data, fmt=fmt, **kwargs)

    def read_labeled_data(self, labeled_data, fmt="deepmd/npy", **kwargs):
        self._labeled_data = dpdata.LabeledSystem(labeled_data, fmt=fmt, **kwargs)
        self._data = self._labeled_data

    def evaluate(self, dp_test: bool = False, name: str = "default", **kwargs):
        if self.model:
            if dp_test is True and isinstance(self._labeled_data, dpdata.LabeledSystem):
                res = {}
                new_labeled_data = self._labeled_data.predict(self.model_path, **kwargs)
                atom_num = self._labeled_data.get_natoms()
                res["atom_numb"] = atom_num
                # get energy error
                new_labeled_e = new_labeled_data.data["energies"].flatten()
                orig_labeled_e = self._labeled_data.data["energies"].flatten()
                np.savetxt(
                    "%s.energy.txt" % name,
                    np.column_stack((orig_labeled_e, new_labeled_e)),
                    fmt="%.6f",
                )
                np.savetxt(
                    "%s.energy_per_atom.txt" % name,
                    np.column_stack(
                        (orig_labeled_e / atom_num, new_labeled_e / atom_num)
                    ),
                    fmt="%.6f",
                )
                res["MAE_energy"] = get_mae(new_labeled_e, orig_labeled_e)
                res["RMSE_energy"] = get_rmse(new_labeled_e, orig_labeled_e)
                res["MAE_energy_per_at"] = (
                    get_mae(new_labeled_e, orig_labeled_e) / atom_num
                )
                res["RMSE_energy_per_at"] = (
                    get_rmse(new_labeled_e, orig_labeled_e) / atom_num
                )

                # get force error
                new_labeled_f = new_labeled_data.data["forces"].flatten()
                orig_labeled_f = self._labeled_data.data["forces"].flatten()
                np.savetxt(
                    "%s.force.txt" % name,
                    np.column_stack((orig_labeled_f, new_labeled_f)),
                    fmt="%.6f",
                )
                res["MAE_force"] = get_mae(new_labeled_f, orig_labeled_f)
                res["RMSE_force"] = get_rmse(new_labeled_f, orig_labeled_f)

                # get virial error
                if self._labeled_data.has_virial():
                    new_labeled_v = new_labeled_data.data["virials"].flatten()
                    orig_labeled_v = self._labeled_data.data["virials"].flatten()
                    np.savetxt(
                        "%s.virial_error.txt" % name,
                        np.column_stack((orig_labeled_f, new_labeled_f)),
                        fmt="%.6f",
                    )
                    res["MAE_virial"] = get_mae(new_labeled_v, orig_labeled_v)
                    res["RMSE_virial"] = get_rmse(new_labeled_v, orig_labeled_v)
                print(res)
                return res

            elif self.data:
                print("Labeling datas...")
                self._labeled_data = self.data.predict(self.model_path, **kwargs)
        else:
            print("No model loaded!")

    def data_filter(self, max_force=None):
        if self.labeled_data:
            pass
        else:
            print("No labeled data")
            return

        cells = self.labeled_data.data["cells"]
        coords = self.labeled_data.data["coords"]
        energies = self.labeled_data.data["energies"]
        forces = self.labeled_data.data["forces"]
        virials = self.labeled_data.data["virials"]
        data_dict = self.labeled_data.data
        n_atom = sum(data_dict["atom_numbs"])
        n_frame = cells.shape[0]
        clean_ls = [i for i in range(n_frame)]
        print("Before cleaning, there are %d frames." % len(clean_ls))
        if max_force:
            for frame in range(n_frame):
                # print("Max force is %s"%abs(forces[frame]).max())
                if abs(forces[frame]).max() > max_force:
                    clean_ls.remove(frame)
        print("After cleaning, %d frames left." % len(clean_ls))
        print("max energy", energies[clean_ls].max() / n_atom)
        print("min energy", energies[clean_ls].min() / n_atom)
        data_dict["cells"] = cells[clean_ls]
        data_dict["coords"] = coords[clean_ls]
        data_dict["energies"] = energies[clean_ls]
        data_dict["forces"] = forces[clean_ls]
        data_dict["virials"] = virials[clean_ls]

        return dpdata.LabeledSystem(data=data_dict)

    @classmethod
    def tasks(
        cls, task: str, model: Union[Path, str], system: Union[Path, str], **config
    ):
        # label_config= config.pop("label_config",{})
        if task == "inference":
            model_data_obj = cls(
                model=model, data=system, type_map=config.get("type_map")
            )
            model_data_obj.evaluate()
            sys_prefix = config.get("prefix", "systems")
            out_path = Path(sys_prefix) / system.name
            out_path.mkdir(parents=True, exist_ok=True)
            if max_force := config.get("max_force"):
                model_data_obj.data_filter(max_force=max_force).to(
                    "deepmd/npy", out_path
                )
            else:
                model_data_obj.labeled_data.to("deepmd/npy", out_path)
            return out_path

        elif task == "dp_test":
            model_data_obj = cls(
                model=model, labeled_data=system, type_map=config.get("type_map")
            )
            test_res = model_data_obj.evaluate(dp_test=True, name=system.name)
            test_res.update({"sys_name": system.name})
            return test_res
        elif task == "filter":
            model_data_obj = cls(labeled_data=system)
            sys_prefix = config.get("prefix", "systems")
            out_path = Path(sys_prefix) / system.name
            out_path.mkdir(parents=True, exist_ok=True)
            max_force = config.get("max_force", 10)
            model_data_obj.data_filter(max_force=max_force).to("deepmd/npy", out_path)
            return out_path


def get_mae(test_arr, orig_arr):
    num_data = len(test_arr)
    if num_data != len(orig_arr):
        raise RuntimeError("Two arrays must be of the same size")
    return abs(test_arr - orig_arr).sum() / num_data


def get_rmse(test_arr, orig_arr):
    num_data = len(test_arr)
    if num_data != len(orig_arr):
        raise RuntimeError("Two arrays must be of the same size")
    return (np.sum(abs(test_arr - orig_arr) ** 2) / num_data) ** 0.5
