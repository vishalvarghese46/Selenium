from collections import Counter, defaultdict

s = 'mississippi'
cnt = Counter()
for i in s:
    cnt[i]+=1

print(cnt.most_common(10))
d = defaultdict(list)

for x,y in cnt.most_common(10):
    d[x].append(y)
print(d)
