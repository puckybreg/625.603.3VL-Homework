import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def inverse_transform_sample(inverted_cdf, n):
    data = np.random.uniform(0, 1, n)
    values = []
    for i in data:
        values.append(inverted_cdf(i))
    sorted_values = np.sort(values)
    # print(sorted_values)
    return sorted_values

def problem3_10_4():
    inverted_cdf = lambda x: np.sqrt(x)
    trails = 1000
    count = 0
    for i in range(trails):
        sampled_values = inverse_transform_sample(inverted_cdf,5)
        if (sampled_values[0]) < 0.6 and (sampled_values[4] > 0.6):
            count+=1

    percentage = count/trails
    print(f"We found there to be {percentage} of times that our Y1 and Y5 bound 0.6")


def problem3_10_6():
    inverted_cdf = lambda x:-np.log(1-x)
    trails = 1000
    possible_n = 13
    for n in range(1, possible_n):
        count = 0
        for i in range(trails):
            sampled_values = inverse_transform_sample(inverted_cdf, n)
            if sampled_values[0] < 0.2:
                count+=1
        print(f"for n of: {n}, {count/trails} percentage of the time our min")

def problem3_10_8():
    # count, bins, ignored = plt.hist(data, 1000, facecolor='green')
    #
    # plt.xlabel('X~U[0,1]')
    # plt.ylabel('Count')
    # plt.title("Uniform Distribution Histogram (Bin size 20)")
    # plt.axis([0, 1, 0, 1])  # x_start, x_end, y_start, y_end
    # plt.grid(True)
    #
    # plt.show()


def main():
    problem3_10_6()





if __name__ == "__main__":
    main()