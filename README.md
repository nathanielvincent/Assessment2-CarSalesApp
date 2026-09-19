# Car Sales Analytics Application Information
## How To Run The Program:
1. Download the files for this application.
2. Download and install Python.
3. **If you are proving your own custom data**, place your `.csv` file in the same working directory as `main.py`, or ideally within `./data`.
The program will automatically detect your `.csv` file and ask you which file to use when you start the program. 
4. Create a Virtual Environment (venv) and make sure you enable it for your workspace.
5. In the same working directory as `main.py`, run the two following commands;
   - `pip install -r requirements.txt`
   - `python main.py` (Possibly `python3 main.py`, depending on your installation!)

## How To Run Test Cases:
Automated testing can be completed by following these steps;
1. Complete all the steps from `How To Run The Program` above **up to, and including** `pip_install -r requirements.txt`.
2. In the same working directory as `automated_tests.py`, run `pytest automated_tests.py`

The output of this should contain a big green line at the bottom and say that the tests passed. 
If anything is wrong, it will include a red "X failed" counter, where X is the test count that failed.

## How Manual Testing Was Done:
Manual testing was completed as development went on, 
for example manually testing each and every individual item in the terminal user interface 
to ensure they all work correctly and as expected.

**⚠️This testing below was done on the `test_set_small.csv` file provided by me in this repository** so outputs validity can be checked.
For reproducability, when the program prompts you to pick a dataset to read from, select `test_set_small.csv`.

**⚠ Some shown data does not precisely match the terminal output**, it displays the same data that the terminal outputs, 
but in a different format better suited for a markdown table.

| Command Line Menu Input | Expected Result                                                            | Actual Result                                                              | Worked First Try? |
|-------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|-------------------|
| (Nothing)               | !! That is not a valid option, please try again. Press Enter to dismiss !! | !! That is not a valid option, please try again. Press Enter to dismiss !! | Yes               |
| q                       | !! That is not a valid option, please try again. Press Enter to dismiss !! | !! That is not a valid option, please try again. Press Enter to dismiss !! | Yes               |
| 1                       | There have been a total of 5 sales.                                        | There have been a total of 5 sales.                                        | Yes               |
| 2                       | The total amount of revenue made from car sales is $106000.00.             | The total amount of revenue made from car sales is $106000.00.             | Yes               |
| 3                       | `Ben: 2 Sales`, `Emily: 1 Sale`, `Mark: 1 Sale`, `Joe: 1 Sale`.            | `Ben: 2 Sales`, `Emily: 1 Sale`, `Mark: 1 Sale`, `Joe: 1 Sale`.            | Yes               |
| 4                       | The most sold car make is Honda.                                           | The most sold car make is Honda.                                           | Yes               |
| 5                       | The least sold car make and model is Tesla Model 3.                        | The least sold car make and model is Tesla Model 3.                        | Yes               |
| 6                       | `Ben: $35000.00`, `Emily: $16000.00`, `Mark: $12000.00`, `Joe: $8000.00`   | `Ben: $35000.00`, `Emily: $16000.00`, `Mark: $12000.00`, `Joe: $8000.00`   | Yes               |
| 7                       | Ben has the highest sale average.                                          | Ben has the highest sale average.                                          | Yes               |
| 9                       | The most profitable month in the dataset is 2026-06.                       | The most profitable month in the dataset is 2026-06.                       | Yes               |
| 10                      | (Program closes)                                                           | (Program closes)                                                           | Yes               |
| 11                      | !! That is not a valid option, please try again. Press Enter to dismiss !! | !! That is not a valid option, please try again. Press Enter to dismiss !! | Yes               |
