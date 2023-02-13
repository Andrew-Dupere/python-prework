#Question 1
def hello_USERNAME():
    user_name = input('What is your username?')
    print(f'Hello! {user_name}')

#Question 2
def first_odds():
    for num in range(1,101):
        if num %2 != 0:
            print(num)


#Question 3

def max_num_in_list(a_list):
        return max(a_list)

#Question 4

def is_leap_year(a_year):
    if (a_year)/4 %2 == 0 and (a_year)/100 %2 != 0:
        return True
    elif (a_year)/400 %2 == 0:
        return True
    else:
        return False


#Question 5

def is_consecutive(a_list):
    checkList = list(range(a_list[0],a_list[-1]+1))
    
    
    return a_list == checkList
