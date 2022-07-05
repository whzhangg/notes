
# Installing Python Packages (in development mode)
##### Some slightly outdated references I've seen
- (2012) https://python-packaging.readthedocs.io/en/latest/about.html
- (2019) https://stefanoborini.com/current-status-of-python-packaging/
### Project structure
A General link: https://setuptools.pypa.io/en/latest/setuptools.html
##### Folder structure
Some posts I visited are listed:
- The following [stackoverflow discussions](https://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application) suggest different practice for the folder structure.
- Another [informative post](https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/) suggesting the folder structure similar to the structure I adapt, as well as the setup files (.toml, .cfg, .py)
- Here is the sample project [Github](https://github.com/pypa/sampleproject) recommended by PyPa (Python Packaging Authority). *This is similar to what I adopt*

This is my template project:
![[python example project tree.png|200]]

##### toml file
In the `.toml` file, only build information is included, as shown in the following:
```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```
This follows https://setuptools.pypa.io/en/latest/userguide/quickstart.html#basic-use

##### setup.py file
Using `setup.py` is discouraged, but it (its existance) maybe needed in some build process. A bare minimum file like the following satisfies:
```python
from setuptools import setup

if __name__ == "__main__":
	setup()
```
Following https://setuptools.pypa.io/en/latest/userguide/quickstart.html#development-mode

##### setup.cfg
I use `setup.cfg` for most of the package informations. A Guide can be found [here](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html) including the file gramma. The following is an example:
```toml
[metadata]
name = myrandproj
version = 0.1
description = serve as an example
author = wenhao Zhang
author_email = wenhao997@yahoo.com

[options]
package_dir =
	= src
packages = find:
python_requires = >=3.8
install_requires =
	requests
	beautifulsoup4
	numpy

[options.packages.find]
where = src
```

Two points for reference:
1. keywords are similar to the keyword arguments in `setup.py` and can be found [here](https://setuptools.pypa.io/en/latest/references/keywords.html)
2. With the `src/` layout, [this section](- [This](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html#using-a-src-layout) is an in) provide an instruction

### Installation
##### Install in development mode
A reference from pip documentation is [here](https://pip.pypa.io/en/stable/topics/local-project-installs/)

`pip install -e .` install the package in the current folder, where setup files can be found. `--no-deps` option prevent installing dependencies. Such a development mode installation seems to have two effect:
- create an egg-info along with the package folder in the development directory (eg. in the `src/` folder) and link it to `site-packages` (`miniconda3/envs/pymat/lib/python3.8/site-packages`). 
- setuptools seems to add the package directory to `sys.path` by some ways, (maybe in the `easy-install.pth` file in `site-packages`) but I'm not sure

##### Remove installed package in development mode
`pip show package` shows the package information. To uninstall, `pip uninstall package` does the job. During uninstall, pip will also read any .egg-info/ folder contained in the current directory. If that folder is outdated, pip will report error. In these cases, we need to simply remove these folders.

For a manual uninstall, see here: https://stackoverflow.com/questions/17346619/how-to-uninstall-editable-packages-with-pip-installed-with-e

### License
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository