import math

def run():
    square_root_for_first_1000_natural_numbers = {i: math.sqrt(i) for i in range(1, 1001)}
    
    print(square_root_for_first_1000_natural_numbers)

if __name__ == '__main__':
    run()