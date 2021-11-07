def divisible_by_3(num):
    return num%3 == 0;

def divisible_by_9(num):
    return num%9 == 0;

def divisible_by_6(num):
    return num%6 == 0;

def divisible_by_4(num):
    return num%4 == 0;

def run():
    squares_divisibles_by_3_until_100 = [i**2 for i in range(1, 101) if not divisible_by_3(i)]
    print(squares_divisibles_by_3_until_100)

    print("\n<===================================================================>\n")
    
    numbers_divisible_by_9_and_6_and_4_until_99999 = [i for i in range(1, 100000) if divisible_by_9(i) and divisible_by_6(i) and divisible_by_4(i)]
    print(numbers_divisible_by_9_and_6_and_4_until_99999)

if __name__ == '__main__':
    run()