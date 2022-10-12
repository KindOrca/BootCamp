"""
Advanced Requirements
OOP에서 중요한 것은 기능별로 정확한 설계입니다.

요구사항:
    아래 작성된 내용은 전체 설명이 아니기 때문에 소스코드를 보시면서 설계를 하시길 바랍니다.

    Person(사람)
        사서 또는 이용자에 대한 기본정보를 보여준다.

    Librarian(사서)
    사서는 Person으로부터 상속을 받야야한다.
    사서에 대한 정보(변수): 
        - 이름
        - 나이
        - 관리하는 책 리스트(private): 생성시 빈 리스트로 초기화한다.

        주요 기능
            사서는 관리하는 책 리스트에 책을 추가하는 함수를 가지고 있다.
            사서는 서적을 대출해주는 함수를 가지고 있다.
            사서가 관리하는 책의 리스트는 외부에서 접근할 수 없다.
            사서는 관리하는 책의 리스트를 반환하는 함수를 가지고 있다.

    User(이용자)
        이용자는 Person으로부터 상속을 받야야한다.
        이용자에 대한 정보(변수): 이름, 나이, 빌린 책 리스트(private)
        - 이름
        - 나이
        - 빌린 책 리스트(private): 생성시 빈 리스트로 초기화한다.

        주요 기능
            이용자는 책을 빌리는 함수를 가지고 있다.
            이용자는 빌린 책을 반환하는 함수를 가지고 있다.
            이용자가 빌린 책의 리스트는 외부에서 접근할 수 없다.
            이용자는 빌린 책의 리스트를 반환하는 함수를 가지고 있다.
"""


class Person:
    """
    ## Person 클래스의 코드는 수정하지 마세요 ##
    이미 완성된 코드입니다.
    아래 코드를 활용하여 문제를 해결해주세요.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print('안녕하세요! 제 이름은 {}, {}살 입니다!'.format(self.name, self.age))
        
        
class Book:
    """
    ## Book 클래스의 코드는 수정하지 마세요 ##
    이미 완성된 코드입니다.
    아래 코드를 활용하여 문제를 해결해주세요.
    """
    def __init__(self, book_name, librarian):
        self.book_name = book_name
        self.librarian = librarian


class Librarian(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__booklist = []

    def add_book(self, book):   #새책을 받거나, 반납받는 함수
        self.__booklist.append(book)

    def remove_book(self, book):    #책을 빌려주는 함수
        """
        리스트에 해당하는 책이 없을때는 False를,
        있을 경우 삭제 후에 True를 리턴해주세요~!
        """
        if book in self.__booklist:
            self.__booklist.remove(book)
            return True
        return False

    def get_book_list(self):    #관리중인 책 목록을 반환하는 함수
        return self.__booklist


class User(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__booklist = []

    def borrow_book(self, book): #책을 대출하는 함수
        self.__booklist.append(book)

    def return_book(self, book): #책을 반납하는 함수
        """
        리스트에 해당하는 책이 없을때는 False를,
        있을 경우 삭제 후에 True를 리턴해주세요~!
        """
        if book in self.__booklist:
            self.__booklist.remove(book)
            return True
        return False

    def get_borrowed_list(self):    #빌린 책 목록을 반환하는 함수
        return self.__booklist
