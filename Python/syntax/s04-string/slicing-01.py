"""
문자열 슬라이싱(slicing)
특정한 범위를 지정해서 추출
추출된 문자열은 새로운 변수에 할당
마찬가지로 문자열이 추출되어도 문자열 변화X

변수 = 문자열[시작번호:종료번호] 로 사용함


"""


#%%
s='01234567'

si=s[0:4]
print(si)


#%%

se=s[3:4]
sa=s[:]
sy=s[4:]
sl=s[-1:]
print(se)#배열이 3이상 4미만인 것을 출력하므로 값은 3
print(sa)#배열 전체를 출력
print(sy)#4이상인 모든배열 출력
print(sl)#마지막 배열출력

#%%
