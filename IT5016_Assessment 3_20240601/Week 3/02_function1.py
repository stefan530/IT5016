"""
Basic input functions

Author Stefan Davis Smith Steunenberg

"""
def function1 (n1,n2,n3): 
    sum = n1 + n2 + n3
    minimun = min(n1,n2,n3)
    return sum - minimun

n1 = int(input("Number 1:"))
n2 = int(input("Number 2:"))
n3 = int(input("Number 3:"))
print(function1(n1,n2,n3))

#print("1.", function1(1, 2, 3))
#print("1.", function1(11, 12, 3))
#print("1.", function1(6, 2, 5))
