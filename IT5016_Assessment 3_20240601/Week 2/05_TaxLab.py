"""
lab 5
Author Stefan Davis Smith Steunenberg

"""


salary = 54000
no_tax_boundary = 14000
rate1_boundary = 38000
rate1 = 0.24
rate2 = 0.34

taxable1 = rate1_boundary - no_tax_boundary
taxable2 = salary - rate1_boundary
tax1 = taxable1 * rate1
tax2 = taxable2 * rate2
total_tax = round(tax1 + tax2)
net_pay = salary - total_tax

print("Salary: $", salary, sep= "")
print("Amount to be taxed at:", rate1 * 100, "%: $", taxable1, sep="")
print("Tax at rate1: $", tax1, sep="")
print("Amount to be taxed at: ", rate2 * 100, "%: $", taxable2 , sep="")
print("Tax at rate2: $", tax2, sep="")
print("=" * 32)
print("Total tax: $", tax2, sep="")
print()
print("Net pay: $", net_pay, sep="")
print("=" * 32)
