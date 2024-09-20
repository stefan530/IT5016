"""
Basic word length function

Author Stefan Davis Smith Steunenberg

"""

def function3(word):
    first = word[0]
    last = word[len(word) -1]
    combined = last + first
    return combined.upper()


print("1.", function3 ("Daphe"))
print("2.", function3 ("George"))
print("3.", function3 ("Jessica"))
print("4.", function3 ("Stefan"))
print("5.", function3 ("Jun"))
print("6.", function3 ("Nafets"))