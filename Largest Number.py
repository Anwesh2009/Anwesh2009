while True:
    try:
        a = int(input("First Number : "))
        b = int(input("Second Number : "))
        c = int(input("Third Number : "))

        if a>b and a>c:
            print("Biggest number is ",a)
        elif b>a and b>c:
            print("Biggest Number is ",b)
        else:
            print("Biggest Number is ",c)
    except:
        print("Enter Only Numbers!")