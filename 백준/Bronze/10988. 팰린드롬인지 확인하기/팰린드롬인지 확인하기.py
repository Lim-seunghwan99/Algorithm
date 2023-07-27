def pelindrop():
    word = input()
    if word == word[::-1]:
        return 1
    else:
        return 0
print(pelindrop())