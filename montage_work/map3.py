import json, sys
P = "D:/montage_work/blog_stupen2/"
d = json.load(open(P + "words.json", encoding="utf-8"))
print(list(d.keys()))
for c in d["chunks"]:
    if c["id"] in sys.argv[1:]:
        print("#" + c["id"], c["start"], c["end"], c["text"])
        for w in c.get("words", []):
            print("   ", w)
