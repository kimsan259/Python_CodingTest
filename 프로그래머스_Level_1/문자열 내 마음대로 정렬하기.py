def solution(strings,n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return 하세요'''
    return sorted(strings, key=lambda x: x[n])

strings = ["sun","bed","car"]
print(solution(strings, 1))