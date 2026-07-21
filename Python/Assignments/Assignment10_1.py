# WAP which accept one number and prints multiplication table of that number

def MultiplicationTable(No):
    for i in range(1,11):
        print (No * i)

def main():
    Value = int(input("Enter a number: "))

    MultiplicationTable(Value)

if __name__ == "__main__":
    main()