numbers = input("Enter numbers separated by a comma").split(',')
numberTuple = ()
for number in numbers:
    numbers[numbers.index(number)] = int(number)
    numberTuple= (*numberTuple, int(number))
print("List: ", numbers)
print("Tuple: ", numberTuple)