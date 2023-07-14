def solution():
    S = list(input())
    n = S
    alpha =[0] * 26
    for i in range(len(n)):
        if n[i] == 'a':
            alpha[0] += 1
        elif n[i] == 'b':
            alpha[1] += 1
        elif n[i] == 'c':
            alpha[2] += 1
        elif n[i] == 'd':
            alpha[3] += 1
        elif n[i] == 'e':
            alpha[4] += 1
        elif n[i] == 'f':
            alpha[5] += 1
        elif n[i] == 'g':
            alpha[6] += 1
        elif n[i] == 'h':
            alpha[7] += 1
        elif n[i] == 'i':
            alpha[8] += 1
        elif n[i] == 'j':
            alpha[9] += 1
        elif n[i] == 'k':
            alpha[10] += 1
        elif n[i] == 'l':
            alpha[11] += 1
        elif n[i] == 'm':
            alpha[12] += 1
        elif n[i] == 'n':
            alpha[13] += 1
        elif n[i] == 'o':
            alpha[14] += 1
        elif n[i] == 'p':
            alpha[15] += 1
        elif n[i] == 'q':
            alpha[16] += 1
        elif n[i] == 'r':
            alpha[17] += 1
        elif n[i] == 's':
            alpha[18] += 1
        elif n[i] == 't':
            alpha[19] += 1
        elif n[i] == 'u':
            alpha[20] += 1
        elif n[i] == 'v':
            alpha[21] += 1
        elif n[i] == 'w':
            alpha[22] += 1
        elif n[i] == 'x':
            alpha[23] += 1
        elif n[i] == 'y':
            alpha[24] += 1
        elif n[i] == 'z':
            alpha[25] += 1
    print(*alpha)
solution()