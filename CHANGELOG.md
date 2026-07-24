# CHANGELOG

<!-- version list -->

## v0.2.7 (2026-07-24)

### Bug Fixes

- Remove total translational momentum when initializing MD velocities to prevent unphysical
  translations.
  ([`2ca09f8`](https://github.com/qchempku2017/pfd-kit/commit/2ca09f8180e3a710369e6a48930f08032e193593))


## v0.2.6 (2026-07-16)

### Bug Fixes

- Update input name init_model in download settings to fix downloading issue and enhance download
  command helper text.
  ([`7814f41`](https://github.com/qchempku2017/pfd-kit/commit/7814f410f4314a8ba0ba10b7be37198998f1cdf4))

- Version in __init__.py
  ([`ea2507f`](https://github.com/qchempku2017/pfd-kit/commit/ea2507fc07d4cfcbd2a27d47267c88a3fc575ffe))


## v0.10.13 (2026-07-15)

### Bug Fixes

- Version in __init__.py
  ([`ea2507f`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/ea2507fc07d4cfcbd2a27d47267c88a3fc575ffe))


## v0.10.12 (2026-07-15)

### Bug Fixes

- Update input name init_model in download settings to fix downloading issue and enhance download
  command helper text.
  ([`7814f41`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/7814f410f4314a8ba0ba10b7be37198998f1cdf4))


## v0.2.5 (2026-02-17)

### Bug Fixes

- Add support for pytest
  ([`6d4a166`](https://github.com/qchempku2017/pfd-kit/commit/6d4a166aee6a62ea0a24dea9f238187b08103059))

- Relax perturbation test thresholds and ensure bond lengths within ±10%
  ([`1a7a97e`](https://github.com/qchempku2017/pfd-kit/commit/1a7a97e36bcdd98804f28a8a45f746df740cb4dd))


## v0.10.11 (2026-02-11)

### Bug Fixes

- Add support for pytest
  ([`6d4a166`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/6d4a166aee6a62ea0a24dea9f238187b08103059))

- Relax perturbation test thresholds and ensure bond lengths within ±10%
  ([`1a7a97e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/1a7a97e36bcdd98804f28a8a45f746df740cb4dd))


## v0.10.10 (2026-01-25)

### Bug Fixes

- Issues with NoneType in select_confs.py
  ([`051de33`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/051de33f4c119561b24ee69af0400d64b993354d))

- Issues with wrong pressure writeout
  ([`5bb9e9b`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/5bb9e9b7ef689af97b4cf613ebfc517e4ba88f44))


## v0.10.9 (2026-01-07)

### Bug Fixes

- Issues with entropy filtering with gpu
  ([`a6cb151`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/a6cb151f48ce1532308b00a25cb8b62420f3144b))


## v0.10.8 (2026-01-05)

### Bug Fixes

- Issues with pressure unit
  ([`d3f7fbd`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/d3f7fbdb8df07ac4b8b54975107171c5cafa0388))

- Update resubmit args
  ([`0565655`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/0565655dceede963bd5764b502a61c6227029ce5))


## v0.10.7 (2025-12-24)

### Bug Fixes

- Update calypso docs
  ([`1f16018`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/1f16018a12a90a348d5420524d5c1791488a66e5))


## v0.10.6 (2025-12-03)

### Bug Fixes

- Using default vasp KSPACING
  ([`9a87127`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/9a87127871e4ed405b91f2424cab087679aa24c7))


## v0.10.5 (2025-10-23)

### Bug Fixes

- Handle None paths in collect.py
  ([`8a64953`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/8a649535a6efaf7133c7f32ef3690a76b89fe381))


## v0.10.4 (2025-10-22)

### Bug Fixes

- Issues with sorted atoms
  ([`0859542`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/0859542fe318dcb8eff470709bd2c1e130b46ee3))


## v0.10.3 (2025-10-09)

### Bug Fixes

- Issues with ase inference
  ([`16d1894`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/16d18946c51de889fb1e9261c37f7718ee2a9496))


## v0.10.2 (2025-09-25)

### Bug Fixes

- Issues with ase task group number
  ([`811c770`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/811c77059e8976ae031b7dfe8e212ce434f02882))


## v0.10.1 (2025-09-20)

### Bug Fixes

- Issues with scheduler OP
  ([`c8541e7`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/c8541e7f8bb5c4743ba6f8cd20a9e9e08bb30658))


## v0.10.0 (2025-09-19)

### Bug Fixes

- Support multiple directories for select confs
  ([`6168d73`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/6168d7350a380cf94ee54a76b8eb3a6ef150524b))

### Features

- Add calypso support
  ([`1d1a625`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/1d1a625e720e2675cb1be7955d79721eb45a97b3))


## v0.9.3 (2025-09-16)

### Bug Fixes

- Add support for atomic magmom in VASP
  ([`c65f0d3`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/c65f0d32127ec07eb22214a26419d54b7feb015d))

- Add tests for ase md components
  ([`42cbbd7`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/42cbbd73728acfa6357c163d03eddc50ea81dfcf))

- Add vasp support
  ([`c65f0d3`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/c65f0d32127ec07eb22214a26419d54b7feb015d))

- Redundant import
  ([`fafb172`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/fafb172c289bbf507f37fb3e7ca96630f38b485b))

- Update changelog
  ([`b0ceef7`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/b0ceef7f38db7dc3ea02c8b7b013023dc8abd070))

- Update docs
  ([`c65f0d3`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/c65f0d32127ec07eb22214a26419d54b7feb015d))

- Update docs for new version
  ([`003d002`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/003d0025f7736af710f52df2cc14d9400aee5969))

- Update examples
  ([`33f17c9`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/33f17c91c45d51374fe643a2d08bcba21c9207e2))

- Update README and dependencies
  ([`f6f2223`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/f6f2223546bf6b4045ac2f8c1f999bc60affa059))

- Update readthedocs config
  ([`0c9c20e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/0c9c20e12705b86cdc7705506da1eb3b1b5f3559))

- Update release setting
  ([`cb0da95`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/cb0da950716b1feeff09aebf1b7b5d6d2a95f67c))


## Unreleased

### Bug Fixes

- Update changlog setting
  ([`51a3a1e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/51a3a1e593311da7dbb634f68a6abc78e43c16cc))

- Update docs for new version
  ([`003d002`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/003d0025f7736af710f52df2cc14d9400aee5969))

- Update examples
  ([`33f17c9`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/33f17c91c45d51374fe643a2d08bcba21c9207e2))

- Update readthedocs config
  ([`0c9c20e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/0c9c20e12705b86cdc7705506da1eb3b1b5f3559))

- Update release setting
  ([`cb0da95`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/cb0da950716b1feeff09aebf1b7b5d6d2a95f67c))


## v0.9.2 (2025-09-12)

### Bug Fixes

- Issues with select_confs
  ([`ca324ab`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/ca324ab22f16d5ea13d63238e4afe90159c57b7f))


## v0.6.1 (2025-04-07)

### Bug Fixes

- Issues with None sys_path
  ([`bbf8ca6`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/bbf8ca63225131d8bdd1705721f155daf5f920fa))


## v0.6.0 (2025-02-27)

### Bug Fixes

- Miscellaneous
  ([`124b2c4`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/124b2c414f8c411c1026bc60bd082a3aad81309f))

### Features

- Add calypso support
  ([`3d281f6`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/3d281f62f8b62f03630f520cfbe9d7fa1b561ec9))


## v0.5.3 (2024-12-28)

### Bug Fixes

- Enable fp in dist
  ([`3270c9c`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/3270c9c531f1f258754d0161116aa8f1580f1ff4))


## v0.5.2 (2024-12-28)

### Bug Fixes

- Add fe3o4 example
  ([`769176d`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/769176d6f81f3d048c114b1ff3bd8aea8128f470))

- Issues with conf arg
  ([`55b9677`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/55b9677a1dc230614c7bcca6e5f56b98cbcc0406))


## v0.5.1 (2024-11-29)

### Bug Fixes

- Correct rmse calculator
  ([`ccb3b9f`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/ccb3b9f1ba1894d11d5d47b4b980c71acc481ea1))


## v0.5.0 (2024-11-28)

### Features

- Add replicate to pert gen
  ([`3319e43`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/3319e43e815ad15e291c1061ea8a18922cc79489))


## v0.4.3 (2024-11-28)

### Bug Fixes

- Improve conv report for dist
  ([`bc80a4d`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/bc80a4dbc9e1fabb25b32d4588a5e2ec909d3f5d))


## v0.4.2 (2024-11-27)

### Bug Fixes

- Bnbzto example update to adapt the official version of deepmd-kit 3.0
  ([`b124663`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/b124663094ca734d116f6a99a98e10708bbb01c5))

- Fatalerror if no conf is added while unconv
  ([`e3ba0c0`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/e3ba0c03ac52d2f79e4432b78f0addaf137e3ff4))

- Optimized step names and keys
  ([`f6c8ff4`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/f6c8ff476107673bd323297622b302d3f7dc7064))

- Update download module
  ([`c1e5419`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/c1e54191deec9e1a302812f706ce21a04980fb1e))

- Update examples
  ([`dd3b5f1`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/dd3b5f1429644ef57c758f0aa1b13520ca4fed90))


## v0.4.1 (2024-11-26)

### Bug Fixes

- Update examples
  ([`370e318`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/370e318a49aa159e7c6b77e8ae87014b4351d181))


## v0.4.0 (2024-11-23)

### Bug Fixes

- Bugs with energy filter
  ([`d64dfb7`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/d64dfb7d5f1c29768d6e27dfa2068d85a4ff2c73))

- Miscellaneous
  ([`a2885fb`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/a2885fb9affa99890e6f6c5c6c6d6ab01acaf346))

### Features

- Add recursive finetune
  ([`245487d`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/245487daff2f49f1ecc8032574f7f170121c673d))


## v0.3.5 (2024-11-21)

### Bug Fixes

- Reformatting README
  ([`038a01f`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/038a01f187f6d478a625fb68759a00b5d8dceb6f))


## v0.3.4 (2024-11-21)

### Bug Fixes

- Miscelaneous
  ([`2ddffe4`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/2ddffe4813da26e9421eecbb2ac4e3526a8fd5b7))


## v0.3.3 (2024-11-20)

### Bug Fixes

- Add quick start example
  ([`eb97887`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/eb9788768ed64c04dc43002765d32a85e866d047))

- Issue with dist workflow
  ([`520090e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/520090ea3ea538b651578bbb3b0f15b22ee9581d))

fix: update docs

- Modify doc hompage, make the scientific purpose more clearly.
  ([`2fe80f1`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/2fe80f194a56eb592fd5d634ba883cacafbe5253))


## v0.3.2 (2024-11-16)

### Bug Fixes

- Add status supervisor
  ([`ac799ba`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/ac799ba1e1a81b53f22a06c3d101cabf0e94754c))

- Remove POTCAR
  ([`5ce3541`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/5ce3541da21872159ab4e397a0bf025b25f5d1fa))


## v0.3.1 (2024-11-15)

### Bug Fixes

- Add api docs
  ([`ec8bb74`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/ec8bb74b4c1853065dbe2719f22bf7a402177b61))

- Issues with multi-head fine-tune
  ([`cd10fa3`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/cd10fa30f824f18b0e583e84408df88ae7ae4e3c))


## v0.3.0 (2024-11-14)

### Bug Fixes

- Update docs
  ([`dc6b76b`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/dc6b76b29375dbcd3852fa705366076973daa773))

### Features

- Reformulating loop structures
  ([`fd3622c`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/fd3622cae85d69b93a13e3f4e25f5c05bda21961))


## v0.2.0 (2024-11-11)

### Bug Fixes

- Bugs with download
  ([`55e3b83`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/55e3b8380c32776b55b1e2d8fa9b52b2bde986d6))

- Update BNBZTO English doc
  ([`f1c3796`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/f1c37962e0f963d0c38e8bd481d6ca492b9a3960))

- Update pylint setting
  ([`e719ab4`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/e719ab4d977966ffd882f8c779a683fd258c2972))

fix: modify the pylint setting

### Features

- Add data_gen workflow
  ([`d444cc5`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/d444cc54739926b49a7b3e93a41872e6bcd587f7))


## v0.1.4 (2024-11-09)

### Bug Fixes

- Modify examples
  ([`6549e9e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/6549e9e52ae0ec5fc30625959664013df922e29a))


## v0.1.3 (2024-11-09)

### Bug Fixes

- Update examples
  ([`e403a41`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/e403a417317ec74e202315da18de62d09f8eaa73))


## v0.1.2 (2024-11-09)

### Bug Fixes

- Add new example folder
  ([`4e2eb4c`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/4e2eb4cf9fd896a900feda3ec12508eec09da34b))

- Bugs with logging
  ([`59e4972`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/59e49727fbae8ebe4491231fc7ee7efbc7c2cab6))

- Unit test of pert_gen
  ([`526b0e9`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/526b0e9ddd39c08323c95cfd40e1c7fdd1cc46a6))

- Update an advanced finetune demo —— BNBZTO
  ([`2afc4c2`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/2afc4c253a5d16d06135f69bedbb45f282546134))

- Update docs
  ([`a063110`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/a063110dd24868033a0195f43fa0b56fd7d29e1b))

- Update docs
  ([`6f6cae2`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/6f6cae2a912f56ade60e116d437203623cdc71de))

- Update input script
  ([`5ccaf95`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/5ccaf952329c066a42fe87863c98a7c683db5bfc))


## v0.1.1 (2024-11-08)

### Bug Fixes

- Add argument list for input script
  ([`0431790`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/0431790afe0d6d8e6369b2f2cc121f0816b6407b))

- Micelaneous
  ([`bb05c85`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/bb05c859bc6623e9821fd110bfcc78ef59e43388))

- Minor bugs
  ([`7e23548`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/7e235483ad0f9fb8cfbabc0d51862201f2989937))


## v0.1.0 (2024-10-31)

### Bug Fixes

- Update examples
  ([`9e2bf7e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/9e2bf7e87c3b108c7cd7b13fc239584d98649a90))

- Update I/O of steps
  ([`47da0d8`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/47da0d80e2f8eecbf6d0ac31a5c0da67de6116d3))

- Update input script doc
  ([`50196e9`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/50196e977f768e7204ba6761af903f61be3046de))

- Update package info
  ([`929a2fd`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/929a2fd02ab90b107d8c9277e59e2288b0ceb2d8))

- Update script doc
  ([`c51cb80`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/c51cb808034f6865d706c089c749c36a8058be14))

### Features

- Add conf filter in the check converge step
  ([`bddd99f`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/bddd99f590cf7b99bfebb16b26b6d123ff9deab7))


## v0.0.14 (2024-10-27)

### Bug Fixes

- Add download end results
  ([`8d0c502`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/8d0c502d6be6b342d45859fc2714a5f2c629f188))

- Update cli docs
  ([`d7881e5`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/d7881e5f8fe9555f0620941045b95975e7e2c46f))

- Update readme
  ([`050de0e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/050de0e249d8e4c312c97c402dd3af02a9137e13))


## v0.0.13 (2024-10-26)

### Bug Fixes

- Modified release rule
  ([`14fbdd0`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/14fbdd07fda36511ad20ddf8f637ebe92705c45c))

- Modify release rule
  ([`9d1cb28`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/9d1cb282e34e5030201f312888ad4593f98c94f9))

- Modify rule for release workflow
  ([`4d3644e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/4d3644e0275d0c99651f691e67b5810ac247bc58))

- Modify rules
  ([`bde47c6`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/bde47c6df92033bf3b6c25bda64ecdb1b64c3b52))

- Update ci-test rule
  ([`53bef9a`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/53bef9aa9d87804768ccc65b01595854f0c7ee90))


## v0.0.12 (2024-10-26)

### Bug Fixes

- Add doc build to release workflow
  ([`0a33c42`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/0a33c426ca37e369854903261ef2fd732d9cda61))

- Set up doc pages
  ([`80682f9`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/80682f9a208895201dc0a0134518b33477863d76))

- Update build dependency
  ([`3d5c2cc`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/3d5c2cc56e2b892e4e38aba85a5091f57eabe31b))

- Update doc
  ([`38e61fb`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/38e61fb0dce1b4f75aedd30dd5230837fd99aaba))

- Update docs
  ([`75fab5d`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/75fab5d31daaa7d9909112d7b3820ebd5c15fc0f))

- Update docs
  ([`14d99fd`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/14d99fda5c7dab4478399fcddc37f0b21b3a2b14))

- Update docs
  ([`d0ff959`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/d0ff95951b6e4081cdb35366d4d41e8c4e27479c))

- Update docs
  ([`f94cc82`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/f94cc828130f9ba43f76f1bd6762175062e0433d))

- Update docs
  ([`4cb7605`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/4cb76058db64e4b82cf7160f36b7c0a2bd3b8198))

- Update docs
  ([`a886db4`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/a886db4652971ef3af189a3d5b0d40d850f2f079))


## v0.0.11 (2024-10-25)

### Bug Fixes

- Add filter test
  ([`5afb27e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/5afb27e561d31a1bcf967dc0433521522af7b7fe))

- Miscellaneous updates
  ([`3f8ae06`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/3f8ae06d4c4bdd3e9add4df11e9d64aa0ebfea74))

- Optimize the distance filter
  ([`4301e92`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/4301e922eb3330eba2615b46d2a3883643e2a4f6))


## v0.0.10 (2024-10-22)

### Bug Fixes

- Bug with distillation workflow
  ([`f28acfc`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/f28acfc26391ddf2dde91e33074a5a5353a64a89))

- Logging for convergence mudolue
  ([`e523b17`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/e523b17e07dfbf3ea85f7a355c5eaaa0a924389f))


## v0.0.9 (2024-10-20)

### Bug Fixes

- Add logging support
  ([`15b9747`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/15b97471d29e2e3af4ccb7d6cdcf737c7eefee69))

- Add logging support
  ([`d845181`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/d845181472ec90e8abd1f3a4d009d9e2738ae6e2))


## v0.0.8 (2024-10-17)

### Bug Fixes

- Add ticket support
  ([`7cce152`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/7cce1522906cdee10f81b4503b8f5b0083b240fa))

- Key error in dist
  ([`1b789ec`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/1b789ecf21a25288378674c9e0d67f218b90f001))


## v0.0.7 (2024-10-14)

### Bug Fixes

- Bug with cli
  ([`f42707f`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/f42707ff80d5d4dfe5e3858971cc1fc3251c97ac))

- Issues with workflow test
  ([`2e3d921`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/2e3d9213dfca07733085a4e2338aa2ffd4cab347))

- Optimize the resubmit functions
  ([`2c68faf`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/2c68fafd0d3546996570b77733428214b1f5984d))

- Restructuring flow generation
  ([`18cec13`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/18cec13495be7989c9b11a94dc7bd62ac09abc89))


## v0.0.6 (2024-10-12)

### Bug Fixes

- Enable download of validation-test
  ([`435f3e0`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/435f3e08230c5fe6c05e85e475acc15aeb7028c7))

- Get task type from config
  ([`440ba3d`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/440ba3dd3ad57fd235d3271023c009284e57607d))

- Minor issue with model test
  ([`785ec9b`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/785ec9b5fcc6df280a8ec4f400941d00e8182255))

- Rewrite model test OP
  ([`286eed3`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/286eed30c495486811ee84b61087882aa5c21517))


## v0.0.5 (2024-10-10)

### Bug Fixes

- Bugs with gen_task_lmp
  ([`7137573`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/7137573b5439092c6bfd426b4adfd22c30916ab2))

- Update dependency
  ([`ae42886`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/ae42886b98f0cc22c2cd60ae07505e475ebffc2f))

- Update node config
  ([`749473b`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/749473b5fa6668f9b65c64e04a485053353ed329))


## v0.0.4 (2024-10-08)

### Bug Fixes

- Bug with PertGen
  ([`7f21ab8`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/7f21ab8e5e174a1a51d1202fe89463f3a985bc29))


## v0.0.3 (2024-10-08)

### Bug Fixes

- Add support for other models
  ([`a39c78a`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/a39c78a48d2aff6ae852f49cf999cd502dec5e50))

- Deprecate the gen_task op
  ([`24c26b4`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/24c26b44b0dccdbcf69b9752fb25f8ce31a2d4bb))

- Improve code
  ([`4e12b45`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/4e12b45600f1ac8bb02db6ad92e152d749ad690f))

- Init conf prefix
  ([`f97f6b4`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/f97f6b470e9ff48e351b85538b1e7cfd7efcd26c))

- Reformulate input script and add darg
  ([`a82e336`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/a82e3364f87130f65099d0b1d3436b1c9d9e6934))

- Update ft example
  ([`a7f7a88`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/a7f7a88573fec7cf56a330afbf1de31a00865d8f))

- Update pre-commit
  ([`43372f5`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/43372f53962b40eaaf6bf31e72d192a58c0ccd22))


## v0.0.2 (2024-09-29)

### Bug Fixes

- Restore cli
  ([`71f8df8`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/71f8df88685bf3cc140fe4c2bcb13ba898eb8e0e))


## v0.0.1 (2024-09-29)


## v0.0.0 (2024-09-29)

### Bug Fixes

- Add ase to setup file
  ([`730da07`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/730da079179067a7a5c8d5742696a9fed44df2c0))

- Add ci test module
  ([`6fde807`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/6fde807818dbf772755346ab2406bb0ac81dc820))

- Add cli entrypoint
  ([`98c39db`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/98c39db14c1bba72f5aad5510a6902d5cc0e49cd))

- Add conf filter
  ([`1e2e52e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/1e2e52e23602860f17f39f4593ed1e137e7588fd))

- Add dist loop
  ([`36e6411`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/36e64111c3b82aec5348ff64622f89a1090bdc1d))

- Add example file for iterative finetune
  ([`c50f7c6`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/c50f7c6877f50dcf39683a200c71e16775356e0a))

- Add examples and update docs
  ([`ebc4c3c`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/ebc4c3c6a9b3292b136efa849cb47a08bfe38777))

- Add filter to ft workflow
  ([`4927f87`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/4927f8778aed87ecac16d4deefc5f92b930cfe22))

- Add fine-tune module
  ([`d4fc7ba`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/d4fc7bada70b438a79fd60a148283dcbf1306116))

- Add INCAR to ft example
  ([`708396c`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/708396c4ae3de54bf8e749bec74de2121942a4b7))

- Add init model policy
  ([`bd4ba88`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/bd4ba8826b461641888a88aa3251afbdc993ec28))

- Add init_data to dist
  ([`9bb5327`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/9bb5327de86ede59cbdae96495088f4cba13878f))

- Add iter_max to ft workflow
  ([`681cd51`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/681cd5115ca1d85c9cfa839406b816cf2ab484f2))

- Add numb_models to dist wf
  ([`c620187`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/c620187eeecbd6149faee4f5e8388553dcf59407))

- Add pre-commit
  ([`f75aba6`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/f75aba6069e103421a812b13413e193fcdc61437))

- Add semantic-version
  ([`71ec75b`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/71ec75b2c250523b26db06dee1f6c3c5fd885ac6))

- Add semantic-version
  ([`3e87da8`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/3e87da8d7dbd404414758ae482eda2d0e1aabf4e))

- Add unit test for collect_data
  ([`f1bf082`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/f1bf08271efdbd2252abe48902353cee8dafeb22))

- Bug
  ([`4f8dea1`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/4f8dea170f511f7ec5601c4b3b9701574c960bc8))

- Bugs with ci-test
  ([`e988f99`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/e988f99ad8a493a66b210fd249005d2cbf5f4809))

- Bugs with ci-test
  ([`3ea9520`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/3ea9520b629eae729eeed5421306f3df5a9fb999))

- Bugs with github workflow
  ([`96e2eda`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/96e2eda97d3bbf8b630ef2aa8af084a778bba138))

- Change doc for pfd
  ([`8556703`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/855670339fbb0f81bfde1c292829f4379af989b6))

- Change import module to pfd
  ([`5eac94f`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/5eac94f24b1b0d8ee5b4fcdb01bf113e33a0631d))

- Change init version
  ([`20eb6b8`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/20eb6b869b0e535731537cd682d71bfe91b5aaba))

- Change module name
  ([`8c19083`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/8c19083c2f32e139b659f6898d4d9ba4efcd179f))

- Change name from pdf to pfd
  ([`4c8352e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/4c8352e61f112a1d25cccc0bba4a1bea4b3a22dc))

- Change package name to pfd
  ([`07d998f`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/07d998fcb9e8b8e8bd86dd9602c8dd7e0ebb7f79))

- Change to python-semantic-release
  ([`a0a8e4f`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/a0a8e4f91c48416714587333626b9ead32299e4b))

- Delete excessive example files
  ([`81dec9e`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/81dec9ea6ec540b59a7b628f560b3d3ed1252d0d))

- Delete redundent config
  ([`31a3b62`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/31a3b6294f2c5e8c470e76cb39504c636723e55e))

- Enable optional fp style
  ([`480db90`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/480db9016ebd2835ea143cf91e2c77248410587b))

- First major commit
  ([`63c6d6d`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/63c6d6d9eaa8ea686fd00b30dfbf31548ab506fe))

- Fix bugs with finetune
  ([`e8e3f05`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/e8e3f054a5cc765c0aea52986887bd452f3cd39f))

- Fix import issue
  ([`de04905`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/de04905fd40c2a9ad954908113bd02f4bdd61e12))

- Fix issue with exploration
  ([`c833065`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/c8330652fc52ac2176319249d7f45fb170f154a0))

- Fix issue with select_conf_config
  ([`117dbb3`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/117dbb35d329e70bd40d8d25fd27074c1787c9d7))

- Fix issues with data filter
  ([`e5aac22`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/e5aac22f095b7c1ef87e9e5700d93cacb18de9c3))

- Fix issues with dpdata abacus
  ([`5f302ed`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/5f302ed71e55ac497e4695992555504ee07e16c0))

- Fix issues with iter data
  ([`0ba12a0`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/0ba12a0dee35ab6dc2688468a09bfab289549dc6))

- Fix issues with pytorch model
  ([`30ffb5f`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/30ffb5f5622bad2792e949c2b0e0c6b8da7b5b59))

- Fix minor bug
  ([`5961d60`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/5961d6060c8b6612bb99ff15da01dba2cd1fb0bf))

- Fix minor bugs
  ([`1748384`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/174838462629a3cc83caa427ee06a7fb8a79fcfd))

- Fix pop bug
  ([`f0d5a09`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/f0d5a090207d2e974408d3febb73f7f00d146a57))

- Fix RMSE force bug
  ([`4be8f44`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/4be8f44374f3ca2d416104fcdbf7d8b7531b1704))

- Fixing compatibility issues with dpgen2
  ([`38cd80d`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/38cd80d0090a0800a7b00b25a5f1663d36d0fb66))

- Improve artifact downloads
  ([`8e46780`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/8e467803bc95e0957e4949288a3346acfb6e0420))

- Improve docs
  ([`5c45044`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/5c45044d0885e24e30454361eead78ffff611360))

- Improve pert_gen module
  ([`69ed108`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/69ed10836e33701c8c443e2f274ef86d240d003f))

- Issue with test
  ([`7a68fcc`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/7a68fcca320ea4f778705c408756df92aa55ab30))

- Issue with test
  ([`a038030`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/a03803091671604d240c677d7e1d079963027683))

- Issues with python-semantic
  ([`e62cf2d`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/e62cf2db3a7a360b3ab4f9a7d18eb771f22cc921))

- Issues with test module
  ([`d76e57b`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/d76e57bf3044d651b0e34725944fba6bb49e8488))

- Major on zero
  ([`f9afa2b`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/f9afa2bb280b43205712688ea7d37abcdaa12fab))

- Major restructuring
  ([`8abfa4f`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/8abfa4facfb67d9574b2cafc3449fa34e523d379))

- Minor bugs
  ([`24f30b8`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/24f30b84e3fec0d408cb970ef4e9898b414d23f8))

- Minor bugs
  ([`17c3476`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/17c3476be776bb02ecf370911b438392d260fc87))

- Minor import issue
  ([`e013315`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/e0133151949a31c827386542a8e749035dea2fbe))

- Modify collect data
  ([`7d53af6`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/7d53af69ed8f43d7abd92c6327712a7c91fda44c))

- Modify help info for dl subcommand
  ([`a6de998`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/a6de998ebc719b8dc52d866a38f124e6825ce0f1))

- Modify resubmit cli
  ([`85cee42`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/85cee42de455a32ec6b3633beaa8bacc0b086f1f))

- Modify UI
  ([`7e48c69`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/7e48c69e042ac2032d1153f379793a34e5b2db85))

- Multi-conf
  ([`25c3fa5`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/25c3fa51e44d8bbb8067b8537e5dd876dd9384f0))

- New loop structure for ft workflow
  ([`37fac90`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/37fac907a26051030b2d906a25b2dcc930475f83))

- Recommit coverge.py
  ([`44f4bff`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/44f4bff80ae024264e0c21f0c824271a61620d5e))

- Remove user credentials
  ([`67b4ef0`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/67b4ef07a1c685dbc7478bfaa72c72c14787f6a9))

- Replace setup.py with pyproject.toml
  ([`ed0add3`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/ed0add37354507b758cb9f84cea0c661a8a4b6d5))

- Resolve issues with github workflows
  ([`713023d`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/713023dfccd766dc1177fa0f3c38aa7176b4c42b))

- Restructure dist workflow
  ([`318caef`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/318caefec988b2a3ae2e61ee7899e58536a51325))

- Semantic
  ([`8e94e48`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/8e94e480d9200fb653e45566e027a980e4a96024))

- Semantic
  ([`96f2b49`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/96f2b4955d9d6bc738f15aedf716d7b14931e86b))

- Semantic
  ([`8e12ba7`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/8e12ba7387680da7c6a1e6b751f722c0445c6c8c))

- Set default numb_model to 1
  ([`b5ff8ea`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/b5ff8ea62661858a9fab275b09934bd8063a5ac4))

- Test pre-commit
  ([`cbfd5c4`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/cbfd5c4c4d29b88b7577f1193b811cdfd242b17f))

- Untrack devel for semantic
  ([`5f0daa3`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/5f0daa3c9a8ccd53391a9af89e34e2d9bb05374f))

- Updata examples
  ([`f4d6643`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/f4d664363d4534e260c9080ea37087299ab79d7d))

- Update action permission
  ([`3bb78f9`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/3bb78f916faa842394784648fa9b14f8ec43415d))

- Update CLI
  ([`1855dd8`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/1855dd829d2ff72db8ab30517089f33f03a8e0df))

- Update dependency
  ([`c0c12f0`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/c0c12f0b44c45c927a740e51c508a039dd98563c))

- Update doc and examples
  ([`b0ef4cb`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/b0ef4cbe0f54784819e283409d5b39044b4bcc1f))

- Update docs
  ([`428784b`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/428784b4819c42187ccbec7c18dfcd159b164cfe))

- Update download setting
  ([`d7649a2`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/d7649a2605207c8fe9839dbc22758aca63dcfd15))

- Update examples and doc
  ([`5282a58`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/5282a58c8184df1439f8efdefa9f1f7c618de879))

- Update finetuen example.json
  ([`c67935c`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/c67935c6db12dec9e847f2b3aeea987be72fbf12))

- Update node version
  ([`e04fa8c`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/e04fa8c7dd9bae316b5a8f394de08daf50b7e664))

- Update node version
  ([`6a40880`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/6a40880d7d3fd6353555defc8be9d6ff4f0176c1))

- Update package name
  ([`5451254`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/545125409e55d2ca0f626891a16806421cbf8d9c))

- Update pylint build env
  ([`b4d0cd4`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/b4d0cd4e49e69cefe827e1f8bed08506aebfb507))

- Update python semantic
  ([`59c015b`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/59c015b34403a86fe5b125a2d02540d14f113318))

- Update release
  ([`96548d9`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/96548d9f69888b5ce5bd0b1ee862d1f78eb8af8f))

- Update resubmit cli
  ([`a60843c`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/a60843ce281a87ba505ba7599dd189d07ebdfdbb))

- Update secret
  ([`6a5573b`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/6a5573b2f6e388646248da2c9ce9d25ca41d2f92))

- Update secret
  ([`105073b`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/105073ba7ab92cd32a5aad9c16288a64cff372fc))

- Update secret
  ([`50796bd`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/50796bd74087b467ec914f8dfac8dc5e5532ee81))

- Update semantic
  ([`d5f1619`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/d5f16190339bb5ca129646703f25107869b0598c))

- Update semantic
  ([`a026c54`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/a026c549b89d95680ba352a439199599ceae2f1e))

- Update semantic
  ([`367eb5c`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/367eb5cfb7389584eb2905e1775110e31ecafb7f))

- Update setup.py
  ([`eba0019`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/eba00193effad9d7ff29c02067898e6b5be97120))

- Update token
  ([`55f163a`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/55f163a6d0c81d8a545a751069eb907483ca4927))

- Update toml
  ([`4b6e644`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/4b6e644a40800a25b531ad549eb8b5190fbd7547))

- Update toml
  ([`39c2379`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/39c23790137e15b72af635dcff79624c60960ae9))

- Update unittest
  ([`953cc23`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/953cc238cf36d064e960475d1b73102ed5473488))

- Update url
  ([`ffc91b2`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/ffc91b2727c9961aff63d60aa154a1322cbcbb08))

- Update version info
  ([`d27c12c`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/d27c12c473c8ec75019fab08858181d80f33539c))

### Chores

- **release**: 1.0.0 [skip ci]
  ([`450c658`](https://github.com/ruoyuwang1995nya/pfd-kit/commit/450c6588aa7deaa6d0736b5dc8c61578d1b6d672))

# 1.0.0 (2024-09-28)

### Bug Fixes

* add ase to setup file
  ([730da07](https://github.com/ruoyuwang1995nya/dp-distill/commit/730da079179067a7a5c8d5742696a9fed44df2c0))
  * add ci test module
  ([6fde807](https://github.com/ruoyuwang1995nya/dp-distill/commit/6fde807818dbf772755346ab2406bb0ac81dc820))
  * add cli entrypoint
  ([98c39db](https://github.com/ruoyuwang1995nya/dp-distill/commit/98c39db14c1bba72f5aad5510a6902d5cc0e49cd))
  * add conf filter
  ([1e2e52e](https://github.com/ruoyuwang1995nya/dp-distill/commit/1e2e52e23602860f17f39f4593ed1e137e7588fd))
  * add dist loop
  ([36e6411](https://github.com/ruoyuwang1995nya/dp-distill/commit/36e64111c3b82aec5348ff64622f89a1090bdc1d))
  * add example file for iterative finetune
  ([c50f7c6](https://github.com/ruoyuwang1995nya/dp-distill/commit/c50f7c6877f50dcf39683a200c71e16775356e0a))
  * add examples and update docs
  ([ebc4c3c](https://github.com/ruoyuwang1995nya/dp-distill/commit/ebc4c3c6a9b3292b136efa849cb47a08bfe38777))
  * add filter to ft workflow
  ([4927f87](https://github.com/ruoyuwang1995nya/dp-distill/commit/4927f8778aed87ecac16d4deefc5f92b930cfe22))
  * add fine-tune module
  ([d4fc7ba](https://github.com/ruoyuwang1995nya/dp-distill/commit/d4fc7bada70b438a79fd60a148283dcbf1306116))
  * add INCAR to ft example
  ([708396c](https://github.com/ruoyuwang1995nya/dp-distill/commit/708396c4ae3de54bf8e749bec74de2121942a4b7))
  * add init model policy
  ([bd4ba88](https://github.com/ruoyuwang1995nya/dp-distill/commit/bd4ba8826b461641888a88aa3251afbdc993ec28))
  * add init_data to dist
  ([9bb5327](https://github.com/ruoyuwang1995nya/dp-distill/commit/9bb5327de86ede59cbdae96495088f4cba13878f))
  * add iter_max to ft workflow
  ([681cd51](https://github.com/ruoyuwang1995nya/dp-distill/commit/681cd5115ca1d85c9cfa839406b816cf2ab484f2))
  * add numb_models to dist wf
  ([c620187](https://github.com/ruoyuwang1995nya/dp-distill/commit/c620187eeecbd6149faee4f5e8388553dcf59407))
  * add pre-commit
  ([f75aba6](https://github.com/ruoyuwang1995nya/dp-distill/commit/f75aba6069e103421a812b13413e193fcdc61437))
  * add semantic-version
  ([71ec75b](https://github.com/ruoyuwang1995nya/dp-distill/commit/71ec75b2c250523b26db06dee1f6c3c5fd885ac6))
  * add semantic-version
  ([3e87da8](https://github.com/ruoyuwang1995nya/dp-distill/commit/3e87da8d7dbd404414758ae482eda2d0e1aabf4e))
  * add unit test for collect_data
  ([f1bf082](https://github.com/ruoyuwang1995nya/dp-distill/commit/f1bf08271efdbd2252abe48902353cee8dafeb22))
  * bugs with ci-test
  ([e988f99](https://github.com/ruoyuwang1995nya/dp-distill/commit/e988f99ad8a493a66b210fd249005d2cbf5f4809))
  * bugs with ci-test
  ([3ea9520](https://github.com/ruoyuwang1995nya/dp-distill/commit/3ea9520b629eae729eeed5421306f3df5a9fb999))
  * bugs with github workflow
  ([96e2eda](https://github.com/ruoyuwang1995nya/dp-distill/commit/96e2eda97d3bbf8b630ef2aa8af084a778bba138))
  * delete excessive example files
  ([81dec9e](https://github.com/ruoyuwang1995nya/dp-distill/commit/81dec9ea6ec540b59a7b628f560b3d3ed1252d0d))
  * enable optional fp style
  ([480db90](https://github.com/ruoyuwang1995nya/dp-distill/commit/480db9016ebd2835ea143cf91e2c77248410587b))
  * first major commit
  ([63c6d6d](https://github.com/ruoyuwang1995nya/dp-distill/commit/63c6d6d9eaa8ea686fd00b30dfbf31548ab506fe))
  * fix bugs with finetune
  ([e8e3f05](https://github.com/ruoyuwang1995nya/dp-distill/commit/e8e3f054a5cc765c0aea52986887bd452f3cd39f))
  * fix import issue
  ([de04905](https://github.com/ruoyuwang1995nya/dp-distill/commit/de04905fd40c2a9ad954908113bd02f4bdd61e12))
  * fix issue with exploration
  ([c833065](https://github.com/ruoyuwang1995nya/dp-distill/commit/c8330652fc52ac2176319249d7f45fb170f154a0))
  * fix issue with select_conf_config
  ([117dbb3](https://github.com/ruoyuwang1995nya/dp-distill/commit/117dbb35d329e70bd40d8d25fd27074c1787c9d7))
  * fix issues with data filter
  ([e5aac22](https://github.com/ruoyuwang1995nya/dp-distill/commit/e5aac22f095b7c1ef87e9e5700d93cacb18de9c3))
  * fix issues with dpdata abacus
  ([5f302ed](https://github.com/ruoyuwang1995nya/dp-distill/commit/5f302ed71e55ac497e4695992555504ee07e16c0))
  * fix issues with iter data
  ([0ba12a0](https://github.com/ruoyuwang1995nya/dp-distill/commit/0ba12a0dee35ab6dc2688468a09bfab289549dc6))
  * fix issues with pytorch model
  ([30ffb5f](https://github.com/ruoyuwang1995nya/dp-distill/commit/30ffb5f5622bad2792e949c2b0e0c6b8da7b5b59))
  * fix minor bug
  ([5961d60](https://github.com/ruoyuwang1995nya/dp-distill/commit/5961d6060c8b6612bb99ff15da01dba2cd1fb0bf))
  * fix minor bugs
  ([1748384](https://github.com/ruoyuwang1995nya/dp-distill/commit/174838462629a3cc83caa427ee06a7fb8a79fcfd))
  * fix pop bug
  ([f0d5a09](https://github.com/ruoyuwang1995nya/dp-distill/commit/f0d5a090207d2e974408d3febb73f7f00d146a57))
  * fix RMSE force bug
  ([4be8f44](https://github.com/ruoyuwang1995nya/dp-distill/commit/4be8f44374f3ca2d416104fcdbf7d8b7531b1704))
  * fixing compatibility issues with dpgen2
  ([38cd80d](https://github.com/ruoyuwang1995nya/dp-distill/commit/38cd80d0090a0800a7b00b25a5f1663d36d0fb66))
  * improve artifact downloads
  ([8e46780](https://github.com/ruoyuwang1995nya/dp-distill/commit/8e467803bc95e0957e4949288a3346acfb6e0420))
  * improve docs
  ([5c45044](https://github.com/ruoyuwang1995nya/dp-distill/commit/5c45044d0885e24e30454361eead78ffff611360))
  * improve pert_gen module
  ([69ed108](https://github.com/ruoyuwang1995nya/dp-distill/commit/69ed10836e33701c8c443e2f274ef86d240d003f))
  * issue with test
  ([7a68fcc](https://github.com/ruoyuwang1995nya/dp-distill/commit/7a68fcca320ea4f778705c408756df92aa55ab30))
  * issue with test
  ([a038030](https://github.com/ruoyuwang1995nya/dp-distill/commit/a03803091671604d240c677d7e1d079963027683))
  * issues with test module
  ([d76e57b](https://github.com/ruoyuwang1995nya/dp-distill/commit/d76e57bf3044d651b0e34725944fba6bb49e8488))
  * major restructuring
  ([8abfa4f](https://github.com/ruoyuwang1995nya/dp-distill/commit/8abfa4facfb67d9574b2cafc3449fa34e523d379))
  * minor bugs
  ([17c3476](https://github.com/ruoyuwang1995nya/dp-distill/commit/17c3476be776bb02ecf370911b438392d260fc87))
  * minor import issue
  ([e013315](https://github.com/ruoyuwang1995nya/dp-distill/commit/e0133151949a31c827386542a8e749035dea2fbe))
  * modify collect data
  ([7d53af6](https://github.com/ruoyuwang1995nya/dp-distill/commit/7d53af69ed8f43d7abd92c6327712a7c91fda44c))
  * modify help info for dl subcommand
  ([a6de998](https://github.com/ruoyuwang1995nya/dp-distill/commit/a6de998ebc719b8dc52d866a38f124e6825ce0f1))
  * modify resubmit cli
  ([85cee42](https://github.com/ruoyuwang1995nya/dp-distill/commit/85cee42de455a32ec6b3633beaa8bacc0b086f1f))
  * modify UI
  ([7e48c69](https://github.com/ruoyuwang1995nya/dp-distill/commit/7e48c69e042ac2032d1153f379793a34e5b2db85))
  * multi-conf
  ([25c3fa5](https://github.com/ruoyuwang1995nya/dp-distill/commit/25c3fa51e44d8bbb8067b8537e5dd876dd9384f0))
  * new loop structure for ft workflow
  ([37fac90](https://github.com/ruoyuwang1995nya/dp-distill/commit/37fac907a26051030b2d906a25b2dcc930475f83))
  * recommit coverge.py
  ([44f4bff](https://github.com/ruoyuwang1995nya/dp-distill/commit/44f4bff80ae024264e0c21f0c824271a61620d5e))
  * remove user credentials
  ([67b4ef0](https://github.com/ruoyuwang1995nya/dp-distill/commit/67b4ef07a1c685dbc7478bfaa72c72c14787f6a9))
  * resolve issues with github workflows
  ([713023d](https://github.com/ruoyuwang1995nya/dp-distill/commit/713023dfccd766dc1177fa0f3c38aa7176b4c42b))
  * restructure dist workflow
  ([318caef](https://github.com/ruoyuwang1995nya/dp-distill/commit/318caefec988b2a3ae2e61ee7899e58536a51325))
  * set default numb_model to 1
  ([b5ff8ea](https://github.com/ruoyuwang1995nya/dp-distill/commit/b5ff8ea62661858a9fab275b09934bd8063a5ac4))
  * test pre-commit
  ([cbfd5c4](https://github.com/ruoyuwang1995nya/dp-distill/commit/cbfd5c4c4d29b88b7577f1193b811cdfd242b17f))
  * updata examples
  ([f4d6643](https://github.com/ruoyuwang1995nya/dp-distill/commit/f4d664363d4534e260c9080ea37087299ab79d7d))
  * update action permission
  ([3bb78f9](https://github.com/ruoyuwang1995nya/dp-distill/commit/3bb78f916faa842394784648fa9b14f8ec43415d))
  * update CLI
  ([1855dd8](https://github.com/ruoyuwang1995nya/dp-distill/commit/1855dd829d2ff72db8ab30517089f33f03a8e0df))
  * update dependency
  ([c0c12f0](https://github.com/ruoyuwang1995nya/dp-distill/commit/c0c12f0b44c45c927a740e51c508a039dd98563c))
  * update doc and examples
  ([b0ef4cb](https://github.com/ruoyuwang1995nya/dp-distill/commit/b0ef4cbe0f54784819e283409d5b39044b4bcc1f))
  * update docs
  ([428784b](https://github.com/ruoyuwang1995nya/dp-distill/commit/428784b4819c42187ccbec7c18dfcd159b164cfe))
  * update download setting
  ([d7649a2](https://github.com/ruoyuwang1995nya/dp-distill/commit/d7649a2605207c8fe9839dbc22758aca63dcfd15))
  * update examples and doc
  ([5282a58](https://github.com/ruoyuwang1995nya/dp-distill/commit/5282a58c8184df1439f8efdefa9f1f7c618de879))
  * update finetuen example.json
  ([c67935c](https://github.com/ruoyuwang1995nya/dp-distill/commit/c67935c6db12dec9e847f2b3aeea987be72fbf12))
  * update node version
  ([e04fa8c](https://github.com/ruoyuwang1995nya/dp-distill/commit/e04fa8c7dd9bae316b5a8f394de08daf50b7e664))
  * update node version
  ([6a40880](https://github.com/ruoyuwang1995nya/dp-distill/commit/6a40880d7d3fd6353555defc8be9d6ff4f0176c1))
  * update release
  ([96548d9](https://github.com/ruoyuwang1995nya/dp-distill/commit/96548d9f69888b5ce5bd0b1ee862d1f78eb8af8f))
  * update resubmit cli
  ([a60843c](https://github.com/ruoyuwang1995nya/dp-distill/commit/a60843ce281a87ba505ba7599dd189d07ebdfdbb))
  * update secret
  ([6a5573b](https://github.com/ruoyuwang1995nya/dp-distill/commit/6a5573b2f6e388646248da2c9ce9d25ca41d2f92))
  * update secret
  ([105073b](https://github.com/ruoyuwang1995nya/dp-distill/commit/105073ba7ab92cd32a5aad9c16288a64cff372fc))
  * update secret
  ([50796bd](https://github.com/ruoyuwang1995nya/dp-distill/commit/50796bd74087b467ec914f8dfac8dc5e5532ee81))
  * update setup.py
  ([eba0019](https://github.com/ruoyuwang1995nya/dp-distill/commit/eba00193effad9d7ff29c02067898e6b5be97120))
  * update url
  ([ffc91b2](https://github.com/ruoyuwang1995nya/dp-distill/commit/ffc91b2727c9961aff63d60aa154a1322cbcbb08))
  * update version info
  ([d27c12c](https://github.com/ruoyuwang1995nya/dp-distill/commit/d27c12c473c8ec75019fab08858181d80f33539c))
