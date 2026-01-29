def average(list):
    total_avg = 0
    for n in list:
        total_avg = total_avg + n

    average1 = total_avg / len(list)
    return average1

def result(avg, leng):
    if leng > avg:
        print(f"The length of the word '{word}' is greater than the average")
    elif leng < avg:
        print(f"The length of the word '{word}' is less than average")
    else:
        print("The length of the word and the average are equal")

word = input("Enter a word --> ")
length = len(word)

num = []
for i in range(length):
    num1 = int(input("Enter a number -->"))
    num.append(num1)

avrg = average(num)

print(num)
print(f'The length of the word is {length}')
print(f'The average of the numbers is {avrg}')
result(avrg, length)