#9 Q3 WAP which accept one number and print square of that number

def Square(No):
    return No * No

def main():
    Value = int(input("Enter first number:"))

    Ret = Square(Value)

    print("Square is:",Ret)
    
if __name__ == "__main__":
    main()