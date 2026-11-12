# PC用: 元画像のフォルダを、軽いJPEGにして images/ に連番で追加し、images.js に1行ずつ足します。
# 使い方:  pip install pillow   →   python tools/prepare.py 元画像のフォルダ [長辺px=900] [画質=76]
import sys, os, re
from PIL import Image
src = sys.argv[1]; size = int(sys.argv[2]) if len(sys.argv) > 2 else 900; q = int(sys.argv[3]) if len(sys.argv) > 3 else 76
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
js = os.path.join(root, "images.js"); text = open(js, encoding="utf-8").read()
nums = [int(n) for n in re.findall(r'"(\d+)\.jpg"', text)]; n = max(nums) if nums else 0
new = []
for f in sorted(os.listdir(src)):
    if not f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")): continue
    im = Image.open(os.path.join(src, f)).convert("RGB"); m = min(1, size / max(im.size))
    im = im.resize((round(im.size[0] * m), round(im.size[1] * m)), Image.LANCZOS)
    n += 1; name = "%03d.jpg" % n
    im.save(os.path.join(root, "images", name), "JPEG", quality=q, optimize=True, progressive=True)
    new.append(' ["%s"],' % name)
if new:
    text = text.replace("\n];", "\n" + "\n".join(new) + "\n];")
    open(js, "w", encoding="utf-8").write(text)
print(len(new), "枚追加しました")
