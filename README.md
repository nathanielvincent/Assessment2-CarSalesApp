# Car Sales Analytics Application Information
## How To Run The Program:
1. Download the files for this application.
2. Download and install Python.
3. **If you are proving your own custom data**, replace provided `car_sales.csv` with your own custom data.
4. Create a Virtual Environment (venv) and make sure you enable it for your workspace. 
5. In the same working directory as `main.py`, run the two following commands;
   - `pip install -r requirements.txt`
   - `python main.py` (Possibly `python3 main.py` depending on your installation!)

## How To Run Test Cases:
Automated testing can be completed by following these steps;
1. Complete the steps from `How To Run The Program` above **first**.
2. In the same working directory as `automated_tests.py`, run `pytest automated_tests.py`

The output of this should have a big green line at the bottom and say that the tests passed. If anything is wrong,
it will include a red "X failed" counter.

## How Manual Testing Was Done:
Manual testing was completed as development went on, 
for example manually testing each and every individual item in the terminal user interface 
to ensure they all work correctly and as expected.

This testing below was done on the provided `test_set_small.csv` file so I can validate the outputs are correct.
You will have to change the file the code is reading from in `constants.py` if you wish to validate my validation.

| Command Line Menu Input | Expected Result                                                            | Actual Result                                                              | Worked First Try? |
|-------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|-------------------|
| (Nothing)               | !! That is not a valid option, please try again. Press Enter to dismiss !! | !! That is not a valid option, please try again. Press Enter to dismiss !! | Yes               |
| q                       | !! That is not a valid option, please try again. Press Enter to dismiss !! | !! That is not a valid option, please try again. Press Enter to dismiss !! | Yes               |
| 4                       | The most sold car make is Honda.                                           | The most sold car make is Honda.                                           | Yes               |
| 2                       | The total amount of revenue made from car sales is $106000.00.             | The total amount of revenue made from car sales is $106000.00.             | Yes               |
| 7                       | Ben has the highest sale average.                                          | Ben has the highest sale average.                                          | Yes               |
