import math

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    x = int(input())

    # vasiot kod pisuvajte go tuka

    d = {}

    for i in range(m, n + 1):
        d[i] = (i ** 2, i ** 3, round(math.sqrt(i), 5))

    if x not in range(m,n):
        print('nema podatoci')
    else:
        print(d[x])

    print(sorted(d.items()))