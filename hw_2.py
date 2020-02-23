# 2.7.12


def main():
    my_string = "AROLLINGTONEGATHERSNOMO"
    my_sorted = ''.join(sorted(my_string))
    # my_string.sorted()

    standard = 'A'
    acc = ''
    for i in my_sorted:
        if i != standard:
            standard = i
            print(acc, len(acc))
            acc = i
        else:
            acc= acc + i
    print(my_sorted, len(my_sorted))
    # G_1 = my_sorted[0:2]
    # G_2 = my_sorted[2:4]
    # print(G_1, G_2)

if __name__ == "__main__":
    main()