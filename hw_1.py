import random

def draw():
    list_of_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    randomly_drawn = []
    for x in range(5):
        choice = random.choice(list_of_int)
        list_of_int.remove(choice)
        randomly_drawn.append(choice)
    randomly_drawn.sort()
    # print(randomly_drawn)
    # print(randomly_drawn[3])
    return randomly_drawn[3]

def main():
    count = 0
    for x in range(1500000):
        my_draw = draw()
        if my_draw < 8:
            count+= 1
    print("count:", count)
    print(count/1500000)
if __name__ == "__main__":
    main()

