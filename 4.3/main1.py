def is_palindrome(s):

    if len(s) == 0: raise ValueError

    if not isinstance(s, str): raise TypeError

    return s == s[::-1]



def average(lst) -> float:

    if not isinstance(lst, list): raise TypeError

    return sum(lst) / len(lst)



class BankAccount:
    def init(self):
        self.__balance = 0

    def deposit(self, amount: int or float) -> int or float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: int or float) -> int or float:
        if amount < self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self) -> int or float:
        return self.__balance



class Library:
    def __init(self):
        self.__books = {}

    def add_book(self, book):
        if book not in self.__books and book.strip():
            self.__books[book] = 1
        else:
            self.__books[book] += 1

    def remove_book(self, book):
        if book in self.__books:
            self.__books[book] -= 1
            if self.__books[book] == 0:
                del self.__books[book]
        else:
            print("Book not found")

    def find_book(self, book):
        return self.__books.get(book, 0) > 0