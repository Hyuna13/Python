#정규식 기본
import re
#cafe,cave,care...

p = re.compile("ca.e")#.하나의 문자 ^문자열시작 $문자열끝
#print(m.group())#매치가 안되면에러
def print_match(m):
  if m:
    print(m.group()) #일치하는 문자열 반환
    print(m.string) #입력받은 문자열
    print(m.start()) #일치하는 문자열 시작 index
    print(m.end()) #일치하는 문자열 끝 index
    print(m.span()) # 시작/끝 index
  else:
    print("ERROR")
 
m = p.match("case") #match 주어질문자열 처음부터 확인
print_match(m)
m = p.search("careless") #match 주어질문자열 중에 확인
print_match(m)
lst = p.findall("careless")#일치하는것 리스트형태로 반환
print(lst)
