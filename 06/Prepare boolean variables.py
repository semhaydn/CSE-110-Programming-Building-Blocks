# is_hot = True

# # You can check the value of the variable

# if is_hot:
#     print("It's hot")


# # it works, but its redundat (and therefore bad practice) to check if it is True

# if is_hot == True:
#     print("It's hot ")


is_hot = True
# Using the "not" keyword
if not is_hot:
    print("It is not hot")

# It works, but is generally avoided to check if it is false:
if is_hot == False:
    print("It is not hot")