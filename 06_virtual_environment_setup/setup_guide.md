# Virtual environment setup guide in python:

- **Step-1:** `pip install virtualenv`

- **Step-2:** visit this website: <b><i> https://github.com/pypa/virtualenv </b> **or** <b><i> https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/ </b></i>

- **Step-3:** visit this website <b><i> https://virtualenv.pypa.io/en/latest/user_guide.html </b></i> and follow these steps

<p style="text-align:center; font-weight: bold; font-size: 30px;">OR</p>

- **Step-1:** `pip install virtualenv`

- **Step-2:** Go to current directory and run command `virtualenv venv` or `python -m venv`

- **Step-3:** Go to current directory and run command `.\env_name\Scripts\activate`

- **Step-4:** Confirm that the env is successfully selected
  `which python`

- **Step-5:** Install required packages
  `pip install -r requirements.txt`

- **Step-6:** run `deactivate` to exit virtual environment

### Some important commands:

- `virtualenv --version` : to check version of virtualenv

- `deactivate` : to exit virtual environment

- `virtualenv --help` : to get help

- `pip install package_name` : to install packages in virtual environment

- `pip uninstall package_name` : to uninstall packages in virtual environment

- `pip list` : to list packages in virtual environment

- `pip freeze` : to freeze packages in virtual environment

- `pip list > requirements.txt` : to add all packages in 
virtual environment to requirements.txt file

- `pip install -r requirements.txt` : to install packages from requirements.txt file
