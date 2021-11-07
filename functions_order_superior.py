from functools import reduce

def lambda_filter():
    my_list = [1, 2, 3, 4, 5]
    print(list(filter(lambda x: x%2 == 0, my_list)))

def lambda_map():
    my_list = [1, 2, 3, 4, 5]
    print(list(map(lambda x: x**2, my_list)))

def lambda_reduce():
    my_list = [2, 2, 2, 2, 2]
    print(reduce(lambda a, b: a * b, my_list))

def run():
    lambda_filter()
    lambda_map()
    lambda_reduce()

if __name__ == '__main__':
    run()