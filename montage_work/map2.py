import json, re
P = "D:/montage_work/blog_stupen2/"
k = json.load(open(P + "keep.json", encoding="utf-8"))
ch = json.load(open(P + "words.json", encoding="utf-8"))["chunks"]
cuts = json.load(open(P + "cuts.json", encoding="utf-8"))


def cut_t(x):
    c = 0
    for a, b in k:
        if a <= x <= b:
            return c + x - a
        c += b - a
    return None


def fm(t):
    return "%d:%05.2f" % (t // 60, t % 60)


for c in ch:
    t = cut_t(c["start"] + 0.05)
    if t is not None and (9 * 60 + 10 <= t <= 9 * 60 + 50):
        print(fm(t), "#" + c["id"], "%.2f" % c["start"], c["text"], "|", cuts.get(c["id"]))
