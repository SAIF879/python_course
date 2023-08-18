alpha_list = ['a' , 'b' , 'c']
for each_letter in "defghij":
    alpha_list.append(each_letter)
# print(alpha_list)

#for number in range(len(alpha_list)):
#print(number)


#make a function that returns the pow of interger

def power_of_integer(number , power):
    result =1
    while power>0:
        result *= number
        power-=1
    return result

base = 2
exponent = 3
result = power_of_integer(2, 3)
print(f"{base} to the power of {exponent} is {result}")
