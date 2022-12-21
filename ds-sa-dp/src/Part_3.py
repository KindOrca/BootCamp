"""
Advanced Requirements
추상적 문제에 대해서 다양한 알고리즘을 활용하여 문제를 해결하기

요구사항:
    어렵고 불편한 추상화된 상황을 느껴보도록 합니다.
    아래 문제에서는 단순한 정답맞추기가 아닌 내부로직을 어떻게 구성해야할지 다방면으로 생각해봅니다.

    입력된 숫자를 특정 문자열 형태로 변환하는 문제입니다.
    아래 예상 입출력을 보면서 어떤 식으로 배열과 반복문, 조건문을 구성해야 할지 생각해봅니다.

    Case 1
        입력
        0
        출력 
        Zero.

    Case 2
        입력
        11
        출력 
        Eleven.

    Case 3
        입력
        1043283
        출력 
        One million, forty-three thousand, two hundred and eighty-three.
"""

def word_logic(num):
    word_box = {
        0:'zero',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen',
        20:'twenty',
        30:'thirty',
        40:'forty',
        50:'fifty',
        60:'sixty',
        70:'seventy',
        80:'eighty',
        90:'ninety',
        100:'hundred',
        1000:'thousand',
        1000000:'million'
    }
    if num < 100 and num > 20:
        A = (num // 10) * 10
        B = num % 10
        word_result = word_box[A]
        if B != 0:
            word_result += '-' + word_box[B]
    elif num < 1000 and num > 100:
        A = num // 100
        B = num % 100
        word_result = word_box[A] + ' ' + word_box[100]
        if B != 0:
            word_result += ' and ' + word_logic(B)
    # elif num > 1000:
    #     A = num // 1000
    #     B = num % 1000
    #     word_result = word_box[A] + ' '  + word_box[1000]
    #     if B != 0:
    #         word_result += ', ' + word_logic(B)
    else:
        word_result = word_box[num]
    return word_result

def number_logic(num):
    if num == 0: return 'Zero.'
    ret = ''
    number_list = [1000000,1000]
    for a in number_list:
        A = num // a
        if A > 0:
            ret += word_logic(A) + ' ' + word_logic(a)
            num %= a
            if a != 1:
                ret += ', '
    if num != 0:
        ret += word_logic(num)
    else:
        ret = ret[:-1]
    ret += '.'
    return ret.capitalize()