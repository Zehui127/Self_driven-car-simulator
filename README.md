# AUDRI
Learning to drive using inverse reinforcement learning

![alt text](https://github.com/Zehui127/Self_driven-car-simulator/blob/master/demo.JPG)
### Copy rights
Many work of the similator is also done together by William and other team members 


## Dependencies

### Python
__Python 3.6__ is used in this project. The __64-bit__ version is required for the
Tensorflow library.

__Windows__:  
Download and install from [the Python website](https://www.python.org/downloads/windows)

__macOS__:  
Using [Homebrew](https://brew.sh): `$ brew install python3`  
OR download and install from [the Python website](https://www.python.org/downloads/mac-osx)  

__Linux__:  
Install using your package manager. The package is likely named `python` or
`python3`

### PyPI
This is the official Python package manager, used to install the Python
dependencies

The dependencies are given in [`requirements.pip`](requirements.pip)  
To install them: `$ pip install -r requirements.pip`

## Code quality
This project (mostly) follows the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008)  

For more details check the [code guidelines](docs/code.md)

### Checking for code quality
We use [Pylint](https://www.pylint.org) to check that the code style is being applied  
Our Pylint settings are provided in [`pylintrc`](pylintrc)  

To check the quality of all source code (i.e. in the [`src/`](src) folder):  
`$ find src/ -iname '*.py' |xargs pylint`  
Run the above from the root of the repository
