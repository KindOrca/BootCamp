"""
Advanced Requirements

내장함수를 다양하게 활용할 줄 알아야 합니다.

요구사항:
    도전과제에서 주로 바라볼 부분은 예외사항입니다.
    우리가 실제로 마주할 문제들도 대부분 복합적인 문제이므로 계속해서 스스로 문제를 만들고 해결해보는 과정을 겪어보도록 합니다.
    문제를 해결하는 방법과 문제에서 요구하는 개념 간의 연관성을 찾아보면서 문제를 해결합니다.

    Part 3의 요구사항은 기본적으로 충족하고, 추가적인 예외사항을 해결해주세요.
    다양한 내장함수를 활용해봅니다.
    중복되는 문자열을 처리해줄 수 있도록 기능을 구현해주세요.
    소문자는 대문자로, 대문자는 소문자로 변경해주세요.

    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

    *예시 1* 
        입력값:
            'c t A'
        출력값:
            'a C T'
    
    *예시 2* 
        입력값:
            'z X y W v U t S'
        출력값:
            's u w x T V Y Z'
"""

def part4(s):
    from functools import reduce
    s_ = list(set(s.split()))
    s_sorted = sorted(s_)
    s_up_lo = map(lambda x : x.upper() if x.islower() else x.lower(), s_sorted)
    ans = reduce(lambda a,b: a+' '+b, s_up_lo)
    return ans

