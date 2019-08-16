#%% [markdown]
## Python を使ったデータ分析
# Python の基礎を学んだので、Python でデータ整理、分析をする際に役立つパッケージを紹介します。
#%% [markdown]
### Numpy
# `numpy` は行列計算用のパッケージです。
#
# 内部は C で実装されており、高速に計算をすることができます。
#
# また、anaconda を使って python をインストールした場合には、 計算に Intel の　Math Kernel Library が使われており、さらに高速に計算をすることができます。
#
# `numpy` は　`np` として 略して import するのが慣習です。

# %%
import numpy as np
#%% [markdown]
#### ndarray
# numpy では `ndarray` オブジェクトが行列です。
#
# `ndarray` を作るには、`array` 関数を用いて、次のようにシークエンス型（リストやタプルなど）を渡します。

#%%
np.array([1, 2, 3])
#%% [markdown]
# 
# リストを 1 つ渡すとベクトル、行列にするにはリストの中にリストを渡します。
#
# 各リストが行に相当されます。
#
# リストをさらに入れ子にすると、より多次元にすることができます。

#%%
np.array([[1, 2, 3], [4, 5, 6]])
#%% [markdown]
# リストの長さを同じにしないと、リストのベクトルが作成されてしまうので注意してください。

#%%
np.array([[1, 2, 3], [4, 5]])
#%% [markdown]
# 各要素を参照するのは、リストと同様の方法ですが、行列の場合、参照できるのは行と列です。
# 
# `[1]` とすると、1 行目が参照されます。`[:,1]` とすると、1 列目が参照されます。
#
# `[1,1]` とすれば、1 行目の 1 列目の要素が参照されます。

#%%
A = np.array([[1, 2, 3], [4, 5, 6]])
A
#%%
A[1]
#%%
A[:, 1]
#%%
A[1, 1]
#%% [markdown]
# n x m の `ndarray` に対し、同じ行列数で要素が bool 型の `ndarray` を渡すと、`True` の要素のみが返ってきます。

#%%
mask = np.array([[True, False, True], [False, False, True]])
A[mask]
#%% [markdown]
# 各要素が条件式を満たすかどうかを確認することが可能です。
#
# この結果を用いて、条件を満たす要素のみを参照することも可能です。
#%%
A > 4
#%%
A[A > 4]
#%% [markdown]
# 複数の条件も設定できます。各条件は `()` で囲み、`&` ならば積集合、`|` ならば和集合になります。

#%%
(A > 4) & (A < 8)
#%%
(A < 3) | (A > 8)
#%% [markdown]
# `array` 以外にも `ndarray` を生成する方法があります。
# 
# 例えば、`arange` は `range` 関数と同じような挙動で ndarray を生成します。

#%%
np.arange(1, 10)
#%% [markdown]
# `ones` は 1 のみの ndarray、`zeros` は 0 のみの ndarray を生成します。

#%%
np.ones((3, 3))
#%%
np.zeros((3, 3))

# %% [markdown]
# `reshape` を使えば、n x m 行列を l x k 行列に変更できます。

#%%
C = np.arange(1, 10)
C
#%%
np.reshape(C,(3, 3))
#%% [markdown]
# 同名のメソッドもあります。

#%%
C.reshape((3, 3))
#%% [markdown]
#### 属性
#%% [markdown]
# `ndarray` の属性には、例えば、配列の行列数を返す `shape` や 要素の型を返す `dtype` などがあります。

#%%
A = np.array([[1, 2, 3], [4, 5, 6]])
A.shape
#%%
A.dtype
#%% [markdown]
# `T` で転置行列を返します。
#%%
A.T
#%% [markdown]
#### 行列計算
# 先述したように、`numpy` では様々な行列計算をすることができます。

#%%
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
#%% [markdown]
# まずは行列の加算です。
#%%
A + B
#%% [markdown]
# `dot` または　`@` で行列の積を計算します。
#%%
A @ B
#%%
np.dot(A, B)
#%% [markdown]
# `*` を使うと、各要素をかけ合わせます。
#%%
A * B
#%% [markdown]
# `linalg` は様々な線形代数の計算をする関数が含まれています。
# 例えば、`inv` は逆行列を計算します。
#%%
C = np.array([[1, 3, 5], [2, 9, 7], [2, 8, 4]])
np.linalg.inv(C)
#%% [markdown]
# ここで実際に、`numpy` の計算が高速だという例をお見せしましょう。
# 
# 10000 個の要素を足し合わせていく作業をループ文と numpy の `sum` を使って試してみます。

#%%
Z = np.ones(10000)
Z.shape

#%% [markdown]
# セルの最初に `%%timeit` を使うことによって、そのセルの計算速度を測定できます。 

#%%
%%timeit
sum_Z = 0
for i in range(10000):
    sum_Z += Z[i]

#%%
%%timeit 
np.sum(Z)
#%% [markdown]
# 桁が違うほどの差でした。大規模な計算をするときは、できるだけ `numpy` を使うのを勧めます。
#%% [markdown]
#### ブロードキャスト
# `ndarray` には、ブロードキャストという機能がついています。
#
# これによって、配列の行列数が違う場合にも計算を可能にします。
# 
# 実際に見てみましょう。行列の加算は配列の数が同じもの同士に定義されますが、X と Y は配列数が違います。
#
# この 2 つを足してみます。

#%%
X = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
Y = np.array([[1, 2, 3]])
X + Y
#%% [markdown]
# この結果は次の計算によるものであることは明らかですね。

#%%
Y_wide = np.array([[1, 2, 3],[1 ,2, 3],[1, 2, 3]])
X + Y_wide
#%% [markdown]
# ブロードキャストというのは、つまり、行列同士を計算できるように、配列数が足りない行列を引き伸ばしてくれるということです。
# 
# 例えば、ある数字を全ての要素に足したい場合、行列数を同じにしないでもすむというメリットがあります。

#%% [markdown]
#### 乱数生成
# Python にも `random` という疑似乱数を生成するモジュールがありますが、numpy の `random` はより高機能です。
# 
# 計量経済学をするなら気になるところですね。
# 
# さっそく見ていきましょう。
#
# `rand` は一様分布から疑似乱数を生成します。引数に配列数を渡します。

#%%
np.random.rand(3, 3)
#%% [markdown]
# `randn` は標準正規分布からの疑似乱数を発生させます。
#%%
np.random.randn(3, 3)
#%% [markdown]
# `choice` は引数に渡した 1 次元の ndarray もしくはリストからランダムに要素を抽出します。
#%%
countries = ['Japan', 'China', 'Korea']
np.random.choice(countries)
#%% [markdown]
# 引数には要素を抽出する回数、復元抽出か非復元抽出か、各要素を抽出する確率を渡せます。

#%%
np.random.choice(countries, size = 2)
#%%
np.random.choice(countries, size = 2, replace = False)
#%%
np.random.choice(countries, size = 2, p = [0.9, 0.05, 0.05])
#%% [markdown]
# 一様分布や標準正規分布といったおなじみのもの以外にも、ベータ関数やラプラス分布、ロジスティック分布などから疑似乱数を生成することもできます。
# 
# 次の例は、自由度 5 の$\chi^2$分布から疑似乱数を生成しています。 

#%%
np.random.chisquare(5, 3)
#%% [markdown]
### Scipy
#%% [markdown]
# `scipy` を語るにはスペースが足りないほど、`scipy` は統計、機械学習、画像処理など様々な科学計算用の関数を備えています。
#
# ネーミングセンスからお分かりのように、`scipy` は `numpy` と併用して用います。
# 
# せっかくなので、いくつか見ていきましょう。
#%% [markdown]
#### optimize
# 
# `scipy` はそ機能の大きさのため、各機能毎に import することが勧められています。
# 
# `optimize` は最適化に関する関数を備えています。
#
# `brentq` は方程式の解を見つけ出します。

#%%
from scipy import optimize as opt
def func1(x):
    fx = 3 * x - 5
    return fx

opt.brentq(func1, -10, 10)
#%% [markdown]
# `minimize` は関数の最小値を探す関数です。オプションによって、様々な探索アルゴリズムを選択できます。

#%%
def func2(x):
    fx = x ** 2 + 3 * x - 5
    return fx

opt.minimize(func2, 0)
#%% [markdown]
#### stats
# 
# `stats` は統計分析に関する関数を備えています。
# 
# 例えば、`numpy` のように疑似乱数を生成することも可能です。
#
# `norms.rvs` とすると、正規分布の疑似乱数を生成します。

#%%
from scipy import stats
stats.norm.rvs(loc = 0, scale = 1, size = 10)
#%% [markdown]
# `rvs` は疑似乱数の生成ですが、他にも豊富なメソッドがあります。
# 
# 例えば、
# 
# 1. `pdf` : 確率密度関数の値を返す 
# 2. `cdf` : 累積密度関数の値を返す
# 3. `ppf` : パーセント点の値を返す

#%%
stats.norm.pdf(x = 0, loc = 0, scale = 1)
#%%
stats.norm.cdf(x = 0, loc = 0, scale = 1)
#%%
stats.norm.ppf(q = 0.05, loc = 0, scale = 1)
#%% [markdown]
# 検定もすることも可能です。
#
# 例えば、`ttest_ind` は 2 つのデータ (`ndarray`) の差を t 検定します。

#%%
N_A = stats.norm.rvs(loc = -5, scale = 1, size = 10)
N_B = stats.norm.rvs(loc = 3, scale = 1, size = 10)
stats.ttest_ind(N_A,N_B)
#%% [markdown]
### Pandas
# 
# `pandas` は 様々な I/O (入出力) 処理、高機能なデータ処理をすることができるパッケージです。
#
# `pandas` のデータ型は、`Series` と `DataFrame` です。
#
# `Series` はラベル付きのベクトル、`DataFrame` はラベル付きの行列です。
# 
# R を使ったことがある人はピンとくるかもしれませんが、`DataFrame` は R の data.frame 型と同じようなものです。 
#
# 実際、pandas は R のデータ整理用のパッケージ、`dplyr` でできることの多くを実装しています。
# 
# `pandas` は `pd` と略して import するのが慣習です。
# 
# それでは、`Series` から見ていきましょう。

#%%
import pandas as pd
#%% [markdown]
#### Series
# 
# Series の作り方は、numpy の１次元の `ndarray` と同じようなものです。

#%%
pd.Series([1, 2, 3])
#%% [markdown]
# `ndarray` とは似ていますが、異なるところもあります。
# 
# まず、左側に index が表示されていますね。
#
# この index は好きなようにラベルを付けることも可能です。

#%%
pd.Series([1, 2, 3], index = ['one', 'two', 'three'])
#%% [markdown]
# Series に名前を付けることも可能です。

#%%
pd.Series([1, 2, 3], index = ['one', 'two', 'three'], name = 'numbers')
#%% [markdown]
# index、要素、名前などが属性として参照できます。

#%%
A_s = pd.Series([1, 2, 3], index = ['one', 'two', 'three'], name = 'numbers')
#%%
A_s.index
#%%
A_s.values
#%%
A_s.name
#%% [markdown]
# 要素を参照すると、`ndarray` が返ってきました。
# 
# `pandas` と `numpy` との間は簡単に行き来することができます。
# 
# 今度は `ndarray` を `Series` にしてみます。

#%%
A_np = np.array([1, 2, 3])
A_index = np.array(['one', 'two', 'three'])
pd.Series(A_np, index = A_index)
#%% [markdown]
# 後で見ますが、`DataFrame` でも同じことができます。
# 
# 実際にデータ分析をする際には、まず `pandas` を使ってデータを整理し、`numpy` や `scipy` を使って分析を行うという流れになると思います。
#%% [markdown]
##### 要素の参照
# `Series` は様々な方法で要素を参照することができます。
# 
# まず、要素の番号を入れて参照してみましょう。

#%%
A_s
#%%
A_s[1]
#%% [markdown]
# index 名で要素を参照することも可能です。

#%%
A_s['three']
#%% [markdown]
# 参照した要素に違う値を代入してみます。

#%%
A_s['three'] = 5
A_s
#%% [markdown]
# `numpy` のところで説明したように、各要素が条件式を満たしているかを判別できます。
#
# また、この結果を用いて条件式を満たす要素を参照できます。

#%%
A_s > 2
#%%
A_s[A_s > 2]
#%% [markdown]
##### 計算
# `Series` の計算は `numpy` の時と違います。
# 
# `Series` では四則演算は index が同じもの同士で行います。

#%%
A_s = pd.Series([1, 2, 3], index = ['one', 'two', 'three'])
B_s = pd.Series([4, 5, 6], index = ['one', 'two', 'three'])
B_s
#%%
A_s + B_s 
#%%
A_s - B_s
#%%
A_s * B_s
#%%
A_s / B_s
#%% [markdown]
# index が同じもの同士で計算するので、商も定義されます。
# 
# index が合致しないものは NaN (Not a number) が返ってきます。

#%%
C_s = pd.Series([1, 2, 3], index = ['one', 'two', 'four'])
C_s
#%%
A_s + C_s
#%% [markdown]
##### 文字列操作
# 
# Series には `str` という強力な文字列操作のメソッドが備わっています。
#
# これを用いることによって、データのクリーニングが非常に楽になります。
#
# まずは、基本的な操作からしていきましょう。
# 
# `lower` は文字列を小文字に、`upper` は文字列を大文字に、`len` は文字列の文字数をカウントします。

#%%
small_text = pd.Series(['A', 'B', 'C'])
small_text.str.lower()
#%%
large_text = pd.Series(['a', 'b', 'c'])
large_text.str.upper()
#%%
number_text = pd.Series(['one', 'two', 'three'])
number_text.str.len()
#%% [markdown]
# `extract` は指定した文字を抜き出します。

#%%
number_with_text = pd.Series(['one1', 'two2', 'three3'])
number_with_text.str.extract(r'(\d)', expand = False)
#%% [markdown]
# `\d` は **正規表現** というもので、パターンマッチングをする際に強力な助けとなります。
#
# 正規表現はマッチングしたい文字列の条件式を非常に簡単に書くことができます。
#
# いくつかの文字はメタキャラクタというもので、例えば `\d` は任意の数とマッチングするという意味です。
# 
# さきほどの文は、文頭から文字を参照していき、任意の数が当たったらその文字を抜き出す ということをしています。
#
# マッチングの文に正規表現を使う場合は最初に `r` を付けておきましょう。
#
# 先程とは逆に、任意の数字以外の文字列を抜き出す場合次のようにします。
# 
# `\D` は数以外の任意の文字とマッチングします。
# 
# `+` は直前のマッチング式が一致していたら、それを繰り返します。
#
# 例えば、`two+` は `two` も `twoooooooo` とも一致しますが、`tw` とは一致しません。

#%%
number_with_text.str.extract(r'(\D+)', expand = False)
#%% [markdown]
# `replace` はマッチした文字列を指定した文字列に置き換えます。

#%%
number_with_text.str.replace(r'(\d)', '')
#%% [markdown]
# `match` はマッチング文と正確にマッチしているか、`contains` はマッチング文を含んでいるかを返します。

#%%
match_text = pd.Series(['1', 'one2', 'one'])
match_text
#%%
match_text.str.match(r'\d')
#%%
match_text.str.contains(r'\d')
#%% [markdown]
# `get_dummies` はダミー変数を作成できます。
# `DataFrame` を返します。

#%%
dummies_text = pd.Series(['one', 'one', 'two'])
dummies_text.str.get_dummies()
#%% [markdown]
# `sep` で文字列を分けられます。

#%%
dummies_text = pd.Series(['one|two', 'one', 'two'])
dummies_text.str.get_dummies(sep = '|')
#%% [markdown]
#### DataFrame
# `DataFrame` は 多次元の `ndarray` を作るときと似ています。

#%%
pd.DataFrame([[1, 2, 3], [4, 5, 6]])
#%% [markdown]
# `Series` と同じように左に index がありますが、さらに上に columns があります。
#
# これらはどちらもラベル付けすることができます。

#%%
index_list = ['one', 'two']
columns_list = ['a', 'b', 'c']
pd.DataFrame(
    [[1, 2, 3], [4, 5, 6]], 
    index = index_list, 
    columns = columns_list)
#%% [markdown]
# `Series` のように index、columns、要素が属性として用意されています。

#%%
A_dt = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6]], 
    index = index_list, 
    columns = columns_list)
#%%
A_dt.index
#%%
A_dt.columns
#%%
A_dt.values
#%% [markdown]
# `Series` と同じように、要素を参照すると `ndarray` が返ってきます。
#
# また、`Series` と同じように `ndarray` を `DataFrame` にすることもできます。
#%% [markdown]
##### 要素の参照
# `DataFrame` にも様々な要素の参照の方法があります。

#%%
A_dt
#%% [markdown]
# columns の参照は `[]` か、`.columns名` で行います。

#%%
A_dt['a']
#%%
A_dt.b
#%% [markdown]
# 複数の columns の参照はリストを使います。

#%%
A_dt[['a', 'c']]
#%% [markdown]
# index の参照は `loc` を使います。
#
# `loc[index名, columns名]` とします。

#%%
A_dt.loc['one']
#%%
A_dt.loc[:, 'c']
#%%
A_dt.loc['one', 'b']
#%% [markdown]
# `iloc` はラベル名ではなく要素の番号によって参照します。
#%%
A_dt.iloc[1]
#%%
A_dt.iloc[:, 2]
#%%
A_dt.iloc[1, 1]
#%% [markdown]
# 要素を参照して値を再代入することもできます。

#%%
A_dt.loc['one', 'b'] = 5
A_dt
#%% [markdown]
# 条件式を満たしているかを判別することもでき、条件式を満足する行を参照することもできます。

#%%
A_dt > 2
#%%
A_dt[A_dt > 2]
#%% [markdown]
# ある columns が条件式を満たしている 行を参照することもできます。

#%%
A_dt.a > 2
#%%
A_dt[A_dt.a > 2]
#%% [markdown]
# 反対に、ある index が条件式を満たしている columns を参照することもできます。

#%%
A_dt.loc['one'] > 2
#%%
A_dt.loc[:, A_dt.loc['one'] > 2]
#%% [markdown]
##### I/O （入出力）処理
# 
# `pandas` は多様な I/O 処理をすることができ、
#
# csv ファイル、エクセルファイル、Stata ファイル、R ファイルなどの様々なファイルを入出力することが可能です。
# 
# 例えば、次の例はエクセルのファイルを読み込んでいます。

#%%
pd.read_excel('data/excel_example.xlsx')
#%% [markdown]
# 次の例は `DataFrame` を Stata ファイルに出力しています。

#%%
A_dt.to_stata('data/stata_output.dta')
#%% [markdown]
##### グループ化
#%% [markdown]
# `pandas` の `DataFrame` には様々なデータ集計の関数が用意されています。
# 
# 例えば、`groupby` は指定した columns の値でグループを作ります。

#%%
B_dt = pd.DataFrame(
    [['one', 1], ['one', 2], ['two', 3], ['two', 4]], 
    columns = ['num', 'val'])
B_dt
#%%
group_dt = B_dt.groupby('num')
group_dt
#%% [markdown]
# グループ化した `DataFrame`, `DataFrameGroupBy` に集計関数を与えることで集計値を獲得できます。
#
# 例えば、`mean` メソッドは平均値、 `std` メソッドは標準偏差が返されます。

#%%
group_dt.mean()
#%%
group_dt.std()
#%% [markdown]
##### データの結合
# `pandas` には便利なデータの結合の関数が用意されています。
# 
# `concat` は単純に `DataFrame` 同士を結合します。

#%%
A_dt
#%%
index_list = ['one', 'two']
columns_list = ['a', 'b', 'c']
C_dt = pd.DataFrame(
    [[4, 5, 6], [7, 8, 9]],
    index = index_list,
    columns = columns_list)
C_dt
#%%
pd.concat([A_dt, C_dt])
#%% [markdown]
# `axis = 1` にすることで、横方向の結合をすることができます。

#%%
pd.concat([A_dt, C_dt], axis = 1)
#%% [markdown]
# `append` も同様です。

#%%
A_dt.append(C_dt)
#%% [markdown]
# `merge` はキーを指定して、キーが同じもの同士で index を結合します。

#%%
B_dt
#%%
D_dt = pd.DataFrame(
    [['one', 1], ['two', 2], ['three', 3], ['four', 4]], 
    columns = ['num', 'val'])
D_dt
#%%
pd.merge(B_dt, D_dt, on = ['num'])