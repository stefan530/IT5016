"""
Bmi function

Author Stefan Davis Smith Steunenberg

"""
def get_bmi():
 weight = float(input("Enter your weight in(kg): "))
 height = float(input("Enter your height in(cm): "))

 height_in_centimeters = height / 100


 bmi = weight / (height_in_centimeters * height_in_centimeters)

 return bmi
print("Your Total BMI Is",get_bmi())
