T = int(input())
for test_case in range(1, T+1):
    a ,b = map(int,input().split())
    quotient, remainder = a//b, a%b
    
    print("#{} {} {}".format(test_case, quotient, remainder))