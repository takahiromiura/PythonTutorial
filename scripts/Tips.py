#%% [markdown]
## Tips

#%%
import numpy as np
#%% [markdown]
### f-string
#　`string` 以外の変数の値を文字列に組み込みたい場合、f-string 記法というのがあります。
# これは、Python3.6 以上ではないと使えないのに注意してください。
# まずは、何も使わない場合。
# %%
a = 0
b = 2
# %%
'a の値は ' + str(a)
# %%
'a の値は ' + str(a) + ': a - b の値は ' + str(a - b)
# %% [markdown]
# 変数が一つの場合はまだ楽ですが、二つ、三つとなると面倒です。
# 実は、`format` メソッドというものがあり、これを使うことで、文字列に後から変数を代入できます。
# `format` メソッドは Python3.6 より前でも使えます。
# 変数を代入したい場所に `{}` をつけます。
# %%
'a の値は {}: a - b の値は {}'.format(a, a - b)
#%% [markdown]
# `format` はキーワード引数も使えます。
# こちらのほうが可読性が良いです。
# %%
'a の値は {a}: a - b の値は {a_b}'.format(a = a, a_b = a - b)
# %% [markdown]
# f-string 記法はキーワード引数を使った`format` メソッドに似てますが、`format` メソッドを付ける必要がありません。
# 代わりに、`f` を文字列の前につけます (`F` でも可）。
# %%
f'a の値は {a}: a - b の値は {a - b}'
# %% [markdown]
# `{}` の中の変数はすでに定義されている必要があるのに注意してください。
# 下はエラーになります。
# %%
# f'c の値は {c}'
# %% [markdown]
# f-string および `format` はただ変数を代入するだけでなく、より柔軟に文字列の代入をすることができます。
# 例えば、ゼロ埋め（zero padding）や桁区切りなどが可能です。
# `{}` に代入したい変数名の後に `:` を入れ、その後に書式を指定します。
# %%
i = 1234
print(f'zero padding: {i: 06}')
print(f'with conmma :  {i:,}')
#%% [markdown]
### Python の bool 型と Numpy の bool 型の違い
# Python と Numpy にはどちらも bool 型がありますが、若干の違いがあります。
# 論理和などの挙動が一部異なるので、注意してください。

#%% [markdown]
#### Python の bool 型
# Python での `bool` 型、`True`, `False` は `int` クラスのサブクラスです。
# つまり、True は 1, False は 0 と解釈される場合があります。
# 実際に見てみましょう。
# ビット単位演算子 `|` は論理和、`&` は論理積を返します。
#%%
print(f'True & True   : {True & True}')
print(f'True | True   : {True | True}')
print(f'True & False  : {True & False}')
print(f'True | False  : {True | False}')
print(f'False & False : {False & False}')
print(f'False | False : {False | False}')
#%% [markdown]
# 一方で、和 `+` と差 `-` も定義されていますが、この場合は数値として計算されます。
# %%
print(f'True + True   : {True + True}')
print(f'True - True   : {True - True}')
print(f'True + False  : {True + False}')
print(f'True - False  : {True - False}')
print(f'False + False : {False + False}')
print(f'False - False : {False - False}')
#%% [markdown]
#### Numpy での　bool 型
# Numpy での `bool` 型は `int` 型のサブクラスではありません。
# 論理和 `|`、論理積 `&` は Python の `bool` 型と同じです。
# ブール演算子 `and`, `or` も Python の `bool` 型と同じになります。
# %%
true = np.array([True])
false = np.array([False])
# %%
print(f'True & True   : {true & true}')
print(f'True | True   : {true | true}')
print(f'True & False  : {true & false}')
print(f'True | False  : {true | false}')
print(f'False & False : {false & false}')
print(f'False | False : {false | false}')
# %% [markdown]
#　一方で、和 `+` は論理和と同じであり、差 `-` は定義されません。
#%%
print(f'True + True   : {true + true}')
# print(f'True - True   : {true - true}')
print(f'True + False  : {true + false}')
# print(f'True - False  : {true - false}')
print(f'False + False : {false + false}')
# print(f'False - False : {false - false}')
#%% [markdown]
# ただし、どちらの `bool` 型も 数値型（`int`や`float`など）と足し引きができます。
# %%
print(f'True + 1: {True + 1}')
print(f'True - 1: {True - 1}')
print(f'np.array([True]) + 1: {np.array([True]) + 1}')
print(f'np.array([True]) - 1: {np.array([True]) - 1}')
#%%　[markdown]
# したがって、どちらも `sum` を使えば、`True` の数をカウントすることができます。
# これは、`sum` 関数が default で `0` を最初に足しているからです。
# なお、`numpy` の `sum` メソッドも同じです。
# %%
a = [True, False, True, True]
b = np.array([True, True, False, False])
print(sum(a))
print(sum(b))
print(b.sum())
#%% [markdown]
### 三項演算子
# `if ~ else` はインデント・ブロックが必要なため、どうしてもコードが長くなってしまいます。
# 三項演算子を使えば、１行で書くことができます。
# 次のように書きます。
# `変数 = 真の場合の値 if 条件式 else 偽の場合の値`
#%%
b = 5 if 3 == 3 else 9 # True
# 下のコードは上と同じ
# if 3 == 3:
#     b = 5
# else:
#     b = 9
b
#%% [markdown]
# 長い文の場合は可読性が悪くなるので、使い所に注意してください。
#%% [markdown]
### 内包表記
# リスト、辞書などに逐次的に要素を足していく場合には、`for` ループも１行で書くことができます。
# これをリスト内包表記、辞書内包表記と言います。
# リスト内包表記は次のように書きます。
#%%
c = [i for i in range(5)]
# 下と同じ
# c = []
# for i in range(5):
#     c.append(i)
c
# %% [markdown]
# 辞書内包表記は次のように書きます。
# %%
d = {i: i for i in range(5)}
d
# %% [markdown]
# `if` を用いて、条件式が真の場合のみ要素を足していくことや、三項演算子を入れることもできます。
# `if` の場合と `if ~ else` がある場合で少し書き方が違うので注意してください。
# %%
k = [i for i in range(5) if i % 2 == 0]
# 下と同じ
# k = []
# for i in range(5):
#   if i % 2 == 0:
#       k.append(i)
k
#%%
j = [i if i % 2 == 0 else 0 for i in range(5)]
# 下と同じ
# j = []
# for i in range(5):
#   if i % 2 == 0:
#       j.append(i)
#   else:
#       j.append(0)
j
#%% [markdown]
# 三項演算子と同じように、長い文の場合は逆に読みにくくなるので注意してください。
# また、内包表記を使うと、`append` を使うよりも非常に高速に処理を行うことができます。
# 多くのループ作業が必要な場合は、内包表記か `numpy` を使うことを考えましょう。
# ちなみに、タプル内包表記というのはなく、`()` の内包表記はジェネレーター内包表記というものになります。

# %%
(i for i in range(5))
