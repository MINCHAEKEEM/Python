# 기절초풍, 멋있는, 재미있는
# 도전적인, 노란색의, 바보같은
# 돌고래, 개발자, 오랑우탄

print("닉네임을 뽑아봅시다!")

import random

def get_random_nickname():
    first_list = ["기절초풍 ", "멋있는 ", "재미있는 "]
    second_list = ["도전적인 ", "노란색의 ", "바보같은 "]
    third_list = ["돌고래", "개발자", "오랑우탄"]
    f = random.choice(first_list)
    s = random.choice(second_list)
    t = random.choice(third_list)
    result = f + s + t
    return result

my_nickname = get_random_nickname()
print(my_nickname)
