print ("PLEASE ENTER THE FOLLOWING INFORMATION:")

name = input("Please enter your name: ")
with open("output.txt", "w") as f:
    f .write(name + "\n")

print ("WELCOME " +name+ "!")

age = int(input("Please enter your Age " + name + ": "))

if age < 18:
    print("You are not qualified.")
    exit()
elif age >= 18 and age < 35:
    print("You are qualified.")
    with open("output.txt", "a+") as f:
        f.write(str(age) + "\n")
else:
    print("You are above the age qualification.")
    exit()


address = input("Enter your Address " +name+ ": ")
print("Saved")
with open("output.txt", "a+") as f:
    f .write(address + "\n")


gender = input("Enter your Gender " +name+ ": ")
print("Saved")
with open("output.txt", "a+") as f:
    f .write(gender + "\n")

account_details = int(input("Enter account-no "+name+":"))
print("Saved")
with open("output.txt", "a+") as f:
    f.write(str(account_details) + "\n")

#strip(16) - strip here removes whitespaces at the begining and of a string character or removes any leading and trailing characters from a string and should be used in a conditional space
#this is to define username access
  #  if name ==():
  #  exit()
#elif name == "samuel" or name == "big stan":
# print("correct name entry ""Saving.....")

#else:
#    print("yuor entry is incorrect ." "Not,Saved")  
#    exit()
