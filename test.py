from decimal import ROUND_FLOOR
from random import randint

def dice():
    return randint(1,6)


def main():
    times = int(input("Enter number of times:"))
    x = 0
    roles = []
    while x != times:
        role = dice()
        roles.append(role)
        x += 1
    
    avg = sum(roles) / len(roles)
    print(round(avg, 2))
    for num in roles:
        print(num, end = "")


if __name__ == "__main__":
    main()