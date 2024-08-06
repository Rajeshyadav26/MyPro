# wap to check the prime number or not
num = 23
# define flag variable
flag = False
# check if the number is less than or equal to 1
if num < 1:
    print(num, "is not a prime number")
    # if the number is greter than 1
elif num > 1:
    # iterate through number from 2 num - 1
    for i in range(2, num):
        # if the number is divisible by 2 to num -1
        if num % i == 0:
            # set the flag = True
            flag = True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# wap to print the prime numbers 1 to 100
op = []
# iterate through numbers from 2 to 100 using the variable i
for i in range(2, 101):
    # for each i iterate through numbers from 2 to 100 using the variable j
    for j in range(2, 101):
        # if i is divisible by j without leaving a remainder if it is break out of the innner loop
        # after the inner loop check if i is equal to j
        # and append to the i
        if i % j == 0:
            break
    if i == j:
        op.append(i)
print(op)
# wap to print the fibonacci series
a, b = 0, 1  # intialize two variables a and b
op = [a, b]
for i in range(2, 20):
    # calculate the fibonacci series
    c = a + b
    # update the values for the next iteration
    a = b
    b = c
    op.append(c)
print(op)

# wap to check the armstrong number or not


def armstrong_number(num):

    # intialize one variable temp with the value of num to store the original number
    temp = num
    # find the number of digits in num by converting to string and finding it is length to store this in n
    n = len(str(num))
    # intialize one variable add to 0 This will be used to collect the sum of the digits raised to the power of n
    add = 0
    while num > 0:
        # extract the last digit of num using the modulous operator and store it in a variable called digit
        digit = num % 10
        # Add the cube of digit to add
        add += digit ** 3
        # remove the last digit from num using the integer division
        num = num // 10
    # after the loop if the original number is equal to add

    if temp == add:
        print("armstrong number")
    else:
        print("not an armstrong number")


armstrong_number(153)

# wap to check the palindrome number or not
# define a variable num
num = "121"
# convert the string num into a list of numbers and i have assigned one variable to n
n = list(num)
# if the list of n is equal to reverse
#
if list(num) == n[::-1]:
    print("is a palindrome number")
else:
    print("is not a palindrome number")

# wap to print the factorial of a number

num = 5
fact = 1  # it will store the factorial value
if num < 0:
    print("factorial does not exist")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fact = fact * i  # multiply fact with the current value of the loop variable i
    print(f'factorial of {num} is {fact}')


"""
what is mean by pass statement
The pass statement in python is a placeholder that does nothing when executed.
It is used as syntentical pattenrn but no action is necessary"""


def check_leap_year(year):
    # check if the year is divisible by 400 if so print that it is a leap year
    # if the year is not divisible by 400 and then check
    if year % 400 == 0:
        print(year, "is a leap year")

    # if the  is diviyearsible by 4 and not divisible by 100 if so print that it is a leap year
    elif year % 4 == 0 and year % 100 != 0:
        print(year, "is a leap year")
    # if the year does not satisfy any of the above conditions print that it is not a leap year
    else:
        print(year, "is not a leap year")


check_leap_year(2020)


s = "123"
s1 = "abcde"
op = ""
for i in range(len(s1)):
    # check if i is less than lenghth of the string s
    # if true concatenate the characters at index of i of s and s1 to the output
    # if false concatenate the characters at index of i of s1 to the output
    if i < len(s):
        op += s[i] + s1[i]
    else:
        op += s1[i]
print(op)


s = "aaaabbbbcccdddeee"
op = ""
count = 1  # to count the occurance of each character
for i in range(1, len(s)):
    # compare each character with previous one
    # if the characters are the same, increment the count
    # if the characters are different
    if s[i] == s[i-1]:

        count += 1
    else:
        # append the count and add the previous character to op
        op += str(count) + s[i-1]
        # reset the count to 1
        count = 1
# after the loop append the count and the last character to op
op += str(count) + s[i-1]
print(op)


s = "4a4b3c3d3e"
# intialize an empty string to store the output
op = ""
for i in range(0, len(s), 2):
    # extract the number and convert it to an integer
    num = int(s[i])
    # extract the character
    char = s[i + 1]
    # multiply the character by num and concantate to the result
    op += num * char
print(op)


data = """name age salary location
yeswanth  23  34598  bangalore
bharath   20  12330  chennai
akhil     26  34598  bangalore
hari      27  12330  chennai"""

# split the lines and remove the header
line = data.splitlines()[1:]
# initialize an empty dictionary to store the parsed data
d = {}

# iterate through each line
for lines in line:
    # split the line into individual fields
    name, age, salary, location = lines.split()

    # create a nested dictionary for each individual fields
    d[name] = {"age": int(age), "salary": int(salary), "location": location}
print(d)


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = []
for i in range(len(l1)):
    # for each index i retrive the elements from l1 and l2
    # perform this addition of those elements and store the result in variable add
    add = l1[i] + l2[i]
    l3.append(add)
print(l3)


l = [1, 2, 2, 3, 5, 5, 6, 9, 3, 1, 2]
# I have initialized an empty dictionary where we will store the frequncy of each element
d = {}
# loop iterates throuh each element i in the l
for i in l:
    # count the frequncy of each element
    # for each element i returns the number of times i appears in the list
    # this count is assigned as the values to the key i in the dictionary
    d[i] = l.count(i)
print(d)

l = [23, 45, 475, 30033, 56, 77, 99, 12, 124, 13400]
maxx = l[0]  # intialze the variable maxx with the first element of the l
for i in l[1:]:
    # if the current element is greater than maxx
    if maxx < i:
        # if it is true updated to maxx
        maxx = i
print(maxx)

# wap to find the maximum number
s = "23, 45, 407, 79,46, 5"
# split the string into string number by using ,

# i have initalized maxx variable with the first element of the number
maxx = 0
for i in s.split(','):
    # if the current element is greater than maxx
    if maxx < int(i):
        # if it is true updated to maxx
        maxx = int(i)
print(maxx)

# wap to reverse the elements of the list
l = [3, 5, 7, 87, 34, 45]
# create an empty to store the reverse elements
op = []
for i in l:  # iterate through each element i in the list of l
    # I have inserted each element at the beginning of the list op by using the insert method with index 0
    op.insert(0, i)
print(op)


# wap to find the unique elements of the list
l = [2, 4, 3, 2, 3, 4, 7, 6, 9]
op = []
for i in l:  # iterate through each element i in the list l
    # if the element i is not alredy in the list
    if i not in op:
        # if true add i to the list
        op.append(i)
print(op)

# wap to print the vowels from the given string
s = "heEllo worAld"
op = []
for i in s:  # iterate through each character i in the string
    if i in "aeiouAEIOU":  # check if the cureent character is a vowel either upper case or lower case
        # if it is true add the vowel to the list
        op.append(i)
print(op)
