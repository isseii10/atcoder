#2次元累積和
def accumulate2(h, w, target):
    """
    :param h: h行
    :param w: w列
    :param target: h*wのリスト(累積和したいリスト）
    :return: 累積和したリスト
    """
    s_2 = [[0] * (w + 1) for _ in range(h + 1)]
    for i in range(w):
        for j in range(h):
            s_2[i + 1][j + 1] = s_2[i][j + 1] + s_2[i + 1][j] - s_2[i][j] + target[i][j]
    return s_2
