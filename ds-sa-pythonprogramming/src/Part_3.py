"""
Bare Minimum Requirements

컬렉션 자료형의 기본특징과 내장함수를 이해하고 활용할 줄 알아야 합니다.

요구사항:
    프로그래밍뿐만 아니라 데이터 직군, IT 직군에서 자주 활용되는 내장함수에 익숙해지도록 합니다.
    내장함수를 활용한 경우와 활용하지 않은 경우의 차이점에 대해 생각해보면서 문제를 해결합니다.

    자유롭게 문자를 입력받아 알파벳순서대로(A~Z, a~z) 정렬하세요.
    문자를 정렬하기 위한 값의 비교는 아스키코드의 십진법을 기준으로 합니다.
    중복되는 문자열을 처리해줄 수 있도록 기능을 구현해주세요.
    영어 소문자와 대문자에 대해서만 정렬을 진행하도록 합니다.
    
    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

    *예시 1* 
        입력값:
            'a T C'
        출력값:
            'C T a'

    *예시 2* 
        입력값:
            'z X y D c A b U'
        출력값:
            'A D U X b c y z'
"""

def part3(s):
    from functools import reduce
    s_ = list(set(s.split()))
    s_sorted = sorted(s_)
    ans = reduce(lambda a,b: a+' '+b, s_sorted)
    return ans


a = 'A D U X b c y z'
print(part3(a))