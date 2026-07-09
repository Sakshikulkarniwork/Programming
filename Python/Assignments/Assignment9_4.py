#9 Q4 WAP which accept one number and print cube of that number

def Cube(No):
    return (No ** 3)

def main():
    Value = int(input("Enter number:"))

    Ret = Cube(Value)

    print("Cube is :",Ret)

if __name__ == "__main__":
    main()