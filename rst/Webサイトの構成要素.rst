===========================
Web サイトの構成要素
==========================


HTML
=======================
HTML (HyperText Markup Language) は名前こそとっつきづらいですが、知ってしまえばそこまで難しいものではありません。
HTML は IE, Firefox, GoogleChrome など、ブラウザ上に文書を表示するためのマークアップ言語です。
そもそも、マークアップ言語とはなんでしょう。

.. code-block:: html

  例えば、HTMLでは <b>太字</b> の表示はこのように書きます。

この文を html として保存して、ブラウザで表示すると、次のように表示されるはずです。

.. raw:: html

  例えば、HTMLでは <b>太字</b> の表示はこのように書きます。
  <p></p>


``<b>`` に囲まれている文字が太字になりました。
``<b>`` を **タグ** といいます。
タグは、ブラウザが HTML を表示するときに、どこを太字にするか、大文字にするか、斜体にするかを教える目印になります。
マークアップ言語とは、このようにタグを使って文書の表示を操作する言語です。

.. note::
  ちなみに、理論経済学者のほとんどが使っていると言われている、TeX 言語もマークアップ言語の一つです。
  TeX のマクロパッケージ、LaTeXでは ``\textbf{}`` で文字を囲みます。
  ここでは、``\textbf{}`` がタグになります。

タグに囲まれているものを要素の内容と呼びます。
タグの始まりを **開始タグ** と呼び、タグの終わりを **終了タグ** と呼びます。
終了タグは、``<b>`` ではなく、``</b>`` であることに注意してください。

タグに含まれている、``b`` を **要素** と呼びます。
最初に紹介したのは、内容を太字にする、``b`` 要素です。 
HTML にはその他にも様々な要素があります。

ドキュメントツリー
-------------------------

HTML には様々な要素があり、ほとんどの HTML 文書は要素が入れ子になっています。
要素の入れ子構造の全体を表したのが、ドキュメントツリーで、例えば次のようなものです。

.. blockdiag::

  blockdiag {
  node_width = 90;
  node_height = 30;
  span_width = 40;
  span_height = 35;
  orientation = portrait
    html -> head;
    html -> body;
    body -> div;
    body -> ol -> li;
    ol -> li;
    ol -> li;
  }

``html`` 要素は、全ての要素の最上位に位置するものです。
その下に位置するのは、``head`` 要素と ``body`` 要素です。
``head`` 要素はブラウザ上には表示されません。
文字コードや検索のためのキーワードなどをここに記述します。
私たちがブラウザ上で見る文書は、``body`` 要素の中に含まれています。

入れ子になっている要素間を **親子関係**、入れ子の階層が同じ要素間を **兄弟関係** と呼びます。
例えば、上の図では、``ol`` 要素と ``li`` 要素は親子関係、``div`` 要素と ``ol`` 要素は兄弟関係です。

要素の順番
------------------------

要素は大別して **ブロック** レベルと **インライン** レベルの要素に分かれます。
ブロックレベルの要素はインラインレベルの要素を入れ子にできますが、その逆はできません。

ある要素がブロックレベルかインラインレベルかは、文をタグで囲うと改行されるかで見分けられます。
改行されるならば、要素はブロックレベル、改行されないならば、要素はインラインレベルです。

基本的な要素を以下に紹介します。

ブロックレベルの要素
------------------------

h 要素
~~~~~~~~~~~~~~~~~~~~~~~~
``h1`` ～ ``h6`` 要素は、見出しを表示します。

.. code-block:: html

  <h1>H1</h1>　<h2>H2</h2> <h3>H3</h3> <h4>H4</h4> <h5>H5</h5> <h6>H6</h6>

.. raw:: html

  <h1>H1</h1> <h2>H2</h2> <h3>H3</h3> <h4>H4</h4> <h5>H5</h5> <h6>H6</h6>
  <p></p>

p 要素
~~~~~~~~~~~~~~~~~~~~~~~~
``p`` 要素は段落を示します。

.. code-block:: html

  段落１<p>段落２</p>

.. raw:: html

  段落１<p>段落２</p>

table 要素
~~~~~~~~~~~~~~~~~~~~~~~~
``table`` 要素は表を表示します。
``th`` 要素で列、``tr`` 要素で行、``td`` でセルを表します。

.. code-block:: html

  <table border=1>
    <th>列１</th><th>列２</th>
    <tr>
      <td>要素11</td> <td>要素12</td>
    </tr>
    <tr>
      <td>要素21</td> <td>要素22</td>
    </tr>
  </table>
  <p></p>

.. raw:: html

  <table>
    <th>列１</th><th>列２</th>
    <tr>
      <td>要素11</td> <td>要素12</td>
    </tr>
    <tr>
      <td>要素21</td> <td>要素22</td>
    </tr>
  </table>
  <p></p>

ul 要素
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``ul`` 要素は順不同箇条リストを表示します。
``li`` 要素はそのアイテムを表示します。

.. code-block:: html

  <ul>
    <li>hoge</li>
    <li>fuga</li>
  </ul>

.. raw:: html

  <ul>
    <li>hoge</li>
    <li>fuga</li>
  </ul>

ol 要素
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``ol`` 要素は順序付き箇条リストを表示します。
``li`` 要素はそのアイテムを表示します。

.. code-block:: html

  <ol>
    <li>hoge</li>
    <li>fuge</li>
  </ol>

.. raw:: html

  <ol>
    <li>hoge</li>
    <li>fuge</li>
  </ol>

dl 要素
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``dl`` 要素は記述リストを表示します。
``dt`` 要素は項目、``dd`` 要素は項目内容を表示します。

.. code-block:: html

  <dl>
    <dt>first</dt>
     <dd>１番</dd>
    <dt>second</dt>
     <dd>２番</dd>
  </dl>

.. raw:: html

  <dl>
    <dt>first</dt>
      <dd>１番</dd>
    <dt>second</dt>
      <dd>２番</dd>
  </dl>

div 要素
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``div`` 要素は文をグループ化します。

.. code-block:: html

  <div>ここはグループ</div>ここは違う

.. raw:: html

  <div>ここはグループ</div>ここは違う
  <p></p>


インラインレベルの要素
-------------------------------

a 要素
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``a`` 要素はハイパーリンクを付けます。

.. code-block:: html

  <a href='https://google.co.jp'>Google</a>

.. raw:: html

  <a href='https://google.co.jp'>Google</a>
  <p></p>

img 要素
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``img`` 要素は画像を表示します。

.. code-block:: html

  <img src="_images/python-logo-master-v3-TM.png" width="30%" height="30%">


.. image:: ../image/python-logo-master-v3-TM.png
  :scale: 50%

span 要素
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``span`` 要素は文をグループ化します。

.. code-block:: html

  <span>ここはグループ</span>ここは違う

.. raw:: html

  <span>ここはグループ</span>ここは違う
  <p></p>


入力フォーム
-------------------------------

input 要素
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``input`` 要素は様々な入力フィールドを表示します。
入力フィールドは ``type`` で選びます。
``value`` でチェックボックスや、ラジオボタンを押したときにどの値をデータとして送信するかを決めます。
``name`` で送信したデータがどの input 要素によるものかを識別します。

テキスト
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``text`` はテキスト入力フィールドを表示します。
``size`` で入力フィールドの大きさ、
``maxlength`` で最大入力文字数を決めます。

.. code-block:: html

  <input name="text" type="text" size="30" maxlength="20">

.. raw:: html

  <input name="text" type="text" size="30" maxlength="20">
  <p></p>

チェックボックス
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``checkbox`` はチェックボックスを表示します。

.. code-block:: html

   <input name="checkbox" type="checkbox" value="check">チェックする</input>

.. raw:: html

   <input name="checkbox" type="checkbox" value="check">チェックする</input>
   <p></p>

ラジオボタン
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``radio`` はラジオボタンを作ります。

.. code-block:: html

  <input type="radio" name="fruits" value="banana">バナナ
  <input type="radio" name="fruits" value="orange">オレンジ
  </input>

.. raw:: html

  <input type="radio" name="fruits" value="banana">バナナ
  <input type="radio" name="fruits" value="orange">オレンジ
  </input>
  <p></p>

送信ボタン
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``submit`` は送信ボタンを作ります。

.. code-block:: html

  <input name="submit" type="submit" value="送信"></input>

.. raw:: html

  <input name="submit" type="submit" value="送信"></input>
  <p></p>

セレクトボックス
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``select`` 要素はセレクトボックスを作ります。
各アイテムは ``option`` で囲みます。
``value`` で送るデータの値を指定します。

.. code-block:: html

  <select name="country">
  <option value="japan">日本</option>
  <option value="america">アメリカ</option>
  </select>

.. raw:: html

  <select name="country">
  <option value="japan">日本</option>
  <option value="america">アメリカ</option>
  </select>
  <p></p>

フォーム 要素
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``input`` 要素や ``select`` 要素はフォームの部品です。
次のようにすることで、データを送信することができます。

.. code-block:: html

  <form action='Webサイトの構成要素.html' method="post">
  </p>好きなフルーツは？<p>
  <input type="radio" name="fruits" value="banana">バナナ
  <input type="radio" name="fruits" value="orange">オレンジ
  <p>
  <input type="submit" value="送信"></input>
  </p>
  </form>

.. raw:: html

  <form action='Webサイトの構成要素.html' method="post">
  </p>好きなフルーツは？<p>
  <input type="radio" name="fruits" value="banana">バナナ
  <input type="radio" name="fruits" value="orange">オレンジ
  <p>
  <input type="submit" value="送信"></input>
  </p>
  </form>

CSS
========================================
これで、基礎的な HTML の書き方は分かったと思います。
それでは、以下の HTML の文を Web ブラウザで見てみましょう。

.. code-block:: html

  <h1>HTML の例</h1>
  こんにちは！
  <p>この文章は HTML で書きました！</p>
  <p>この講習会の目的は　Python で Web スクレイピングをできるようになることです。</p>
  <p>以下が Python のサイトです。</p>
  <a href='https://www.python.org/'>Python</a>

上の文は `このページ <html/example.html>`_ のように表示されるはずです。

デザインのセンスが全く感じられないでしょう。
普段見ている Web ページでは、文章が左端に固まっていないし、もう少し行間も適切です。
色もついてますね。

HTML は Web ページのデザインを担当していません。
この役割を担っているのは、CSS (Cascading Style Sheets) と呼ばれるものです。
HTML 文書内で CSS を使う場合、``style`` 要素を用います。
HTML のどの要素の内容を装飾するかを **セレクタ** というもので指定します。
Web スクレイピングをする際にも、この **セレクタ** を用いて、取ってくる内容を指定します。
セレクタの後の ``{}`` で装飾内容を指定します。
例えば、 以下の例は ``h1`` 要素の内容を赤色に変更しています。

.. code-block:: html

  <style>
    h1{color:rgb(255,0,0)}
  </style>
  <h1>HTML</h1>

.. raw:: html

  <style>
    #h1{color:rgb(255,0,0)}
  </style>
  <h1 id="h1">HTML</h1>

.. note::

  この例では CSS の内容を html 文書内に書いてますが、普通は CSS の内容を別ファイルに css として保存し、head 内で読み込みます。
  こうすることで、他のページでも使いまわすことができます。

id, class
------------------------------------
先の例では要素を指定すればうまくいきました。
それでは、次の例はどうでしょうか。ここでは、果物（リンゴ、バナナ、スイカ）のみの色を変えたいとします。
しかし、先ほどのように、``p`` 要素を指定してしまうと、牛肉の色も変わってしまいます。

.. code-block:: html

  <style>
    p{color:#ff00ff}
  </style>
  <p>リンゴ</p>
  <p>バナナ</p>
  <p>牛肉</p>
  <p>スイカ</p>

.. raw:: html

  <style>
    .pp{color:#008080}
  </style>
  <p class="pp">リンゴ</p>
  <p class="pp">バナナ</p>
  <p class="pp">牛肉</p>
  <p class="pp">スイカ</p>

こうした場合、あらかじめ HTML で果物のグループを作成しておけば、この問題は解決します。
``class="クラス名"`` をタグ内に記入することによって、グループを作成します。 
リンゴ、バナナ、スイカのタグ内に、fruits というクラス名を付けましょう。

CSS で ``class`` を指定する場合、セレクタは ``.クラス名`` とします。
この例の場合は、``.fruits`` です。

.. code-block:: html

  <style>
    .fruits{color:#008080}
  </style>
  <p class="fruits">リンゴ</p>
  <p class="fruits">バナナ</p>
  <p>牛肉</p>
  <p class="fruits">スイカ</p>

.. raw:: html

  <style>
    .fruits{color:#008080}
  </style>
  <p class="fruits">リンゴ</p>
  <p class="fruits">バナナ</p>
  <p>牛肉</p>
  <p class="fruits">スイカ</p>

上手くいきました！
さて、次にリンゴのみを赤にしたい場合はどうでしょうか。
ここでは ``id`` を使ってみましょう。
``id="id名"`` をタグ内に記入することによって、要素に id 名を割り振ることができます。
リンゴのタグ内に apple という id 名を付けてみましょう。

CSS で ``id`` を指定する場合、セレクタは ``#id名`` とします。この例の場合は、``#apple`` です。

.. note::
  ``class`` と ``id`` はどちらも要素に名前を付けることは一緒ですが、違うところもあります。
  ``class`` は複数の要素に同じクラス名を使えますが、``id`` は複数の要素が同じ id を持つことはできません。
  また、CSS で ``class`` と ``id`` で同じ要素を指定した場合、``id`` で指定した内容が実行されます。

.. code-block:: html

  <style>
    .fruits{color:#008080}
    #id{color:rgb(255,0,0)}
  </style>
  <p class="fruits" id="apple">リンゴ</p>
  <p class="fruits">バナナ</p>
  <p>牛肉</p>
  <p class="fruits">スイカ</p>

.. raw:: html

  <style>
    .fruits{color:#008080}
    #apple{color:rgb(255,0,0)}
  </style>
  <p class="fruits" id="apple">リンゴ</p>
  <p class="fruits">バナナ</p>
  <p>牛肉</p>
  <p class="fruits">スイカ</p>

セレクタをうまく使えば、思い通りに要素を指定することができます。基本的なセレクタの使い方をみてみましょう。


結合子
-----------------------------------------------
結合子を使うことによって、要素の子孫、兄弟関係にある要素を指定できます。

E F
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
E 要素の子孫の全ての F 要素

次の例は、``span`` 要素の子孫の ``p`` 要素を指定しています。
一方、``span`` 要素の子孫ではない ``p`` 要素、 ``span`` 要素の子孫の ``span`` 要素は指定されません。

.. code-block:: html

  <style>
    span p{color:#008080}
  </style>
  <span>果物
    <p>リンゴ</p>
    <p>メロン</p>
    <span>みかん</span>
  </span>
  <p>牛肉</p>

.. raw:: html

  <style>
    span p{color:#008080}
  </style>
  <span>果物
    <p>リンゴ</p>
    <p>メロン</p>
    <span>みかん</span>
  </span>
  <p>牛肉</p>


まだまだ説明できていない様々なセレクタがあります。
`HTML クイックリファレンス <http://www.htmq.com/csskihon/005.shtml>`_ はセレクタを網羅しているので、参照してみるとよいでしょう。
