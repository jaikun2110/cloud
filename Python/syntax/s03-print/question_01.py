"""문제1
지갑에 아래와 같이 돈을 가지고 있다 총금액은?
각각의 금액을 변수에 넣어서 연산을 수행하여 총금액을 구하라
만원1개
1000원 3개
500원 5개
100원 9개
10원 6개
"""
#%%

a=10000*4
b=1000*3
c=500*5
d=100*9
e=10*6
result=0

result+=a+b+c+d+e
print("총합은:", result)

#%%
"""문제2
문제1에서 아래의 금액을 지출하고 남은 금액을 구하라

15000을 2번

"""
#%%

result=46460

buy=15000*2


result-=buy


print("남은 금액은", result)



#%%

"""문제3
한달급여400만원
분기별 보너스 월급여의 30% 지급됨
세금은 월급여의 3%
보너스 세금X
월세후의 수령액은?
연 총세금은?
세후 연수령액은?
"""

m=400
bon=m*(30/100)
t=m*(3/100)


print("보너스:", bon)
print("세금:", t)
print("월 세후 수령액:", m - t)
print("연 총세금:", t * 12)
print("세후 연 수령액:", ((m-t)*12)+(bon*12))


