"""
Advanced Requirements
반복문과 조건문을 활용한 문제를 해결은 계속됩니다.

요구사항:
    복합적으로 엮여있는 조건을 하나씩 풀어봅니다.
    추상도가 높고 프로그래밍에 대한 언급이 없을 수록 문제해결은 어려워집니다.
    머신러닝과 딥러닝에서 봤었던 복잡한 수식이 어떻게 코드화되었는지 함께 생각해보면서 아래 문제를 해결합니다.

    1부터 1이상의 입력받은 숫자까지 모든 숫자에 대해 소수가 몇 개 있는지 반환하세요.
    0이하의 경우 ValueError를 발생시켜 주세요.
"""

def part3(N):
    idx = [True] * N
    sqrt = int(N ** 1/2)
    for i in range(2, sqrt+1):
        if idx[i]:
            for j in range(i+i, N, i):
                idx[j] = False
    
    prime = [i for i in range(2, N) if idx[i]]

    if len(prime) > 0:
        return len(prime)
    raise ValueError
