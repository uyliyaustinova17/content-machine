import json
P = "D:/montage_work/blog_stupen2/cuts.json"
c = json.load(open(P, encoding="utf-8"))
c["232"] = {"keep": [[1143.51, 1157.21], [1158.33, 1167.25]], "why": "убрано «может попробовать клуб» (оговорка), дальше «может попробовать разные упражнения»"}
c["563"] = {"keep": [[2707.93, 2711.37]], "why": "убрано лишнее «проще» в конце, оно в начале #564"}
json.dump(c, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
