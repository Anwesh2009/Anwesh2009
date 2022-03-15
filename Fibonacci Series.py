while True:
    number = int(input("How many numbers of Fibonacci Series:  "))
    no1, no2, no3, no4 = 0,1,1,3
    count = 0
    if number == 2:
        print(no1,no2)
    else:
        print("Fibonacci sequence:")
        while count < number:
            print(no1)
            nth = no1 + no2
            # update values
            no1 = no2
            no2 = nth
            count += 1
