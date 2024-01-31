# 리스트(list)
# 여러 형태의 자료들의 연속된 모임
# 변경가능(mutable)

#%%

ml = ['홍길동', 34, 89.5, False]
print(ml)

#%%

# 성적처리: 이름, 국어, 영어, 수학
s1 = ['우등생', 100, 100, 100, 0, 0.0]
s2 = ['이등생', 90, 90, 95, 0, 0.0]
s3 = ['삼등생', 89, 88, 77, 0, 0.0]

# 총점
s1[-2] = s1[1] + s1[2] + s1[3]
s2[-2] = s2[1] + s2[2] + s2[3]
s3[-2] = s3[1] + s3[2] + s3[3]

# 평균
s1[-1] = s1[-2] / 3.0
s2[-1] = s2[-2] / 3.0
s3[-1] = s3[-2] / 3.0

print(s1)
print(s2)
print(s3)

#%%
hd = ['이름', '국어', '영어', '수학', '총점', '평균']
print(f"{hd[0]} : {s1[0]}")
print(f"{hd[1]} : {s1[1]}")
print(f"{hd[2]} : {s1[2]}")
print(f"{hd[3]} : {s1[3]}")
print(f"{hd[4]} : {s1[4]}")
print(f"{hd[5]} : {s1[5]}")
