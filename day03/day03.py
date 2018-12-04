import re
from collections import defaultdict

pattern = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
areas = defaultdict(list)
for line in open('input.txt').readlines():
    i, x, y, w, h = map(int, pattern.match(line).groups())
    for dx in range(x, w + x):
        for dy in range(y, h + y):
            areas[(dx, dy)].append(i)

count = 0
candidates = set()
disabled = set()
for k, v in areas.items():
    if len(v) == 1:
        candidates.add(v[0])
    else:
        count += 1
        for c in v:
            disabled.add(c)
            
for d in disabled:
    if d in candidates:
        candidates.remove(d)

print(count)  # part 1
print(candidates)  # part 2
