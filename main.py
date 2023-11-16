# csv 불러오기 위함
import pandas as pd

# numpy와 비슷함. 수식(다항함수 등)에 관한 라이브러리
from sympy import *

# 분수 정확히 표현(부동소수점 오류 피하기 위함)
from fractions import Fraction

# 데이터 불러오기
data = pd.read_csv("data.csv")

# a를 수식처리
a = Symbol("a")
res = []
for i, total in enumerate(data["total"]):
    diffr = total - 4407713  # 원래 값 - 4407713
    res.append(Fraction(0.1) * ((diffr - i * a) ** 2))  # 손실함수 각 항

loss_fn = simplify(sum(res))  # 손실함수
dda = diff(loss_fn, a)  # 손실함수 미분
min_a = float(solve(Eq(dda, 0))[0])  # E'(a)=0인 a값 찾고 이를 min_a에 넣기
print(min_a)  # 손실함수가 최소가 되는 a값
print(loss_fn.subs(a, min_a))  # 손실함수에 a=min_a를 넣기(최솟값)
