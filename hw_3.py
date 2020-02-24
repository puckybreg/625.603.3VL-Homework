import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Function for simulating a series
def binornd(n,p):
    heads = []
    tosses = [np.random.random() for i in range(n)]
    return len([i for i in tosses if i <= p])



def main():
    ngood = 8
    nbad = 4
    sampled= 3
    results = []
    for i in [4,2,1,0.5]:
        sim = np.random.exponential(1/i)
        results.append(sim)
        # print(sim)
    print(results)

    # matplotlib histogram
    # plt.hist(results, color='blue', edgecolor='black',
    #          bins=int(180/5))
    #
    # plt.show()

    x = np.arange(0, 4, 0.001)
    plt.plot(4*np.exp(-4*x)) #,2*np.exp(-2*x), , 0.5*np.exp(-0.5*x) )
    plt.plot(1*np.exp(-1*x))
    plt.plot(0.5*np.exp(-0.5*x))
    plt.plot(2*np.exp(-2*x))


    plt.show()


if __name__ == "__main__":
    main()