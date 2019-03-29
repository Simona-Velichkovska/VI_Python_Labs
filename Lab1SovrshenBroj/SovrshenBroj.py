def sovrshen_broj(n):
    # your code here
    sum = 0
    for i in range(1, n):
        if (n % i == 0):
            sum += i
    if n == sum:
        print("Brojot " + str(n) + " e sovrshen")
    else:
        print("Brojot " + str(n) + " ne e sovrshen")


if __name__ == "__main__":
    broj = int(input())
    # sovrshen_broj()
    # your code here
    sovrshen_broj(broj)