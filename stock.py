prices = [100, 110, 90, 80, 120, 150, 120, 190]

# 순회 출력 한번 해주고
for p in prices:
    print(p)

# 추가 삭제 가능하다는거 그냥 보여만주고

# https://finance.yahoo.com/quote/MSFT/history?ltr=1
# 파일 가져온거 읽고 쓰기 (plain)
file = open('../../PycharmProjects/untitled/MSFT.csv')
print(file.readlines())
file.close()
# 실제 데이터 가져와서 csv 읽고 쓰기
import csv
# 2차원 배열에 대한 개념 with as
with open('../../PycharmProjects/untitled/MSFT.csv') as file:
    reader = csv.reader(file)
    for r in reader:
        print(r)
# dictionary...
rows = []
with open('../../PycharmProjects/untitled/MSFT.csv') as file:
    reader = csv.DictReader(file)
    for r in reader:
        rows.append(r)

print(rows[0]['Date'])

# 그래프 그리기
dates = []
prices = []
for r in rows:
    dates.append(r['Date'])
    prices.append(float(r['Close']))
import pygal
chart = pygal.Line()
chart.title = '주식비서'
chart.x_labels = dates
chart.add('prices', prices)

# 상승폭 그리기
changes = [0] # 이부분 하나 넣어줘야하는것
for i in range(1, len(prices)): # 인덱스 참고 하는거 한번 보여주고
    print(prices[i], prices[i] - prices[i-1])
    changes.append(prices[i] - prices[i-1])
chart.add('changes', changes)

# chart.render_in_browser()

# 상한가 하한가
top = 0 # 초기값의 중요성
for p in prices:
    if top < p:
        top = p
print(top)

bottom = 0 # 여기도 마찬가지
bottom = min(prices)
print(bottom)


# 너무 기간이 길어
# 왔다리갔다리 재밌어보이는 2019.08~2019.10 을 뽑아옵시다
interest_dates = []
interest_prices = []
for r in rows:
    if '2019-08-01' <= r['Date'] <= '2019-10-31':
        interest_prices.append(float(r['Close']))
        interest_dates.append(r['Date'])
    else:
        interest_prices.append(None)
        interest_dates.append(None)
# 잘 뽑혔는지 개수로 확인해주고
print(len(prices))
print(len(interest_prices))

chart.title = '2019-08-01 ~ 2019-10-31'
chart.x_labels = interest_dates
chart.add('prices', interest_prices)

chart.render_in_browser()
