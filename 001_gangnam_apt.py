import random

apt = 27 * 100000000
print('내가 가지고 싶은 아파트는 27억입니다')
# salary = float(input('연봉은? '))
# salary = salary * 10000000
salary = 5 * 10000000
print('저축만으로는 ', apt/salary, '년 걸려요')
interest = 0.02
account = 0
year = 0
while account < apt:
    account += salary
    account += account * interest
    year += 1
print('은행 이자 복리 2% 로 하면 ', year, '년 걸려요')

account = 0
year = 0
for i in range(100):
    account += salary
    for j in range(12):
        account += random.randint(50 * 10000, 100 * 10000)
    year += 1
    if account >= apt:
        break
print('부업을 하게 되면 ', year, '년 걸려요')
