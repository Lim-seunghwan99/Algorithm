t=int(input())
for i in range(t):
  numbers=list(map(int,input().split()))
  big=max(numbers)
  small=min(numbers)

  lcm=0
  j=1
  while True:
    if (big*j)%small==0:
      lcm=big*j
      break
    j+=1
  print(lcm)