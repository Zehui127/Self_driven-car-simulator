# AUDRI
Learning to drive using inverse reinforcement learning

[Slack](https://audri.slack.com) - we do most of our online communication here  
[Issue board](https://projects.cs.nott.ac.uk/grp17-todo/audri/boards) - we keep track of tasks on the GitLab issue boards.  
Meetings are planned and documented using issues labelled [~meeting](https://projects.cs.nott.ac.uk/grp17-todo/audri/issues?scope=all&utf8=%E2%9C%93&state=all&label_name[]=meeting)  
Documents related to the project can be found in the [`docs`](docs/) directory  
[Timeline](docs/timeline.md) - the project's development plan, including necessary features and
their deadlines

### Team members
Pierce James Morris (@psypm)  
Amber Elliott (@psyale) - Team leader  
Cameron Hubbard (@psych4)  
William Vigolo da Silva (@psywv) - Git master  
Zehui Li (@psyzl3)  
Hao Sun (@psyhs2)  

[GitLab group](https://projects.cs.nott.ac.uk/groups/grp17-todo/group_members)

### Supervisor
Ender Özcan ([ender.ozcan@nottingham.ac.uk](mailto:ender.ozcan@nottingham.ac.uk))

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
