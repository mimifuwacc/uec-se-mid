"""
逆ポーランド記法 (RPN) 電卓の実装
"""


def calculate_rpn(expression: str):
    """
    逆ポーランド記法で表現された数式を計算する

    Args:
        expression: 逆ポーランド記法の数式（スペース区切り）
    Returns:
        result: 計算結果
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

            # 演算を実行
            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = a / b

            stack.append(result)
        else:
            # 数値として処理する
            # 整数または小数としてパース
            if "." in token:
                num = float(token)
            else:
                num = int(token)
            stack.append(num)

    if len(stack) > 1:
        raise ValueError("演算子が不足しています")

    return stack[0]
