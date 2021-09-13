#파일 읽기
#r은 read의 약자, f에 저장
#data파일에있는 텍스트 읽기
with open('data/chicken.txt', 'r') as f:
  for line in f:
    print(line.strip())

# \n은엔터
#strip은 화이트 스페이스를 없애줌
#화이트스페이스란 "" "\t" "\n" 공백

a = "  abc  df".strip()
print(a)#앞뒤공백 날아감

#split
my_string = "1.2.3.4.5.6"
print(my_string.split(".")) #.을 기준으로 나눠서 리스트에 저장 #리스트는 모두 문자열

numbers = "   \t 1 \n 3 5 7".split()
print(numbers[0])


#평균매출구하기
with open('data/chicken.txt', 'r') as f:
    total_revenue = 0
    total_days = 0
    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1]) 
        total_revenue += revenue #매출
        total_days += 1 #기간
    print(total_revenue / total_days)
