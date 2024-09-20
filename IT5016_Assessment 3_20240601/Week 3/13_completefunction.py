"""
Author: Stefan Davis Smith-Steunenberg

basic definitions showing how to use if statment to see if
group size is greater then 14, if group size is greater then 14
give a 10% discount the way we complete this is completed
by using the variable group rate so only 90% is charged i think?

definitions are ignored untill main has been triggerd
"""
def get_price(child, adult):
    child_price = 10
    adult_price = 25
    group_size = 14
    group_rate = 0.9

    cost = (child * child_price + adult * adult_price)
    
    # putting value of child + adult into a variable called 
    # group size then making the cost equal the cost with 
    # group rate then returning the new cost because the if
    #statement has been triggerd 
    #
    if child + adult > group_size:
       cost = cost * group_rate
    return cost

def main():
    num_child = int(input("Enter the number of children: "))
    num_adult = int(input("Enter the number of adults: "))
    cost = get_price(num_child,num_adult)
    print("The cost of your ticket is: $" + str(cost))

main()
