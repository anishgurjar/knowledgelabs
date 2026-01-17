#Different ways to initialize dict
m = {}
m = {"a": 1, "b": 2}
pairs = [("a", 1), ("b", 2)]
m = dict(pairs)

#Accessing items
x = m["a"] #will throw error is item missing
x = m.get("a", 0) #safe, defualts to 0
print(x)

#adding elements
m["c"] = 3

#deleting
del m["c"] #unsafe
m.pop("c",None) #safe
print(m)

#Iteration Patterns
for key in m:
    pass

for value in m.values():
    pass

for key, value in m.items():
    pass

#Frequency Counting - Manual
nums = [0,3,4,0,1,3,1,2,1,0,3]
#freq = {}
#for i in nums:
#    if i not in freq:
#        freq[i] = 0
#    freq[x] += 1

#Pythonic (Preffered):
from collections import defaultdict
freq = defaultdict(int)
for x in nums:
    freq[x]+=1

print(freq)


#ALLOWED KEYS SHOULD BE
# a. Hashable
# b. Immutable
# Allowed keys: int, str, tuple, frozenkeys
# Not allowed: set, dict, list

