"""
리스트 슬라이싱
리스트의 자료를 꺼내서 새로운 리스트를 생성
리스트[시작위치:종료위치]

시작위치:0부터

종료위치:종료위치:-1까지

"""

lt=[1,2,3,4,5,6]

print(lt[2:4])

#%%

print("리스트의 마지막",lt[-1])

print("리스트의 3부터 마지막 전까지",lt[2:-1])

#%%

ll=lt[-1]#인덱스 참조 int 타입

print(ll,type(ll))

lss=lt[-1:]

print(lss,type(lss))
