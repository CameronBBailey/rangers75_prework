#1
def hello_name(user_name):
    print('Hello ' + user_name + '!')

hello_name('Cameron')


# Question 2 print all odd numbers between 1 and 100

#odd100= [value for value in range(1,100,2)]
#print(odd100)

# Print first 100 odd numbers
#def first_100():
   # numbers = list(range(0,201))
   # for number in numbers:
       # if number % 2 != 0:
           # print(number)

#first_100()
#good practice to always right in a function


#Please write a Python function, max_num_in_list to return the max numbers in a given list.
#def max_num(a_list):
    #max_value = max(a_list)
    # return max_value

#print(max_num([2,3,5,8,9]))

# Question 4 Write a function to return if the given year is a leap year

def is_leap_year(a_year):
   if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 !=0):
        print(True)
   else:
        print(False) 
is_leap_year(2019)
is_leap_year(2028)
is_leap_year(2100)


#5 Write a function to check to see if all numbers in list are consecutive
def is_consecutive(a_list):
    """Figure out if all numbers in a list are consecutive numbers"""
    return sorted(a_list) == list (range(min(a_list),max(a_list)+1))

print(is_consecutive([1,2,3,4,5,7]))
print(is_consecutive([1,2,3,4,5,6]))

def is_consecutive2(a_list):
    i = 0
    status = True
    while i < len(a_list) -1:
        if a_list[i] + 1 == a_list[i+1]:
            i+=1
        else:
            status = False
            break
    print(status)

    is_consecutive2([2,3,4,5])
    is_consecutive2([1,4,3,7])