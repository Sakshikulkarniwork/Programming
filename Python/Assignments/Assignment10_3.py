# WAP which accepts one number and print factorial of that number

def Factorial(No):
    Fact = 0
    for i in range(1, No+1):
        Fact = Fact + i

    return(Fact)

def main():
    Value = int(input("Enter a number: "))

    Ret = Factorial(Value)

    print(f"Factorial of {Value} number is : ",Ret)

if __name__ == "__main__":
    main()