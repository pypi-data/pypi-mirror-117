<!--
  THIS FILE IS EXCLUSIVELY MAINTAINED IN THE NAMESPACE ROOT PACKAGE. CHANGES HAVE TO BE DONE THERE.
-->
# droid portion of ae namespace package

[![GitLab develop](https://img.shields.io/gitlab/pipeline/ae-group/ae_droid/develop?logo=python)](
    https://gitlab.com/ae-group/ae_droid)
[![GitLab release](https://img.shields.io/gitlab/pipeline/ae-group/ae_droid/release?logo=python)](
    https://gitlab.com/ae-group/ae_droid/-/tree/release)
[![PyPIVersion](https://img.shields.io/pypi/v/ae_droid)](
    https://pypi.org/project/ae-droid/#history)

>this portion belongs to the `Application Environment for Python` - the `ae` namespace, which provides
useful classes and helper methods to develop full-featured applications with Python, running on multiple platforms.

[![Coverage](https://ae-group.gitlab.io/ae_droid/coverage.svg)](
    https://ae-group.gitlab.io/ae_droid/coverage/ae_droid_py.html)
[![MyPyPrecision](https://ae-group.gitlab.io/ae_droid/mypy.svg)](
    https://ae-group.gitlab.io/ae_droid/lineprecision.txt)
[![PyLintScore](https://ae-group.gitlab.io/ae_droid/pylint.svg)](
    https://ae-group.gitlab.io/ae_droid/pylint.log)

[![PyPIImplementation](https://img.shields.io/pypi/implementation/ae_droid)](
    https://pypi.org/project/ae-droid/)
[![PyPIPyVersions](https://img.shields.io/pypi/pyversions/ae_droid)](
    https://pypi.org/project/ae-droid/)
[![PyPIWheel](https://img.shields.io/pypi/wheel/ae_droid)](
    https://pypi.org/project/ae-droid/)
[![PyPIFormat](https://img.shields.io/pypi/format/ae_droid)](
    https://pypi.org/project/ae-droid/)
[![PyPIStatus](https://img.shields.io/pypi/status/ae_droid)](
    https://libraries.io/pypi/ae-droid)
[![PyPIDownloads](https://img.shields.io/pypi/dm/ae_droid)](
    https://pypi.org/project/ae-droid/#files)


## installation


execute the following command to use the ae.droid module in your application. it will install ae.droid
into your python (virtual) environment:
 
```shell script
pip install ae-droid
```

if you want to contribute to this portion then first fork
[the ae_droid repository at GitLab](https://gitlab.com/ae-group/ae_droid "ae.droid code repository"). after that pull
it to your machine and finally execute the following command in the root folder of this repository (ae_droid):

```shell script
pip install -e .[dev]
```

the last command will install this module portion into your virtual environment, along with the tools you need
to develop and run tests or to extend the portion documentation. to contribute to the unit tests or to the documentation
of this portion, replace the setup extras key `dev` in the above command with `tests` or `docs` respectively.


## namespace portion documentation

detailed info on the features and usage of this portion is available at
[ReadTheDocs](https://ae.readthedocs.io/en/latest/_autosummary/ae.droid.html#module-ae.droid
"ae_droid documentation").

<!-- common files version 0.2.81 deployed package/portion version 0.2.9)
     to https://gitlab.com/ae-group as ae_droid module as well as
     to https://ae-group.gitlab.io with CI check results as well as
     to https://pypi.org/project/ae-droid as namespace portion ae-droid.
-->
