# 문자열 포맷팅(String Formatting)
# 문자열 포맷 코드
# %s : 문자열(string)
# %c : 문자(character)
# %d : 정수(10진수, decimal)
# %f : 실수(float)
# %o : 8진수(octal)
# %x : 16진수(hexa-decimal)
# 
# 형식
# 포맷문자열 % 변수
# 포맷문자열 % (변수, ...)

#%%

n = 12345
s = "hello"
f = 0.12345

print("#정수")
print(f"정수 : ({n:>10})")
print(f"정수 : ({n:<10})")
print(f"정수 : ({n:>10d})")
print(f"정수 : ({n:^10})")

print("#실수")
print(f"실수 : ({f:>10})")
print(f"실수 : ({f:<10})")
print(f"실수 : ({f:<10.3})")
print(f"실수 : ({f:>10.3})")
print(f"실수 : ({f:>10.3f})")
print(f"실수 : ({f:^10.3})")

print("#문자열")
print(f"문자 : ({s:>10})") # 오른쪽 정렬
print(f"문자 : ({s:<10})") # 왼쪽 정렬
print(f"문자 : ({s:^10})") # 가운데 정렬

#%%

print("정수 : ({0:^10})".format(n)) # 가운데 정렬
print("실수 : ({0:^10})".format(f)) # 가운데 정렬
print("문자 : ({0:^10})".format(s)) # 가운데 정렬
print("전체 : ({0:^10})({1:^10})({2:^10})".format(n, f, s)) # 가운데 정렬

# 인자의 순번을 생략
print("전체 : ({:^10})({:^10})({:^10})".format(n, f, s)) # 가운데 정렬
print("전체 : ({})({})({})".format(n, f, s)) # 가운데 정렬
print(f"전체 : ({n})({f})({s})") # 가운데 정렬

#%%

# 가변처리(동적처리)
# 고객정보 처리
name = "홍길동"
age = 34

msg = "고객님의 이름은 {0}이며 나이는 {1}입니다.".format(name, age)
print(msg)

fmt = "고객님의 이름은 {0}이며 나이는 {1}입니다."
print(fmt.format(name, age))






