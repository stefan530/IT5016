"""
Author: Stefan Davis Smith-Steunenberg

basic multiline strings
"""

name = "stefan"
age = 19
address = "121 Queen St"
mood = "happy"
tired = "tired"
info = f"""
Name: {name}
age: {age}
address: {address}
mood: {mood}
drowsy: {tired}

"""
print(info)