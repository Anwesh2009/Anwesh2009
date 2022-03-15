while True:
    #choice
    ch = input("Type 'CI' For Compund interest\n            or\nType 'SI' For Simple Interest \n")
    #SI = ptr/100
    if ch == "SI":
        p = float(input("Enter the Principle Amount: "))
        r = float(input("Enter the Rate of Interest: "))
        t = float(input("Enter the Number of Years: "))
        SI = p * t * r / 100
        print(f'Simple interest is {SI}')

    #CI = p - p(1+r/100)^n
    if ch == "CI":
        P = float(input("Enter the Principle Amount: "))
        R = float(input("Enter the Rate of Interest: "))
        T = float(input("Enter the Number of Years: "))
        CI = (P * (pow((1 + R / 100), T)))-P
        print(f'Compound interest is {CI}')