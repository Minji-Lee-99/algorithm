#신문 헤드라인
#알파벳 소문자를 대문자로!
#ord(): 문자를 아스키코드로, chr(): 아스키코드를 문자로

for char in input():
    if 97 <= ord(char) <= 122:
        print(chr(ord(char)-32), end='')
    else:
        print(char, end='')