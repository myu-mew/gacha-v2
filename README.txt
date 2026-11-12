みゅ画像ガチャ（フォルダ版）

【中身】
index.html   … ガチャ本体（ほぼ触らなくてOK）
images.js    … 景品の一覧（1行が1枚）
images/      … 景品の画像
assets/      … 背景とボタンの画像

【景品を増やす方法】
1. 画像を images フォルダに入れる（例: 009.jpg）
2. images.js の最後の ]; の上に1行足す
     ["009.jpg","ひとこと解説"],
   （解説は省略できます: ["009.jpg"],）
※ 画像を並べ替えたり消したりしても、保存データはファイル名で管理しているので、ずれません。
※ 同じファイル名の画像を入れ替えると、アルバムの記録はそのまま引き継がれます。

【PCでまとめて増やす方法（任意）】
tools/prepare.py を使うと、元画像を軽いJPEGにして、連番で images に入れて、images.js にも自動で書き足します。
  pip install pillow
  python tools/prepare.py 元画像のフォルダ

【見るとき】
・フォルダごと GitHub Pages などに公開する（index.html を開けば動きます）
・PCに置くなら、index.html をブラウザで開く
※ Claudeアプリ内のプレビューなど、HTML1枚だけを開く場所では画像が出ません。
