


num=int(input("Enter a number that finds the facorial"))
b=1
if num<0:
        print("There is no factor of negative number")
elif num==0:
        print("The factor is 1")
else:
    for i in range(1,num+1):  # i think this is the increament.#why is it a zero.
               b*=i
               print(f"The factorial of {num} is {b}")  # would like output to be just one value