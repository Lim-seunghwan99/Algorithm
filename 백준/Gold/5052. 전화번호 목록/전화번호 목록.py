t = int(input())
for _ in range(t):
    trie = {}
    n = int(input())
    tel = sorted([input() for i in range(n)])
    ans = "YES"
    for i in range(n):
        node = trie
        for char in tel[i]:
            if char not in node:
                node[char] = {}
            node = node[char]
            if '#' in node:
                ans = "NO"
        node['#'] = True

    print(ans)