import json
P = "D:/montage_work/blog_stupen2/"
k = json.load(open(P + "keep.json", encoding="utf-8"))
ch = json.load(open(P + "words.json", encoding="utf-8"))["chunks"]
cuts = json.load(open(P + "cuts.json", encoding="utf-8"))


def src(t):
    c = 0
    for a, b in k:
        if c + b - a >= t:
            return a + t - c
        c += b - a


def tt(s):
    m, x = s.split(":")
    return int(m) * 60 + float(x)


for s in ["4:48.60", "15:31.08", "20:20.15", "36:04.49", "17:00.04", "0:13.38", "39:22.28", "48:15.81"]:
    x = src(tt(s))
    print("=== cut", s, "-> src %.2f" % x)
    for c in ch:
        if c["start"] - 4 <= x <= c["end"] + 4:
            d = cuts.get(c["id"])
            print(" #%s %.2f-%.2f [%s] %s" % (c["id"], c["start"], c["end"], d if isinstance(d, str) else json.dumps(d, ensure_ascii=False)[:60], c["text"][:120]))
            if c["start"] - 1 <= x <= c["end"] + 1:
                print("    ", " ".join("%s(%.2f)" % (w["text"], w["start"]) for w in c.get("words", [])))
