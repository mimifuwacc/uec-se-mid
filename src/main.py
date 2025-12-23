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

            # 演算を実行
            operations = {
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
                "/": lambda x, y: x / y,
            }

            if token == "/" and b == 0:
                raise ValueError("ゼロ除算エラー")

            result = operations[token](a, b)
            stack.append(result)
        else:
            # 数値として処理する
            try:
                # 整数または小数としてパース
                if "." in token:
                    num = float(token)
                else:
                    num = int(token)
                stack.append(num)
            except ValueError:
                # 数値に変換できない場合は不明なトークン
                raise ValueError(f"不明なトークンエラー: {token}")

    if len(stack) > 1:
        raise ValueError("演算子が不足しています")

    return stack[0]
