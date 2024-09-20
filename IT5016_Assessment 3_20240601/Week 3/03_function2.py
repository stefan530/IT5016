"""
Basic input functions extended

Author Stefan Davis Smith Steunenberg

"""

def function2(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    shorter_length = min(len1,len2)
    return shorter_length

word1 = input("Enter Word1:")
word1 = input("Enter Word2:")
print(function2(word1,word2=""))


print("1.", function2("Sarthak","Tania"))
print("2.", function2("Robin","Stefan"))
print("3.", function2("Muhammad","Badal"))
print("4.", function2("Dylan","Tamara"))
print("5.", function2("Tanya","Ashleigh"))