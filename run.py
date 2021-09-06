import area

print(area.circle(2))
print(area.square(2))
print(area.PI)

#부분만 가져올때

from area import circle
print(circle(2))

#여러개 
from area import circle, square
print(circle(2))

#모든 내용
from area import *

#이름 바꾸기
import area as ar
print(ar.circle(3))
