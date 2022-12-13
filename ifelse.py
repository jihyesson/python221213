#ifelse.py

score=int(input("점수를 입력:"))

if 90 <= score <= 100 :
    grade = "A"
elif 80 <= score < 90 :
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
else:
    grade = "F"

print("귀하의 등급은", grade, "입니다.")

x = int(input("숫자를 입력해주세요."))

if x/2 == %0