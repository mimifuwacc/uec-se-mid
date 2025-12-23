import unittest
from tests.test_rpn_calculator import (
    TestRPNCalculatorNormalCases,
)


def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestRPNCalculatorNormalCases))

    return suite


if __name__ == "__main__":
    unittest.main()
