#151
#리스트에는 네 개의 정수가 저장돼 있다.
리스트 = [3, -20, -3, 44]
#for문을 사용해서 리스트의 음수를 출력하라.
for i in 리스트:
    if i <0 :
        print(i)
#들여쓰기의 중요성

#152
#for문을 사용해서 3의 배수만을 출력하라.
리스트 = [3, 100, 23, 44]
for 변수 in 리스트:
 if 변수 % 3 == 0:
     print(변수)

#153
#리스트에서 20 보다 작은 3의 배수를 출력하라
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if (i < 20) and (i % 3 == 0):
        #하나 이상의 조건을 비교할 때는 논리 연산자를 사용해야겠죠? 두 조건이 모두 참일 때만 실행돼야 하므로 and 연산자를 사용합니다.
        print(i)

#154
#리스트에서 세 글자 이상의 문자를 화면에 출력하라

리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i) >= 3:
        print(i)
#문자열의 길이를 계산하는 len() 함수


#155
#리스트에서 대문자만 화면에 출력하라.

리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.isupper():
        print(i)
        # isupper() 메서드는 대문자 여부를 판별합니다.


#156
#리스트에서 소문자만 화면에 출력하라.
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
  if i.isupper() == False:  #if 변수.isupper() != True:  # if not 변수.isupper():
    print(i)

#157
#이름의 첫 글자를 대문자로 변경해서 출력하라.

리스트 = ['dog', 'cat', 'parrot']

for i in 리스트:
    first = i[0]
    대문자 = first.upper()
    print(대문자 + i[1:])


#158
#파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']

for i in 리스트:
    a = i.split(".")[0]
    print(a)


#159
#파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in 리스트:
    a = i.split(".")
    if a[1] == "h":
        print(a[0])


#160
#파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in 리스트:
    a = i.split(".")
    if (a[1] == "h") or (a[1] == "c"):
         print(a[0])


#161
#for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.
for i in range(100):
    print(i)


#162
#월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.

for i in range(2002,2051,4):
    print (i)

#163
#1부터 30까지의 숫자 중 3의 배수를 출력하라.
for i in range(3,31,3):
    print(i)


#164
#99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
for i in range(100):
    print(99-i)

#or

for i in list(range(0,100))[::-1]:
    print(i)

#165
#for문을 사용해서 아래와 같이 출력하라.

for i in range(10):
    print(i/10,i)


#166
#구구단 3단을 출력하라.

for i in range(1,10):
    print(3,"x", i, "=", 3*i)

#167
#구구단 3단을 출력하라. 단 홀수 번째만 출력한다.
for i in range(1,10,2):
    print(3,"x",i,"=",3*i)
#or
num = 3
for i in range(1,10):
    if i % 2 == 1 :
        print (num,"x", i,"=",num*i)


#168
#1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.

sum = 0
for i in range(1,11):
    sum += i  #sum = sum+1
print("합 :",sum)


#169
#1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
sum = 0
for i in range(1,11,2):
    sum += i
print("합 :",sum)

#170
#1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.

result = 1 #0에서 시작하면 곱셈이 0이 되므로
for i in range(1,11):
     result *= i
print(result)



