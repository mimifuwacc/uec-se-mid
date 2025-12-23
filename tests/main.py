import unittest
from tests.test_rpn_calculator import (
    TestRPNCalculatorNormalCases,
    TestRPNCalculatorErrorCases,
)


def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestRPNCalculatorNormalCases))
    suite.addTests(loader.loadTestsFromTestCase(TestRPNCalculatorErrorCases))

    return suite


if __name__ == "__main__":
    unittest.main()
