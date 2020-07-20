# CodeChallengeGenome
This is my take on the automated test part of the challenge, the project is done using the Page Object pattern/model for automated frameworks.

## Requirements
In order to run the tests the web browser Chrome version 84.0 or higher is required.
Also it is required to use Python 3.8 or newer to run this.

Before running make sure to install the required libraries from terminal in the root of the project. This can be done with the command: 

```shell
pip install -r requirements.txt
```
## Usage

In order to run the tests from terminal the location must be the root of the project. To run from terminal type the command:

```shell
python -m Reporting.CodeChallengeTestPlan
```
This command will run a version of the test that will create a report in the Reporting/Reports Folder.

Also the tests can be run as a unit test from the terminal the same way from root of the project with the command:

```shell
python -m unittest TestFramework.TestCases.AllScenarios
```

## Additional Comments
Since this only had one test case I only created one file with the test cases, but with growing test cases and test plans, abstracting can be done and refactoring some code to fit the maintainability.

Just wanted to mention one rule while doing automated tests is to try to not abstract more than necessary, so I tried to keep this project simple due to the small scope and complexity.

There are multiple comments through the code that are there just to guide through the process, but normally final codes for deployment have less comments as everyone understands the scope of the test cases, test plans and knows what the code intent is.
