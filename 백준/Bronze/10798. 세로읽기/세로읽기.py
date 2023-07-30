def readwords():
    word_arr = [['*' for j in range(15)]for i in range(5)]

    for i in range(5):
        word_list = input()
        for idx, word in enumerate(word_list):
            word_arr[i][idx] = word

    for j in range(15):
        for i in range(5):
            if word_arr[i][j] == '*':
                continue
            print(word_arr[i][j], end = '')
readwords()