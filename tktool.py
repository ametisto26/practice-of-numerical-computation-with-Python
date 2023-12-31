# -*- coding: utf-8 -*-
"""
私的関数
"""
import numpy as np  # NumPy


# 相対誤差のための関数定義
def relerr(approx, true_val):
    # 絶対誤差の計算
    relerr = np.abs(approx - true_val)

    if isinstance(approx, (list, np.ndarray)):
        if true_val.any() == 0.0:  # 0の有無
            nonzero_abs_true_val = []
            for val in true_val:
                if val == 0.0:
                    nonzero_abs_true_val.append(1.0)
                else:
                    nonzero_abs_true_val.append(np.abs(val))
        else:
            nonzero_abs_true_val = np.abs(true_val)

        # 相対誤差の計算
        relerr /= nonzero_abs_true_val

    else:  # 単一変数の場合
        if true_val != 0.0:
            relerr /= np.abs(true_val)

    return relerr
