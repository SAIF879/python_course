
import for_loop

data = for_loop.power_of_integer(2,4)
print(data)

try:
    number = int(input("Enter a number --> "))
    print(number)
except ZeroDivisionError :
    print("invalid argumnet")
except ValueError :
    print("value error")
