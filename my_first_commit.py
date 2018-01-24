# print('lol fuck you nigga \"i\'m in love sucking dicks\"') #экранирование
# myscore = 1000
# message = 'Мой счет: %s очков'
# print(message % myscore)

# first_list = [1,2,3]
# second_list = [4,5,6,7,8,9,10,11,12,13,14,15]
#
# second_list[-5:-2] = [0,0,0]
# del second_list[-2:]
# a='fuck the duck'
# second_list.append(a)
# print(second_list)

# my_fav_gaems = {'dick': 'cock', 'fuck': 'suck'}
# print(my_fav_gaems['dick'])
#-------------creation of 2d array
# # Create baseball, a list of lists
# baseball = [[180, 78.4],
#             [215, 102.7],
#             [210, 98.5],
#             [188, 75.2]]
# # Import numpy
# import numpy as np
#
# # Create a 2D numpy array from baseball: np_baseball
# np_baseball = np.array(baseball)
#
# # Print out the type of np_baseball
# print(type(np_baseball))
#
# # Print out the shape of np_baseball
# print(np_baseball.shape)
#-----------------printing the shape of 2d array
# # baseball is available as a regular list of lists
#
# # Import numpy package
# import numpy as np
#
# # Create a 2D numpy array from baseball: np_baseball
# np_baseball = np.array(baseball)
#
# # Print out the shape of np_baseball
# print(np_baseball.shape)

# a = 12
# b = 6
#
# pryamougolnik = a * b
#
# def gcdIter(a, b):
#
#     delitel  =  b**2
#     print('Ploshad` ravna: ', pryamougolnik)
#
#     test_value = pryamougolnik - delitel
#
#     while test_value != 0:
#         print('ostatok: ', test_value)
#         gcdIter(a,b)
#     return test_value
#
# print(gcdIter(a,b))
#------------Recursive way to find greatest common diviser
# def gcdRecur(a,b):
#     if b == 0:
#         return a
#     else:
#         while b == 0:
#             return a
#         else:
#             return gcdRecur(b, a%b)
#####################looking for a char in an alphabetically sorted string###############
# def isIn(char, aStr):
#     if aStr == '':
#         return False
#     if len(aStr) == 1:
#         if char == aStr:
#             return True
#         else:
#             return False
#
#     middle_char_index = int(len(aStr) / 2)
#     middle_char = aStr[middle_char_index]
#
#     if char == middle_char:
#         return True
#     if char != middle_char and char < middle_char:
#         return isIn(char, aStr[:middle_char_index])
#     if char != middle_char and char > middle_char:
#         return isIn(char, aStr[middle_char_index:])
#
# print(isIn('d', 'adrtuy'))
########################################polysum#####################################
# from math import *
# '''
# Write a function called 'polysum' that takes 2 arguments, 'n' (a number of sides) and 's' (a lenght).
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places.
# '''
# def polysum(n, s):
#
#     po1ygon_area = ((0.25 * n) * (s ** 2)) / (tan(pi / n)) #The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
#     polygon_perimeter = n * s                              #The perimeter of a polygon is: length of the boundary of the polygon
#     result = po1ygon_area + polygon_perimeter ** 2         #This variable should sum the area and square of the perimeter of the regular polygon.
#     return round(result, 4)                                # The function returns the sum, rounded to 4 decimal places
######################################################################################+
total_debt = 5000

month = 0
min_payment = total_debt / 100 * 2
annual_interest_rate = 0.18


def calc_debt(total_debt, month, min_payment):
    month = 0
    payed = 0
    print('initial debt: ', total_debt)
    print('minimal payment: ', min_payment)
    print('________________________________')

    if month == 0:
        print('initial debt: ', total_debt)
        total_debt -= min_payment
        interest = (annual_interest_rate / 12.0 * total_debt)
        print('month: ', month)
        print('unpaid balance: ', total_debt)
        print('minimal payment: ', min_payment)
        print('interest: ', interest)
        print('________________________________')
        month += 1
        payed += min_payment



    while month < 12 and month != 12:
        total_debt += interest
        min_payment = round((total_debt / 100 * 2), 2)
        print('month: ', month)
        print('debt: ', total_debt)
        print('minimal payment: ', min_payment)



        total_debt = round((total_debt - min_payment), 2)
        print('debt: ', total_debt)
        interest = round((annual_interest_rate / 12.0 * total_debt), 2)
        print('interest: ', interest)

        print('________________________________')
        month += 1
        payed += min_payment
        print('lol')


    if month == 12:
        return round((total_debt + interest), 2), payed

print(calc_debt(total_debt, month, min_payment))