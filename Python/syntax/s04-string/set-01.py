"""
집합 자료형:set
합집합,교집합,여집합
셋(set)은 키(key)만 있는 딕셔너리(dict) 형태
문자열과 리스트와 다르게 순서가 없음
데이터를 넣은 순서를 보장하지 않음
집합 자료형은 True 와 False 와 같은 
bool자료형을 각각 1과 0과 같은값으로 인식함 


"""


s=set()

print(type(s),s)

#%%

s1 = {1,3,5,7,8}#중괄호로 선언하면 set 클래스로 저장됨

"""
리스트 타입은 l=[]로 빈 리스트 지정 가능하나
s={} 와 같이 컴파일시 딕셔너리타입으로 지정됨
s=set({}) 으로 빈 셋 지정 가능
"""

