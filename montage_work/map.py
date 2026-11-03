import json
P = "D:/montage_work/blog_stupen2/"
k = json.load(open(P + "keep.json", encoding="utf-8"))
ch = json.load(open(P + "words.json", encoding="utf-8"))["chunks"]


def src(t):
    c = 0
    for a, b in k:
        if c + b - a >= t:
            return a + t - c
        c += b - a


for m, s in [(9, 27), (9, 30), (12, 33), (17, 9), (29, 40), (38, 33)]:
    x = src(m * 60 + s)
    print("=== cut %d:%02d -> src %.2f" % (m, s, x))
    for c in ch:
        if c["start"] - 6 <= x <= c["end"] + 6:
            print(" #%s %.2f-%.2f %s" % (c["id"], c["start"], c["end"], c["text"]))
