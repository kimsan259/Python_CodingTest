# n = int(input())
#for i in range(n):
#    print(" " * i + "*" * ((n - i) * 2 - 1))
#for i in range(n - 2, -1, -1):
#    print(" " * i + "*" * ((n - i) * 2 - 1))

n = int(input())
for i in range(n,0,-1):
    print(' ' * (n-i) + '*' * 2*i-1)
for i in range(1,n):
    print(' ' * (n-i) + '*' * 2*i-1)