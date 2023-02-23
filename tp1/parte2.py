print("---------------- Ex 1 ----------------")
def reverse(s):
    return s[::-1]

name="hugo"
print(reverse(name))

print("\n---------------- Ex 2 ----------------")
def count_a(s):
    number = 0
    for letter in s:
        if letter.lower() in ["a"]:
            number +=1
    return number

second_name="baptistA"
print(count_a(second_name))

print("\n---------------- Ex 3 ----------------")
def count_vowels(s):
    number = 0
    for letter in s:
        if letter.lower() in ["a", "e", "i", "o", "u"]:
            number +=1
    return number

print(count_vowels(second_name))

print("\n---------------- Ex 4 ----------------")
def lowercase(s):
    return s.lower()

print(lowercase(second_name))

print("\n---------------- Ex 5 ----------------")
def uppercase(s):
    return s.upper()

print(uppercase(second_name))