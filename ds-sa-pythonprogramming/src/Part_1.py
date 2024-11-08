"""
Bare Minimum Requirements

컬렉션 자료형을 다양하게 활용할 줄 알아야 합니다.

요구사항:
    컴퓨터공학 기본을 시작하면서 첫 프로그래밍 과제입니다.
    수학문제를 풀 때 덧셈부터 시작하듯이 프로그래밍에서도 기초부터 여러번 반복해보도록 합니다.
    아래에서 요구되는 요구조건과 테스트 통과코드방법은 하나일 수 있지만 다양한 방법을 생각해보면서 프로그래밍을 진행하도록 합니다.
    
    '1부터 101 사이에 있는 모든 제곱수'를 하나의 리스트로 반환하는 코드를 작성해주세요.
    제곱수 : 1, 4, 9, 16,...,81, 100
    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

        입력값:
            없음    
        출력값:
            [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def part1():
    ans = []
    l,a = 1,1
    while a < 100:
        a = l*l
        ans.append(a)
        l+=1
    return ans