#9 Q5 WAP which accept one number and check weather it is divisible by 3 and 5

def ChkDivisible(No):
    return (No % 3 == 0) and (No % 5 == 0)

def main():
    Value = int(input("Enter number:"))

    if ChkDivisible(Value):
        print(Value, "is divisible by 3 and 5")
    else:
        print(Value, "is not divisible by 3 and 5")

if __name__ == "__main__":
    main()