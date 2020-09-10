# python 3.6.4
# encoding: utf-8

def count_one(number):

    count = 0

    while number > 0:

        count = count if number % 2 == 0 else count + 1
        number = number >> 1

    return count


if __name__ == '__main__':

    for number in range(0,1000,3):

        count = count_one(number)

        print("Number:{},Count:{}".format(number,count))
