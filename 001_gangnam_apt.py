# # 처음에 원하는 가격 출력
# print(270000)
#
# # 내 월급도 출력
# print(400)
#
# # 사칙연산
# print(400 + 400) # 두달치모았을때
# print(400 - 150) # 차할부냈을때
# print(400*2) # 인센티브 탓을때
# print(400 - (400 / 10)) # 십일조낼때
#
# # 월급 더해서 얼마나걸리는지 볼까요
# print(270000 - (400 + 400 + 400 + 400 + 400 + 400))
#
# # 변수로 저장해서 써볼까요
# price = 270000
# salary = 400
# price = price - salary
# price = price - salary
# price = price - salary
# price = price - salary
# price = price - salary
# print(price)
#
# # 반복문을 써볼까요
# for i in range(12):
#     price = price - salary
# print(price)
#
# # 이런 타입의 반복문도 있어요
# while price > 0:
#     price = price - salary
# print(price)
#
# # 은행 이자
# account = 0
# interest = 0.02
# for i in range(24):
#     account = account + salary
#     account = account + account * interest
#
# # 월급이랑 가격을 입력받아볼까요
# price = input('가격 입력 ')
# salary = input('월급 입력 ')
#
# # 복권 만들기 랜덤 값 출력
# import random
# print(random.randint(1, 10))
# p = random.randint(1, 100)
# account = 0
# if p < 5:
#     account += 100000
# elif p < 30:
#     account += 50000
# elif p < 70:
#     account += 1000
# else:
#     account += 0
# print(account)

pay = input('월급을 입력해주세요 ')
print('당신의 연봉은', pay * 12, '입니다')


# import random
#
# apt = 27 * 100000000
# print('내가 가지고 싶은 아파트는 27억입니다')
# salary = float(input('연봉은?(?천만원) '))
# salary = salary * 10000000
# print('저축만으로는 ', apt/salary, '년 걸려요')
# interest = 0.02
# account = 0
# year = 0
# while account < apt:
#     account += salary
#     account += account * interest
#     year += 1
# print('은행 이자 복리 2% 로 하면 ', year, '년 걸려요')
#
# account = 0
# year = 0
# for i in range(100):
#     account += salary
#     for j in range(12):
#         account += random.randint(50 * 10000, 100 * 10000)
#     year += 1
#     if account >= apt:
#         break
# print('복권을 하게 되면 ', year, '년 걸려요')
