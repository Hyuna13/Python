#파일 쓰기
#w는 writing을 의미
with open('new_file.txt', 'w') as f:
  f.write("Hello\n")
  f.write("my name is T")

#a는 append를 의미, 기존의 것에 덮어쓰기
with open('new_file.txt', 'a') as f:
  f.write("\nwelcome")

#단어장만들기
with open('vocabulary.txt', 'w') as f:
    while True:
        english = input('영어 단어를 입력하세요: ')    
        if english == 'q':
            break
        
        korean = input('한국어 뜻을 입력하세요: ')
        if korean == 'q':
            break
        
        f.write('{}: {}\n'.format(english, korean))

#단어 퀴즈
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english, korean = data[0], data[1]
        
        # 유저 입력값 받기
        guess = input("{}: ".format(korean))
        
        # 정답 확인하기
        if guess == english:
            print("정답입니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(english))
         
#업그레이드
import random

# 사전 만들기
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english, korean = data[0], data[1]
        vocab[english] = korean

# 목록 가져오기
keys = list(vocab.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아오기
    index = random.randint(0, len(keys) - 1)
    english = keys[index]
    korean = vocab[english]
    
    # 유저 입력값 받기
    guess = input("{}: ".format(korean))
    
    # 프로그램 끝내기
    if guess == 'q':
        break
    
    # 정답 확인하기
    if guess == english:
        print("정답입니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(english))