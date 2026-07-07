#9 Q2) WAP having one function ChkGreater() that accepts two number and print the greater number.

def ChkGreater(No1, No2):
    if (No1 > No2):
        print(No1,"is Greater")
    else:
        print(No2,"is Greater")

def main():
    Value1 = int(input("Enter first number:"))

    Value2 = int(input("Enter second number:"))

    ChkGreater(Value1,Value2)
    
if __name__ == "__main__":
    main()