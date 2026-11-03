from PIL import Image
import glob
fs = sorted(glob.glob("D:/montage_work/blog_stupen2/slides_hd/slide*.png"))
print(len(fs), Image.open(fs[0]).size)
W, H = 480, 270
cols = 4
rows = (len(fs) + cols - 1) // cols
sh = Image.new("RGB", (cols * W, rows * H), "white")
for i, f in enumerate(fs):
    im = Image.open(f).convert("RGB").resize((W, H))
    sh.paste(im, ((i % cols) * W, (i // cols) * H))
sh.save("D:/montage_work/sheet.jpg", quality=85)
