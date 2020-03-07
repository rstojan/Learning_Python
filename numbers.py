size = 5

def get_numbers(num):
    numbers = []
    user_input = input('Enter %s integers:\n' % num)

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    print('Numbers:', end=" ")
    for x in range(size):
        print (numbers[x], end=" ")
    print()

def print_odd_numbers(numbers):
    print('Odd numbers:', end=" ")
    for odd in numbers:
        if odd % 2 != 0:
            print(odd, end=" ")
    print()

def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:', end=" ")
    for negative in numbers:
        if negative < 0:
            print(negative, end=" ")
    print()

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)
