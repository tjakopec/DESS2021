

def input_value(message):
    while True:
            name = input(message)
            if name.strip()=='':
                print('Input required')
            elif name.isalpha():
                return name
            else:
                print('Input can only contains letters')


def read_names():
    while True:
        name1=input_value('Unput your name: ')
        name2=input_value('Input name of you sympathy: ')
        if name1!=name2:
            return {'name1':name1, 'name2':name2}
        else:
            print('Names are the same!')


def sort_letters(names):
    list_of_letters = []
    for letter in names['name1'].lower():
        list_of_letters.append(letter)
    for letter in names['name2'].lower():
        list_of_letters.append(letter)
    list_of_letters.sort()
    return list_of_letters


def count_letters(list_of_letters):
    dictionary = dict((i, list_of_letters.count(i)) for i in list_of_letters)
    numbers=[]
    for letter in dictionary:
        numbers.append(dictionary[letter])
    return numbers


def calculate_percentage(numbers):
    number = int(''.join(str(b) for b in numbers))
    if number < 100:
        return number
    else:
        new_numbers=[]
        if len(numbers) % 2 == 0:
            for i in range(0,len(numbers),2):
                sum_of_numbers = numbers[i] + numbers[i+1]
                if sum_of_numbers >= 10:
                    sum_of_numbers=sum_of_numbers % 10
                new_numbers.append(sum_of_numbers)
        else:
            for i in range(0,len(numbers)-1,2):
                sum_of_numbers = numbers[i] + numbers[i+1]
                if sum_of_numbers >= 10:
                    sum_of_numbers=sum_of_numbers % 10
                new_numbers.append(sum_of_numbers)
            new_numbers.append(numbers[-1])
        return calculate_percentage(new_numbers)



def lc():
    dictionary_of_names = read_names()
    sorted_letters = sort_letters(dictionary_of_names)
    counted_letters=count_letters(sorted_letters)
    percentage = calculate_percentage(counted_letters)
    print (dictionary_of_names['name1'],'and',
           dictionary_of_names['name2'],'are in love',
           percentage,'%')

lc()





