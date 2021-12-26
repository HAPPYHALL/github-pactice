# 271 Account 클래스

import random


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        # 문자열 앞 0채우기
        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3
        # 001-01-000001


kim = Account("김시은", 1000)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account_number)

# 272 클래스 변수
# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.
import random


class Account:
    account_count = 0  ##################

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1
        # 클래스로부터 생성된 계좌 객체의 개수를 얻는 식
        # 함수 내의 영향을 받기 때문에! 들여쓰기!!주의


kim = Account("김시은", 1000)
print(Account.account_count)  # 답 1
lee = Account("이민수", 100)
print(Account.account_count)  # 답 2

# 273 클래스 변수 출력
# Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.
import random


class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001

        Account.account_count += 1

    @classmethod
    # 인스턴스(객체)를 만들지 않아도 class의 메서드를 바로 실행할 수 있다
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count


kim = Account("김민수", 100)
lee = Account("이민수", 100)
lee.get_account_num()  # 2


# 274 입금 메서드

# Account 클래스에 입금을 위한 deposit 메서드를 추가하세요.
# 입금은 최소 1원 이상만 가능합니다.

# def deposit(self, amount):------# ########amount가 왜 나와? (위 cls 영향을 받나?)
#    if amount >= 1:
#       self.balance += amount

# print(Account.amount)


# 275 출금 메서드

# Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요.
# 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.

# def withdraw(self, amount):
#    if self.balance > amount :
#       self.balance -= amount


# k = Account("kim", 100)
# k.deposit(100)  # 100+100=200
# k.withdraw(90)  #200-90=110
# print(k.balance)  #110


# 276 정보 출력 메서드
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.

# def display_info(self)
#     print("은행이름: ", self.bank)
#     print("예금주: ", self.name)
#     print("계좌번호: ", self.account_number)
#     print("잔고: ", format(self.balance, ','))
# 1000단위마다 , 넣기 --->  format(숫자, ',')


# p = Account("파이썬", 10000)
# p.display_info()


# 277 이자 지급하기
# 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.

#   def deposit(self, amount):
#        if amount >= 1:
#            self.balance += amount
#
#            self.deposit_count += 1
#            if self.deposit_count % 5 == 0:         # 5, 10, 15
#                # 이자 지급
#                self.balance = (self.balance * 1.01)

# p = Account("파이썬", 10000)
# p.deposit(10000)
# p.deposit(10000)
# p.deposit(10000)
# p.deposit(5000)
# p.deposit(5000) ----->5번째
# print(p.balance)


# 278 여러 객체 생성
# Account 클래스로부터 3개 이상 인스턴스를 생성하고
# 생성된 인스턴스를 리스트에 저장해보세요.
#
#
# data = []
# k = Account("KIM", 10000000)
# l = Account("LEE", 10000)
# p = Account("PARK", 10000
#
# append는 덧붙인다는 뜻으로 괄호( ) 안에 값을 입력하면 새로운 요소를 array 맨 끝에 객체로 추가한다.
# data.append(k)
# data.append(l)
# data.append(p)
#
# print(data)

# ----------답-----------
#   [ <__main__.Account object at 0x0000023E1E487EB0>,
#   <__main__.Account object at 0x0000023E1E485510>,
#   <__main__.Account object at 0x0000023E1E4854B0> ]


# 279 객체 순회
# 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.

# ************************************
# for c in data:
#     if c.balance >= 1000000:
#         c.display_info()
# *************************************

# 답
# 은행이름:  SC은행
# 예금주:  KIM
# 계좌번호:  380-51-150638
# 잔고:  10000000


# 280 입출금 내역
# 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.
# def withdraw_history(self):
#     for amount in self.withdraw_log:
#         print(amount)
#
#
# def deposit_history(self):
#     for amount in self.deposit_log:
#         print(amount)
#
#
# k = Account("Kim", 1000)
# k.deposit(100)
# k.deposit(200)
# k.deposit(300)
# k.deposit_history()
#
# k.withdraw(100)
# k.withdraw(200)
# k.withdraw_history()




# 281
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


car = 차(2, 1000)
print(car.바퀴)
print(car.가격)


# 282 클래스 상속
# 차 클래스를 상속받은 자전차 클래스를 정의하세요.

class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자전차(차):
    pass


# 283 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.

class 차:
    def __init__(self,바퀴,가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자전차(차):
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


bicycle = 자전차(2, 100)
print(bicycle.가격)


# 284 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요.
# 단 자전차 클래스는 차 클래스를 상속받습니다.

class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        self.바퀴 = 바퀴  ## super()로 기반 클래스의 __init__ 메서드 호출
        self.가격 = 가격  # super().__init__(바퀴, 가격)로도 표현
        self.구동계 = 구동계


bicycle = 자전차(2, 100, "시마노")
print(bicycle.구동계)


# 285 클래스 상속
# 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


# 286 부모 클래스 생성자 호출
# 다음 코드가 동작하도록 자전차 클래스를 수정하세요.
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)


class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)


class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계


bicycle = 자전차(2, 100, "시마노")
bicycle.정보()


# 287 부모 클래스 메서드 호출
# 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.

#     def 정보(self):
#         super().정보()
#         print("구동계 ", self.구동계)
#
# bicycle = 자전차(2, 100, "시마노")
# bicycle.정보()


# 288 메서드 오버라이딩

# 오버라이드(Override)
# - 같은 이름을 가진 메소드를 덮어쓴다
# 다음 코드의 실행 결과를 예상해보세요.

class 부모:
    def 호출(self):
        print("부모호출")


class 자식(부모):
    def 호출(self):
        print("자식호출")


나 = 자식()
나.호출()  # 자식호출


# 289 생성자
class 부모:
    def __init__(self):
        print("부모생성")


class 자식(부모):
    def __init__(self):
        print("자식생성")


나 = 자식()  # 자식생성


# 290 부모클래스 생성자 호출
class 부모:
    def __init__(self):
        print("부모생성")


class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()


나 = 자식()  # 부모생성

# 291 파일 쓰기
# 바탕화면에 '매수종목1.txt' 파일을 생성한 후 다음과 같이 종목코드를 파일에 써보세요.
#
# 005930
# 005380
# 035420


#
# 292 파일 쓰기
# 바탕화면에 '매수종목2.txt' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요.
#
# 005930 삼성전자
# 005380 현대차
# 035420 NAVER

#
# 293 CSV 파일 쓰기
# 바탕화면에 '매수종목.csv' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요. 인코딩은 'cp949'를 사용해야합니다.


# 294 파일 읽기
# 바탕화면에 생성한 '매수종목1.txt' 파일을 읽은 후 종목코드를 리스트에 저장해보세요.
#
# 005930
# 005380
# 035420


# 295 파일 읽기
# 바탕화면에 생성한 '매수종목2.txt' 파일을 읽은 후 종목코드와 종목명을 딕셔너리로 저장해보세요. 종목명을 key로 종목명을 value로 저장합니다.
#
# 005930 삼성전자
# 005380 현대차
# 035420 NAVER
