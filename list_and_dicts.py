def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Gabriel", "lastname": "Tarapues"}

    super_list = [
        {"firstname": "Gabriel", "lastname": "Tarapues"},
        {"firstname": "Omar", "lastname": "Tarapues"},
        {"firstname": "Gabriel", "lastname": "Rodriguez"},
        {"firstname": "Omar", "lastname": "Rodriguez"},
        {"firstname": "Gabriel Omar", "lastname": "TR"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [2.5, 3.7, 8.9],
    }

    for key,value in super_dict.items():
        print(key, "-", value)

    for value in super_list:
        print(value["lastname"], "-", value["firstname"])

if __name__ == '__main__':
    run()