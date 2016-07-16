MAX_WEIGHT = 100


def check_bag_weight(bag_weight, coin, max_weight=MAX_WEIGHT):
    weight_correct = False
    diff = max_weight - bag_weight
    diffcoin = round(diff/coin['weight'],0)
    if bag_weight < max_weight:
        add_or_subtract = 'add'
    elif bag_weight > max_weight:
        add_or_subtract = 'remove'
    else:
        weight_correct = True
        print("Your bag is the correct weight")

    if not weight_correct:
        if diffcoin > 1:
            plural = 'pieces'
        else:
            plural = 'piece'
        print("You need to {0} the weight of you bag by {1} grams".format(add_or_subtract, diff))
        print("You need to {0} {1} {2}p {3} to your bag".format(add_or_subtract, diffcoin, coin['name'], plural))


def input_bag_weight():
    while True:
        try:
            bag_weight = float(input("How much does your money bag weigh: "))
            break
        except ValueError:
            print("That is not a number")
    print("Your bag weighs {0} grams".format(bag_weight))
    return bag_weight

if __name__ == '__main__':
    bag_weight = input_bag_weight()

    check_bag_weight(bag_weight, coin={'name':1, 'weight':3.56})
