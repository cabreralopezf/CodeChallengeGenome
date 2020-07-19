import unittest
import TestFramework.TestCases.AllScenarios as Everything
import HtmlTestRunner
import os


class HtmlTestRunnerTestSuite(unittest.TestCase):
    # This class can be run to execute the tests and also provide a report html on completion, this can be reused with
    # multiple reporting frameworks.
    def test_code_challenge(self):
        # Create Test suite
        consolidated_test = unittest.TestSuite()

        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Everything.AllScenarios)
        ])
        # Output Directory and Test Runner
        root_dir = os.path.dirname(os.path.abspath(__file__))
        html_runner = HtmlTestRunner.HTMLTestRunner(output=root_dir + '/Reports/')
        html_runner.run(consolidated_test)


if __name__ == '__main__':
    unittest.main()
