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

    def test_division_integer_result(self):
        """除算の結果が整数になること（割り切れる場合）"""
        self.assertEqual(calculate_rpn("6 2 /"), 3)

    def test_division_decimal_result(self):
        """除算の結果が小数になること（割り切れない場合）"""
        self.assertEqual(calculate_rpn("5 2 /"), 2.5)

    def test_complex_expression_three_terms(self):
        """3項以上の複合演算が行えること"""
        self.assertEqual(calculate_rpn("3 4 + 2 *"), 14)  # (3 + 4) * 2 = 14

    def test_complex_expression_four_terms(self):
        """4項の複合演算が行えること"""
        self.assertEqual(
            calculate_rpn("5 1 2 + 4 * + 3 -"), 14
        )  # 5 + ((1 + 2) * 4) - 3 = 14

    def test_decimal_numbers(self):
        """小数同士の演算が正しく行えること"""
        self.assertEqual(calculate_rpn("3.5 2.5 +"), 6.0)

    def test_negative_numbers(self):
        """負数を含む演算が正しく行えること"""
        self.assertEqual(calculate_rpn("-3 4 +"), 1)

    def test_decimal_negative_numbers(self):
        """小数と負数を両方含む演算が正しく行えること"""
        self.assertEqual(calculate_rpn("-3.5 4.5 +"), 1.0)


class TestRPNCalculatorErrorCases(unittest.TestCase):
    """異常系のテストケース"""

    def test_insufficient_operands(self):
        """演算子の前にオペランドが1つしかない場合のエラー"""
        self.assertRaisesRegex(
            ValueError, "^オペランドが不足しています$", calculate_rpn, "1 +"
        )

    def test_insufficient_operators(self):
        """計算後に数字が2つ以上残っている場合のエラー"""
        self.assertRaisesRegex(
            ValueError, "^演算子が不足しています$", calculate_rpn, "1 2 3 +"
        )

    def test_division_by_zero(self):
        """ゼロ除算エラー"""
        self.assertRaisesRegex(ValueError, "^ゼロ除算エラー$", calculate_rpn, "1 0 /")

    def test_unknown_token(self):
        """定義されていない文字が入力された場合のエラー"""
        self.assertRaisesRegex(
            ValueError, "^不明なトークンエラー: @$", calculate_rpn, "1 2 @ +"
        )
