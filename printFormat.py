# -*- coding: utf-8 -*-
"""
型指定出力
"""
a = 102.12345678


#書式設定
print(f"a = {a:25.17e}")
print(f'a = {a:+15.3f}')
print(f'a = {a:25.17g}')


#format 関数
print('a = {:25.17e}'.format(a))

