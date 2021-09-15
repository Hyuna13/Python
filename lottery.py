#로또 번호 뽑기
from random import randint

def generate_numbers(n):
  numbers = []
  while len(numbers) < 6:
    num = randint(1, 45)
    if num not in numbers:
      numbers.append(num)
  return numbers


#당첨번호뽑기
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6] + winning_numbers[6:]) #sorted정렬

#겹치는 번호 개수
def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count

#당첨금 확인
def check(numbers, winning_numbers):
   count = count_matching_numbers(numbers, winning_numbers[:6])
   bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
  
   if count == 6:
       return 1000000000
   elif count == 5 and bonus_count == 1:
       return 50000000
   elif count == 5:
       return 1000000
   elif count == 4:
       return 50000
   elif count == 3:
       return 5000
   else:
       return 0

numbers_test = [2, 4, 11, 14, 25, 40]
winning_numbers_test = [1, 4, 10, 11, 34, 40, 25]

print(check(numbers_test, winning_numbers_test))