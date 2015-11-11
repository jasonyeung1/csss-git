'''
An exercise to practice collaboration using git and Github.
Author: Bosco Noronha (nbosco)
Date: 25th Oct 2015
'''
import random


'''
Purpose of the function:
Given a array of integers, return the length of the array.
Eg. Input: [1, 2, 3, 4, 5, 6, 7, 8]
    Output: 8
'''
def amountInArray(array):
    return len(array)


'''
Purpose of the function:
Given a array of integers, return the sum of all the integers.
Eg. Input: [1, 2, 3, 4, 5, 6, 7, 8]
    Output:
'''
def sumOfArray(array):
    total = 0
    for val in array:
        total += int(val)
    return total

'''
Purpose of the function:
Given a array of integers, return the array in reverse order.
Eg. Input: [1, 2, 3, 4, 5, 6, 7, 8]
    Output:[8, 7, 6, 5, 4, 3, 2, 1]
'''
def reverseArray(array):
    return list(reversed(array))
        



'''
Purpose of the function:
Given a array of integers, return the array shuffled.
Eg. Input: [1, 2, 3, 4, 5, 6, 7, 8]
    Output:[8, 2, 1, 5, 7, 3, 4, 6]
'''
def shuffleArray(array):
    done = False
    new_array = []
    while (not done):
        rand = random.randint(0, len(array))
        if (not rand in array):
            new_array.append(rand)
            if (len(new_array) == len(array)):
                done = True
    return new_array
        




#MAIN
array = [1, 2, 3, 4, 5, 6, 7, 8]

print(amountInArray(array))
print(sumOfArray(array))
print(reverseArray(array))
print(shuffleArray(array))
