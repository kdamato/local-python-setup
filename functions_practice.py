def hello():
    print("Hello there!")
hello()

def pack(number1, number2, number3):
   list = []
   for i in range(1,4):
      list.append(i)
   return list
a = pack(1,2,3)
print (a)

# ^It's more complex but I wanted to challenge myself a bit, I'll put simplified version at the end

def eat_lunch(meal):
    if len(meal) == 0:
         print("My lunchbox is empty!")  
    else:
        for i in range(len(meal)):
            if i == 0:
                print(f"First I eat {meal[0]}")
            else:
                print(f"Next I eat {meal[i]}") 
eat_lunch([])
eat_lunch(["Pizza"])
eat_lunch(["Pizza", "Pasta", "Chicken"])


# Heres the simplified version of 2

# def list(num1,num2,num3):
#     return [num1,num2,num3]
# print(list(1,2,3))