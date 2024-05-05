#Longest Substring Without Repeating Characters
s = 'abcabcbb'
# seen = {}
length,l=0,0
# for r in range(len(s)):
#     char = s[r]
#     if char in seen and seen[char] >= l:
#         l = seen[char] + 1
#     else:
#         length = max(length, r-l+1)
#     seen[char] = r
# print(length)

seen = set()
for r in range(len(s)):
    char = s[r]
    if char in seen:
        l = r+1
        senn=set()
    else:
        length = max(length, r-l+1)
    seen.add(char)
print(length)