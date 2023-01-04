# a function that returns a greeting
def hello():
    print("Greetings, user!")

# a function that returns 3 arguments into a list
def pack(a, b, c):
    return [a, b, c]

# A function called eat_lunch(). This function should accept a list of any length, 
# and print out a series of strings that say "First I eat __" (the first element of the list), 
# and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". 
# The function should not return anything.

# Indentation is very important in python --

def eat_lunch(my_list):
  if len(my_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_list)):
      if i == 0:
        print(f"First I eat {my_list[0]}")
      else:
        print(f"Next I eat {my_list[i]}")


hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])