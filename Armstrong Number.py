while True:
    n = int(input("Enter a number: "))
    s = 0
    t = n
    power = n
    while t > 0:
       digit = t % 10
       s += digit ** len(str(power))
       t //=10
    if n == s:
       print(n,"is an Armstrong number")
    else:
       print(n,"is not an Armstrong number")

