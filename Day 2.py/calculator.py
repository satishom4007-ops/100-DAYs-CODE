# sum = 0
# while (True):
#  product = input ("Please Enter THe Product You Just bought: ")
#  price = input("Please Enter The Price Of The Product: ")

#  sum = sum + int(price)
#  print (f"Your Current total basket cost : {sum}")

# recipt =[f"{product}: {price}"]
# print (recipt)
# #  if (product == "q")

sum = 0
recipt = []

# while (True):
#     product = input("Enter the product (or press 'q' to quit): ")
#     price = int(input("Enter price:"))
#     sum = sum + price
#     recipt.append(f"{product}: {price}")
#     print(f"Current total: {sum}")

#     if (product == "q"):
#         break

# print ("\n..........Your Recipt.............")
# for item in recipt:
#     print (item)

# print (f"Total: {sum}")

while (True):
    product = input("Enter the product (or press 'q' to quit): ")
    if (product == "q"):
        break
    price = int(input("Enter price:"))
    sum = sum + price
    recipt.append(f"{product}: {price}")
    print(f"Current total: {sum}")


print ("\n..........Your Recipt.............")
for item in recipt:
    print (item)

print (f"Total: {sum}")