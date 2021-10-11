#math모듈
import math

math.log()
math.cos()

#random 모듈
import random
# 랜덤한 정수 1 <= n <= 20 
print(random.randint(1, 20))

# 랜덤한 소수 0 <= n <= 1
print(random.uniform(0, 1))

#datetime 모듈
import datetime

# 현재 시간과 날짜
today = datetime.datetime.now()
print(today)

# 출력값을 "요일, 월 일 연도"로 포매팅
print(today.strftime("%A, %B %dth %Y"))

# 특정 시간과 날짜
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)

# 두 datetime의 차이
print(today - pi_day)

#os모듈
import os

# 현재 어떤 계정으로 로그인 돼있는지 확인
print(os.getlogin())

# 현재 파일의 디렉토리 확인 
print(os.getcwd())

# 현재 프로세스 ID 확인 
print(os.getpid())