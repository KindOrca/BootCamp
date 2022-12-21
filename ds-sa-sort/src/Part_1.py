"""
Bare Minimum Requirements
정렬을 구현하며 반복문과 조건문의 흐름을 파악합니다.

요구사항:
    정렬은 대부분의 상황에서 활용되는 대표적인 개념입니다.
    프로그래밍의 반복문과 조건문의 중요성을 다시 한 번 상기하면서 정렬이라는 목적을 달성해봅니다.
    정렬 개념을 적용하여 소스코드를 작성해주세요.

    파이썬에서 제공되는 sort와 같은 내장함수를 사용하면 안됩니다.
    반복문과 조건문만을 활용하여 구현하시길 바랍니다.
"""

def bubble_sort(li):
    """
    # 문제 1.
        거품정렬을 구현해주세요.
        매개변수로 들어온 리스트를 오름차순으로 정렬해주세요.
        단 매개변수로 들어오는 요소는 전부 정수입니다. 

        ex)
            li = [54, 26, 93, 17, 77, 31]
            bubble_sort(li)
            print(li) # [17, 26, 31, 54, 77, 93]
    """
    check = False
    for end in range(len(li)-1,0,-1):
        for i in range(end):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
                check = True
        if not check: break


def insertion_sort(li):
    """
    # 문제 2.
        삽입정렬을 구현해주세요.
        매개변수로 들어온 리스트를 오름차순으로 정렬해주세요.
        단 매개변수로 들어오는 요소는 전부 정수입니다. 

        ex)
            li = [54, 26, 93, 17, 77, 31]
            insertion_sort(li)
            print(li) # [17, 26, 31, 54, 77, 93]
    """
    for end in range(1, len(li)):
        for i in range(end, 0, -1):
            if li[i-1] > li[i]:
                li[i-1], li[i] = li[i], li[i-1]
            else: break



def selection_sort(li):
    """
    # 문제 3.
        선택정렬을 구현해주세요.
        매개변수로 들어온 리스트를 오름차순으로 정렬해주세요.
        단 매개변수로 들어오는 요소는 전부 정수입니다. 

        ex)
            li = [54, 26, 93, 17, 77, 31]
            selection_sort(li)
            print(li) # [17, 26, 31, 54, 77, 93]
    """
    for i in range(len(li)-1):
        min_idx = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_idx]:
                min_idx = j
        li[i], li[min_idx] = li[min_idx], li[i]
