"""
리스트 더하기

여러개의 리스트를 연결해서 하나로 만듬


"""

a=[1,3,5]
b=[2,4,6]
c=a+b
print(c)

c[0] = 0

print(a)
print(b)
print(c)#c의 리스트만 변경됨

#%%

"""
리스트 곱하기
리스트 주어진 숫자만금 반복해서 더래서 붙임
"""



a=[1,3,5]
b=3
c=a * b
print(c)