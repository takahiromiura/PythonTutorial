# %% [markdown]
## Web スクレイピング入門
# %% [markdown]
# Python の使い方も学び、Web ページの構造も理解したので、早速 Web スクレイピングをしていきましょう。
# まず、このページでは手始めに [Yahoo news のトピックス一覧](https://news.yahoo.co.jp/topics) から、各記事のタイトルを収集することを目指します。
# %% [markdown]
### requests
# %% [markdown]
# まず、python を使って、Web ページのコンテンツをとってみましょう。
# これには、 `requests` というモジュールを使います。
# Python にも似たようなものがありますが、 `requests` の方が使いやすいです。
# コンテンツが欲しい Web ページの URL について、 `requests.get(URL)` とすると、Web サーバーに Web ページのコンテンツを送ってくれという要求をすることができます。

# %%
import pandas as pd
from bs4 import BeautifulSoup
import requests
url = "https://news.yahoo.co.jp/topics"
response = requests.get(url)
response.status_code
# %% [markdown]
# 最後の行は、ステータスコードというものを表していてます。
# ステータスコードは Web サーバーへの要求が上手くいったかを判別することができるので、毎回チェックしておきましょう。
# 200 は、Web サーバーの要求が無事成功したことを示しています。
# ステータスコードは 200 以外にも、様々な値を返すので、やりながら学んでいけば良いでしょう。
# %% [markdown]
### BeautifulSoup
# %% [markdown]
# 次に、Web ページのコンテンツからデータを取りやすいようにします。
# ここでは、`BeautifulSoup` を用います。
# `BeautifulSoup` は使い方がわかりやすいので、入門としては良いでしょう。

# %%
bs = BeautifulSoup(response.content, "lxml")
# %% [markdown]
# `lxml` というのは、htmlのパーサーの一つです。
# パーサーというのは、HTML を解析して分析しやすくしてくれます。
# また、タグの閉じ忘れなどを直してくれます。
# `BeautifulSoup` には 4 つほどのパーサーを使えますが、`lxml` は使いやすさと早さを兼ね備えているので、これを使います。
#
#  HTML の章で解説しましたが、Web ページは様々な要素が入れ子になっています。
# したがって、自分の欲しい情報をとるには、その情報が置いてある要素を上手く指定することが大事です。
# 要素を指定する方法は、CSS のところで解説しました。
# それでは、我々の欲しい情報は一体どこに位置しているのでしょうか？
#
# 実は、Google Chrome や　Firefox などのモダンブラウザには、それを分かりやすくする機能が備わっています。
# Web ページを開いて、`Ctrl + Shift + I` を押すか、右クリックを押してから、検証（インスペクタ）を押してみましょう。
# 画面が 2 分割され、左側に Web ページ、右側に html が表示されるでしょう。
# 右側の左上のカーソルのマークをクリックしてから、左側の適当なところを押してみましょう。
# すると、そのテキストが html 内のどこにあるかが、右側に表示されます。
#
# この機能を使って、欲しい情報はどこにあるのかを探っていきます。
# ここでは、トピックス一覧の内容が欲しいので、その内のどれかを押してみましょう。
# 一覧の内容は全てリンクが張られているので、 `a` 要素に含まれていることがわかりました。
# %% [markdown]
# ![a](../image/inspect_a.png)
# %% [markdown]
# `BeautifulSoup` は `select` で CSS セレクターを使うことができます。
# 下の例では `a` 要素を取ってきています。
# `select` は CSS セレクターで指定した要素をタグごとにリストに含めます。
# %%
print(len(bs.select('a')))
# %% [markdown]
# 返ってくる要素が多すぎます。
# Web ページは多くのところでリンクを貼っているので、`a` 要素だと制限が緩すぎます。

# 別の方法を考えましょう。
# 各トピックの全体を検証してみると、トピック毎に `div` 要素でくくられていることがわかります。
# それでは、`div` 要素を指定してみましょう。
# %% [markdown]
# ![ul](../image/inspect_div.png)
# %%
# 表示は省略
# bs.select('div')
# %% [markdown]
# 先程よりはましですが、まだ余計なものが残っています。
# よく見ると、この `div` 要素には `topicsList` というクラス名が割り当てられています。
# `.topicsList` として、このクラスを持つ要素を取ってみましょう。
# %%
topics = bs.select('.topicsList')
topics[0]
# %% [markdown]
# 上手くいきました！各トピックがリストの各要素に入ってます。
# それでは、ここからトピック毎に記事名を格納していきましょう。

# `topicsList_title` クラスには、トピックのカテゴリーが入ってます。
# 各 `li` 要素（あるいは、`topicsListItem` クラス）には、各記事が入っています。
# 要素ごとに分けたら、`text` メソッドを使って、要素の内容を取り出します。
# %%
print(topics[0].select('.topicsList_title')[0].text)
print(topics[0].select('li')[0].text)
# %% [markdown]
# この作業をループ化して、`dict = {トピックのタイトル:[記事A, 記事B]}` というように、辞書型にしていきます。
# %%
news_topics = {}
for topic in topics:
      topic_title = topic.select('.topicsList_title')[0].text
      news_topics[topic_title] = []
      for news in topic.select('li'):
              news_topics[topic_title].append(news.text)

# %%
news_topics['国内']
# %% [markdown]
#
# ちなみに、さきほどの処理は次のようにもかけます。
# `[news.text for news in topic.select('li')]` はリスト内包表記というものです。
# ここでは、`li` 要素を順に `news` に格納し、その要素の内容を `news.text` で取り出し、リストに入れていく処理をしています。
# リスト内包表記は、普通にループ文を書くよりもスッキリとして書け、また早く処理することができます。

# %%
# news_topics = {}
# for topic in topics:
#     topic_title = topic.select('.topicsList_title')[0].text
#     news_topics[topic_title] = [news.text for news in topic.select('li')]
# %% [markdown]
# せっかくなので、`pandas` の `DataFrame` に変換しましょう。
# `dict` から `DataFrame` にするには、`from_dict` を使います。

# %%
topics_dt = pd.DataFrame.from_dict(news_topics)
topics_dt