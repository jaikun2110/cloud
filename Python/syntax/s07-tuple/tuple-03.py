
t=(1,2,3,4,5)

print(t[1:4])

t=t[1:4]
#슬라이싱 된 튜플 저장 가능
print(t)

#%%

t1=(1,3,5)
t2=(2,4,6)

t3=t1+t2#튜플 병합 가능
print(t3)

#%%

"""
아래 튜플 데이터에서 인덱스 2번의 데이터를 10으로 바꿔라

"""


tv = 10,
tx = 2
tp = (1,3,5,7,9)

tp = tp[0:1]+tv+tp[2:]

print(tp)