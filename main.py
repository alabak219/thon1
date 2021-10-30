import datetime

def feature1():
    print("feature1")



now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

import turtle

skk = turtle.Turtle()

for i in range(4):
    skk.forward(50)
    skk.right(90)

turtle.done()

import calendar

yy = 2021
mm = 12

print(calendar.month(yy, mm))

import sys

n = len(sys.argv)
print("Total arguments passed:", n)

print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

Sum = 0

for i in range(1, n):
    Sum += int(sys.argv[i])

print("\n\nResult:", Sum)

sentence = input("Enter a Sentence: ").lower()
words = sentence.split()

for i, word in enumerate(words):
    "if first letter is a vowel"
    if word[0] in 'aeiou':
        words[i] = words[i]+ "ay"
    else:
        "else get vowel position and postfic all the consonants present before that vowel to the end of work along with ay "
        has_vowel = False

        for j, letter in enumerate(word):
            if letter in 'aeiou':
                words[i] = word[j:] + word[:j] + "ay"
                has_vowel = True
                break

        if(has_vowel == False):
            words[i] = words[i]+ "ay"
    pig_latin = ' '.join(words)
    print("Pig Latin: ",pig_latin)





