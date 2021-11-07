def divisible_by_3(num):
    return num%3 == 0;

def run():
    my_dict = {i: i**3 for i in range(1, 101) if not divisible_by_3(i)}
    
    print(my_dict)



if __name__ == '__main__':
    run()