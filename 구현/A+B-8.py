n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    ans = a+b
    print("Case #%s: %s + %s = %s"%(i+1,a,b,ans))