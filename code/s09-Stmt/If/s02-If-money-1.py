# 조건문 : If
# 크기비교의 결과 bool
# 크다 : a > b
# 작다 : a < b
# 크거나 같다: a >= b
# 작거나 같다: a <= b
# 
# 논리연산자: 
# 논리합(or): a or b, a, b중 하나만 참이면 True
# 논리곱(and): a and b, a, b중 모두 참이어야 True
# 논리부정(not): not a, a가 참이면 False, a 거짓이면 True
#
# [문제]
# 가진 돈을 가지고 음료수를 구매하는데
# 돈에 따라서 가장 비싼 음료를 구매한다.
# 커피: 5000
# 탄산: 3000
# 생수: 1000
# 1000원 미만이면 정수기 물을 마신다.

money = int(input("가진 돈이 얼마인가? "))
print(type(money), money)

print(f"당신이 가진 돈은 ({money})원 입니다.")

#%%
# 값이 큰 순서로 조건을 처리해야 한다.

if money >= 5000:
    print("당신이 가진 돈으로 (커피)를 살수 있습니다.")
elif money >= 3000:
    print("당신이 가진 돈으로 (탄산)음료를 살수 있습니다.")
elif money >= 1000:
    print("당신이 가진 돈으로 (생수)를 살수 있습니다.")
else:
    print("그냥 정수기 물을 드세요.")
    
    
