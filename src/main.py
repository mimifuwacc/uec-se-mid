"""
逆ポーランド記法 (RPN) 電卓の実装
"""


def _parse_number(token: str) -> int | float:
    """トークンを数値にパースする

    Args:
        token: 数値を表す文字列

    Returns:
        パースされた数値（整数または小数）

    Raises:
        ValueError: 数値に変換できない場合
    """
    if "." in token:
        return float(token)
    return int(token)


def _apply_operator(a: int | float, b: int | float, operator: str) -> int | float:
    """演算子を適用する

    Args:
        a: 1番目のオペランド
        b: 2番目のオペランド
        operator: 演算子（+, -, *, /）

    Returns:
        演算結果

    Raises:
        ValueError: ゼロ除算が発生した場合
    """
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    if operator == "/" and b == 0:
        raise ValueError("ゼロ除算エラー")

    return operations[operator](a, b)


def calculate_rpn(expression: str):
    """
    逆ポーランド記法で表現された数式を計算する

    Args:
        expression: 逆ポーランド記法の数式（スペース区切り）
    Returns:
        result: 計算結果
    Raise:
        ValueError: 各種エラーが発生した場合
    """
    tokens = expression.split()
    stack: list[int | float] = []

    for token in tokens:
        # トークンが演算子かどうかを判定
        if token in {"+", "-", "*", "/"}:
            # 2項演算子には2つのオペランドが必要
            if len(stack) < 2:
                raise ValueError("オペランドが不足しています")
            # スタックからオペランドを取得（後に入ったものが2番目のオペランド）
            b = stack.pop()
            a = stack.pop()

            result = _apply_operator(a, b, token)
            stack.append(result)
        else:
            # 数値として処理する
            try:
                num = _parse_number(token)
                stack.append(num)
            except ValueError:
                # 数値に変換できない場合は不明なトークン
                raise ValueError(f"不明なトークンエラー: {token}")

    if len(stack) > 1:
        raise ValueError("演算子が不足しています")

    return stack[0]
