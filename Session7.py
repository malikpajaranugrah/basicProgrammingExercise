def menu():
    print("""
1. Calculate the area of triangle
2. Calculate the area of rectangle
3. Determine odd and even numbers
4. Exit
""")

def triangle():
    print("Calculate the area of triangle")
    B = float(input("input base: "))
    H = float(input("input height: "))
    area = 0.5 * B * H 
    print("The area of triangle is: ",area)

def rectangle():
    print("Calculate the area of rectangle")
    L = float(input("input length: "))
    W = float(input("input width: "))
    area = (L*W)
    print("The area of rectangle is: ",area)

def oddAndEven():
    print("Determine odd and even numbers")
    number = int(input("input the numbers: "))
    if(number % 2 == 0):
        print(number,"is even number")
    else:
        print(number,"is odd number")


def main():
    run = True
    while run:
        menu()
        choose = input("chosee the number: ")
        if choose == "1":
            triangle()
        elif choose == "2":
            rectangle()
        elif choose == "3":
            oddAndEven()
        elif choose == "4":
            print("thanks for using this app")
            break
        else:
            print("invalid input")



if __name__=="__main__":
    main()












