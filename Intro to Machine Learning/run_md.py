import re, sys

text = open(sys.argv[1], encoding="utf-8").read()
blocks = re.findall(r"```python\n(.*?)```", text, re.DOTALL)

for code in blocks:
    exec(code)