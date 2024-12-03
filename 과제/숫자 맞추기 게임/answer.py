import random  # import random 어서오시고~

print("어서오세요. 이것은 '랜덤 숫자 맞추기 게임' 입니다.")

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 다른분들은 randint 많이 쓰시던데 난 걍 choice 를 선택함
answer = random.choice(items)  # choice 는 리스트, 튜플, 문자열 같은데서만 쓸 수 있음다


while True:  # 애증의 무한동력 반복문 ㅋ
    x = int(input("이 숫자는 무엇일까요?"))
    if answer == x:
        print("흠, 정답을 입력하셔서 게임을 종료합니다.")
        break
    elif x < answer:
        print("숫자가 작습니다. 숫자를 조금 올려보는건 어떨까요?")
       # x = int(input("숫자를 조금 올려보는건 어떨까요?")) << 오답
    elif x > answer:
        print("숫자를 조금 낮춰보는건 어떨까요?")
       # int(input("숫자를 조금 낮춰보는건 어떨까요?")) << 오답
    else:
        print("후후후. 숫자를 좀 더 신중하게 생각해보고 다시 도전하세요.")
