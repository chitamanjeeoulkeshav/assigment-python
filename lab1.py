upper = 0
lower = 0
digit = 0
specialcharacter = 0

sentence = input("Enter your sentence: ")

for x in sentence:
    if x.isalpha():
        if x.isupper():
            upper += 1

        else:
            lower += 1

    elif x.isdigit():
        digit += 1

    else:
        specialcharacter += 1

print('The number of Uppercase alphabets:', upper)
print('The number of Lowercase alphabets:', lower)
print('The number of digit:', digit)
print('The number of specialcharacter:', specialcharacter)