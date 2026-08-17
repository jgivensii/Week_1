#Warehouse Restock Project

##Virtual Environment Set-Up (*Windows Devices*)
**To establish a new virtual environment:**
1. Open up a Powershell terminal and enter `python -m venv .venv`
2. To activate the virtual environment, enter `.venv\Scripts\Activate.ps1`


##Dependencies Installation (*Windows Devices*)
To ensure the code will properly run, the same dependencies must be installed. They are included in the in the pyproject.toml file. **To ensure proper installation, ensure you are in the root directory for this project and execute the following command into a Powershell terminal:** `pip install -e .` 
(***Verify that the proper versions of python and pip are installed prior***) 

##Running the Test Suite (*Windows Devices*)
To run the test suite and validate all tests conducted on this project, the same test environment dependencies must be installed. They are included in the in the pyproject.toml file as well. **To ensure proper installation, ensure you are in the root directory for this project and execute the following command into a Powershell terminal:** `pip install -e .[test]` 
(***Verify that the proper versions of python and pip are installed prior***) 
This will install the pytest module, to run the pytest module to validate all tests, enter the following command into the terminal: `pytest -q`. 
