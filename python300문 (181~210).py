#181
#아래 표에서 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의하라.
apart = [["101호",'102호'],["201호","202호"],["301호","302호"]]


#182
#아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.
stock = [["시가",100,200,300],["종가",80,210,330]]


#183
#아래 표를 stock 이름의 딕셔너리로 표현하라.시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다. 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
stock = {"시가": [100,200,300],"종가": [80, 210, 330]}


#184
#아래 표를 stock 이라는 이름의 딕셔너리로 표현하라. 날짜를 key로 저장하고, 나머지 같은 행의 데이터를 리스트로 저장해서 value로 저장한다. 첫 열이 날짜이다.
stock = {"10/10":[80,110,70,90],"10/11": [210, 230, 190, 200]}

#185
#리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j,"호")

#186
#리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i:
        print(j,"호")


#187
#리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i[::-1]:
        print(j,"호")


#188
#리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j,"호")
        print("-"*5)

#189
#리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j,"호")
    print("----")


#190
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j,"호")
print("----")


#191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for j in i:
        print(j*1.00014)


#192
for i in data:
    for j in i:
        print(j*1.00014)
    print("----")

#193
result = []
for i in data:
    for j in i:
        result.append(j*1.00014)
print(result)


#194
result = []
for i in data:
    sub = []
    for j in i:
        sub.append(j*1.00014)
    result.append(sub)
print(result)


#195
#195
#ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 화면에 종가데이터를 출력하라.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    print(i[3])


#196
#종가가 150원보다 큰경우에만 종가를 출력하라.
for i in ohlc[1:]:
    if(i[3] > 150):
        print(i[3])


#197
#종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.
for i in ohlc[1:]:
    if (i[3] >= i[0]):
        print(i[3])

#198
#고가와 저가의 차이를 변동폭으로 정의할 때 변동폭을 volatility 이름의 리스트에 저장하라.
volatility = []
for row in ohlc[1:]:
    volatility.append(row[1]-row[2])


#201 "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
def print_coin():
    print("비트코인")


#202 201번에서 정의한 함수를 호출하라.
print_coin()


#203 201번에서 정의한 print_coin 함수를 100번호출하라.
for i in range(100):
    print_coin()


#204 "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
def print_coin():
    for i in range(100):
      print("비트코인")


#205
#hello()
#def hello():
    #print("Hi")
#함수가 정의되기 전에 호출되어서 에러가 발생합니다.


#206
#아래 코드의 실행 결과를 예측하라.

def message() :
    print("A")
    print("B")

message()
print("C")
message()



#207
#아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
print("A")

def message() :
    print("B")

print("C")
message()


#208
#아래 코드의 실행 결과를 예측하라.
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()

#209
#아래 코드의 실행 결과를 예측하라.

def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()


#210
#아래 코드의 실행 결과를 예측하라.

def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()







