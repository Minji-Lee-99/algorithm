max_cnt = 0
max_price = 0


def dfs(d, discounts, emoticons, users):
    global max_cnt, max_price  # 이모티콘 플러스 가입자수, 이모티콘 판매액
    if d == len(emoticons):
        cnt = 0    # 주어진 할인율에서 계산된 이모티콘 가입자수
        price = 0   # 주어진 할인율에서 계산된 이모티콘 판매액
        for user in users:
            purchase_price = 0
            for i in range(len(emoticons)):
                if discounts[i] >= user[0]:  # 사용자의 구매 기준에 부합하는지 확인
                    purchase_price += emoticons[i] * (1 - discounts[i] / 100)   # 할인액 계산해서 적용
            if purchase_price >= user[1]:  # 만약 사용자가 구매한 금액이 사용자의 이모티콘 플러스 가입 기준을 넘으면 이모티콘 플러스 가입
                cnt += 1
            else:  # 넘지 못하면 이모티콘만 구매
                price += purchase_price
        if cnt > max_cnt:  # 계산한 이모티콘 가입자수와 이모티콘 판매액을 갱신
            max_cnt = cnt
            max_price = price
        if cnt == max_cnt and price > max_price:
            max_price = price
        return
    for i in range(10, 41, 10):  # 각 이모티콘마다 10~40사이의 할인율 할당
        discounts[d] = i
        dfs(d + 1, discounts, emoticons, users)


def solution(users, emoticons):
    discounts = [0 for i in range(len(emoticons))]
    dfs(0, discounts, emoticons, users)
    answer = [max_cnt, int(max_price)]
    return answer


# users = [[40, 10000], [25, 10000]]
# emoticons = [7000, 9000]

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]

print(solution(users, emoticons))
