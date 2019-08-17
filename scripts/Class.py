
# %% [markdown]
## Python Class
#%% [markdown]
### クラス
#%% [markdown]
# 分析が複雑になると、多くの関数を書く必要がでてきます。
# 
# ただし、多くの関数を書くと、様々な問題が出てきます。
#
# 長い関数を書くと、変更に弱くなります。
#
# また、途中の計算結果のみを取得したい場合は、その後の無駄な計算をしてしまいます。
#
# 一方で、短い関数に分けて作ると、管理が難しくなります。
#
# 例えば、ある関数はデータ A に関する操作、ある関数はデータ B に関する操作だった場合、どちらのデータの関数かを覚えておかないといけません。
# 
# クラスを使えば、関数や変数をひとまとめにすることができ、そういった問題を解決することができます。

#%% [markdown]
# クラスは、`class` によって定義します。

#%%
class First:
    
    pass

#%% [markdown]
#
# まず `First` というクラスを定義しました。
#
# 関数と同じように、クラスの内容をインデント・ブロック内に書いていきます。
#
# `pass` は何もしないという意味です。
# 
# 何も書かないとエラーになるので、`pass` を書いています。
#
# 次のようにクラスを呼び出してみます。

#%%
First
# %%
First()
# %% [markdown]
#### インスタンス
# 上の　`First` と `First()` はどういった違いがあるのかはわかりませんが、大きな違いがあります。
#
# `First` はクラスを呼び出します。
#
# `First()` はクラスのインスタンスを返します。
#
# 例えるならば、クラス自体は設計図のようなものです。
# 
# インスタンスは、その設計図をもとに作られた建造物のようなものです。
#
# なぜ、この違いが重要なのかは後ほど説明します。

#%% [markdown]
#### 属性
#%% [markdown]
# さきほどのクラスは、特に変数も関数も持っていないので、変数を付与しましょう。
# 
# 次のように、インデント・ブロック内に変数を定義します。

#%%
class Second:
    
    a = 100 #クラス属性
    
#%% [markdown]
# クラスの中で `a` という変数を定義しました。クラスが持つ変数を **属性** と呼びます。
#
# また、属性にはクラス属性とインスタンス属性があります。
# 
# インデント・ブロック内で定義した変数はクラス属性です。
# 
# インスタンス属性の作り方は後ほど説明します。
#
# 属性を参照するには、`クラス名.属性名` とします。

#%%
Second.a
#%% [markdown]
#### メソッド
# 
# 今度は、関数を持たせましょう。

#%%
class Third:

    def print_3(self):
        print(3)

#%% [markdown]
# クラスが持つ関数を **メソッド** と呼びます。メソッドの呼び出しは `クラス名.メソッド名` とします。

#%%
Third().print_3()
#%% [markdown]
# メソッドで注意しなければならないのは、メソッドでは自動的に第 1 引数としてインスタンス自身が代入されます。
# 
# Python では慣例的にこれを `self` としてます。
# 
# メソッドはクラスではなく、インスタンスでなければ使えないことに注意してください。
#
# インスタンスを作ると、`self` が使えるようになります。
#
# 実際に、下のコードはエラーになります。
#%%
# Third.print_3()
#%% [markdown] 
# クラスの中のメソッドで違うメソッドを呼び出す場合、また属性を呼び出す場合は、`self.メソッド名`、`self.属性名` とすればできます。
#
# こうすることによって、用途ごとに関数や変数をまとめ、内部で使い回すことができます。
#%%
class Fourth:
    
    a = 100
    
    def print_a(self):
        print(self.a) # 属性 a を出力
        
    def call_print(self):
        self.print_a() # print_a メソッドの呼び出し

# %%
Fourth().print_a()
Fourth().call_print()
#%% [markdown]
#### コンストラクタ
# 実は、インスタンスを作る際に、コンストラクタというメソッドが呼び出されます。
#
# Python では、`__init__` というのがそれで、init の前にアンダースコアを２つ前後に配置します。
#
# これらを特殊メソッドと呼び、クラスの振る舞いを変えることができます。
#
# コンストラクタに追加の引数を定義することによって、元の設計図に変化をつけたインスタンスを作れます。
#
# 例えば、アンケートのデータ整理を行う、`Survey` というクラスを作ったとしましょう。
# 
# アンケートのデータ整理で行う操作はすべて共通ですが、いくつかの属性は異なるべきです（例えば、アンケートの実施年など）。
#
# 例えば、次のようにすれば、インスタンス属性を作ることができます。

#%%
class Survey:

    some_attribute = 0
    a = 3

    def __init__(self, year):
        this_year = year
        self.year = year

    def print_a(self):
        print(self.a)

    def some_method(self):
        pass

#%%
survey2018 = Survey(year = 2018)
survey2019 = Survey(year = 2019)
print(survey2018.year)
print(survey2019.year)
#%% [markdown]
# クラス属性では、変数を定義すればクラス属性になりましたが、インスタンス属性は `self.属性名` としないとインスタンス属性になりません。
# 
# 普通に変数を作成すると、ローカル変数になります。 
#
# 実際、`__init__` メソッドで `this_year` という変数を定義していますが、メソッド外からは参照できません。

#%%
# survey2019.this_year

#%% [markdown]
#### 継承
#%% [markdown]
# ほとんど年のアンケートではデータ整理の操作は同じですが、ある年だけ異なる操作と属性が必要だったとしましょう。
# 
# **継承** を使うことによって、属性とメソッドを引き継いで、新たにクラスを定義することができます。
# 
# クラスの定義の際に、`クラス名（継承クラス名）` とすることによって、継承を行うことができます。

#%%
class SurveyExtra(Survey):
    
    b = 50 # 追加クラス属性
    
    def __init__(self, year, c):
        super().__init__(year) # Survey のコントラクタ
        self.c = c # 追加インスタンス属性
        
    def print_b(self): # 追加メソッド
        print(self.b)

#%% [markdown]
# 新たに定義した `SurveyExtra` は、継承した `Survey` の属性とメソッドを持っています。まずはそれを確認してみます。

#%%
Survey2009 = SurveyExtra(year = 2009, c = 10)
print(Survey2009.a)
Survey2009.print_a()
#%% [markdown]
# `SurveyExtra` で定義した属性とメソッドを呼び出します。

#%%
print(Survey2009.b)
Survey2009.print_b()
#%% [markdown]
# 継承したクラスと同じ名前のメソッドを定義すると、継承したクラスのメソッドは上書きされますが、`super()` を使えば継承したクラスを呼び出すことができます。
# 
# これによって、例えば `Survey` のインスタンス属性に新たにインスタンス属性を追加できます。
#
# `SurveyExtra` のコントラクタを詳しく解説すると、
# 1. まず引数に `Survey` のコントラクタで必要だった `year` と、新たに `b` という引数を追加しています。
# 2. `super().__init__(year)` によって、`Survey` のコントラクタを実行しています。これによってインスタンス属性 `year` が付与されました。
# 3. 最後に、 `self.c = c` で新たなインスタンス属性を付与しました。