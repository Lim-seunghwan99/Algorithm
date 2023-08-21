N = int(input())
arr1 = [None] * 26
arr2 = [None] * 26
for i in range(N):
    a, b, c = input().split()
    a1 = ord(a) - 65
    if b == '.':
        pass
    else:
        b1 = ord(b) - 65
        arr1[a1] = b1
    if c == '.':
        pass
    else:
        c1 = ord(c) - 65
        arr2[a1] = c1
def preorder(root):
    if root is not None:
        print(chr(root+65), end='')
        preorder(arr1[root])
        preorder(arr2[root])


def inorder(root):
    if root is not None:
        inorder(arr1[root])
        print(chr(root+65), end='')
        inorder(arr2[root])


def postorder(root):
    if root is not None:
        postorder(arr1[root])
        postorder(arr2[root])
        print(chr(root + 65), end='')


preorder(0)
print()
inorder(0)
print()
postorder(0)