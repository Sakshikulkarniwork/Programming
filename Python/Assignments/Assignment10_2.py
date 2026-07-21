# WAP which accepts one number and print the sum of first N natural numbers


def SumOfNum(No):
    sum = 0
    for i in range(1, No+1):
        sum = (sum + i)

    return(sum)

def main():
    Value = int(input("Enter a number: "))

    Ret = SumOfNum(Value)

    print(f"Sum of {Value} natural number is : ",Ret)

if __name__ == "__main__":
    main()