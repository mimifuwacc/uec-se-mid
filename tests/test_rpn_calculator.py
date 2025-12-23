"""
逆ポーランド記法 (RPN) 電卓のテストケース
テストシナリオ `docs/test-plan.md` に基づいて作成
"""

import unittest
from src.main import calculate_rpn


class TestRPNCalculatorNormalCases(unittest.TestCase):
    """正常系のテストケース"""

    def test_addition(self):
        """加算が正しく行えること"""
        self.assertEqual(calculate_rpn("3 4 +"), 7)

    def test_subtraction(self):
        """減算が正しく行えること"""
        self.assertEqual(calculate_rpn("5 2 -"), 3)

    def test_multiplication(self):
        """乗算が正しく行えること"""
        self.assertEqual(calculate_rpn("3 4 *"), 12)
