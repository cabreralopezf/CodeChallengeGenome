# CodeChallengeGenome

This is my take on the automated test part of the challenge, the project is done using the Page Object pattern/model for automated frameworks.

In order to run the tests the web browser Chrome version 84.0 or higher is required.

The requirements.txt file can be used to install the libraries needed like selenium and html-testRunner.

In order to use these tests the file in the project structure "TestFramework/TestCases/AllScenarios.py" could be used ran as a unit test.

I created another python file to run the tests as a test plan with a basic reporting framework. The file is located in the project structure "Reports/CodeChallengeTestPlan.py", this format can be changed and accomodated, since this only had one test case I only created one file with the test cases, but with growing test cases and test plans, abstracting can be done and refactoring some code to fit the maintainability.

Just wanted to mention one rule while doing automated tests is to try to not abstract more than necessary, so I tried to keep this project simple due to the small scope and complexity.

There are multiple comments through the code that are there just to guide through the process, but normally final codes for deployment have less comments as everyone understands the scope of the test cases, test plans and knows what the code intent is.
