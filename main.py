import numpy as np
import matplotlib.pyplot as plt

def main():
    print("This is a Match between John and Banker.")

    JohnMoney = 500
    BankerMoney = 2500

    matchtimes = 0
    matchtimesLimit = 200
    johnwinstime = 0
    bankerwinstime = 0

    universeLimit = 1000000

    while(matchtimes < matchtimesLimit and JohnMoney > 0 and BankerMoney > 0):
            JohnMoney -= 10
            BankerMoney -= 10
            matchtimes += 1
            matchResult = np.random.randint(2)
            if (matchResult == 1):
                JohnMoney += 20
                johnwinstime += 1
            else:
                BankerMoney += 20
                bankerwinstime += 1

    matchtype = "Happy Match"
    if(matchtimes<matchtimesLimit): matchtype = "John's Broken Match"

    print("Match times: ", matchtimes)
    print("John wins: ", johnwinstime)
    print("Banker wins: ", bankerwinstime)
    print("John's money: ", JohnMoney)
    print("Banker's money: ", BankerMoney)
    print("Match type: ", matchtype)

    # plot
    x = np.arange(2)
    y = [JohnMoney, BankerMoney]
    plt.bar(x, y)
    plt.xticks(x, ['John', 'Banker'])
    plt.show()

    # matchResult = np.random.randint(2)
    # if (matchResult == 1):
    #     print("John wins!")
    # else:
    #     print("Banker wins!")

if __name__ == "__main__":
    main()
