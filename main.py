import numpy as np
import matplotlib.pyplot as plt

def main():
    print("This is a Match between John and Dealer.")

    JohnSavings = 500
    DealerSavings = 999999

    JohnMoney = JohnSavings
    DealerMoney = DealerSavings

    matchtimes = 0
    matchtimesLimit = 2000
    johnwinstime = 0
    Dealerwinstime = 0

    JohnMoneyFlow = np.zeros(matchtimesLimit)
    JohnMoneyRise = np.zeros(matchtimesLimit)
    DealerMoneyFlow = np.zeros(matchtimesLimit)
    DealerMoneyRise = np.zeros(matchtimesLimit)

    universeLimit = 1000000

    while(matchtimes < matchtimesLimit and JohnMoney > 0 and DealerMoney > 0):
            JohnMoney -= 10
            DealerMoney -= 10
            matchtimes += 1
            matchResult = np.random.randint(2)
            if (matchResult == 1):
                JohnMoney += 20
                johnwinstime += 1
            else:
                DealerMoney += 20
                Dealerwinstime += 1
            JohnMoneyFlow[matchtimes-1] = JohnMoney - JohnSavings
            JohnMoneyRise[matchtimes-1] = JohnMoney
            DealerMoneyFlow[matchtimes-1] = DealerMoney - DealerSavings
            DealerMoneyRise[matchtimes-1] = DealerMoney

    matchtype = "Happy Match"
    if(matchtimes<matchtimesLimit): matchtype = "John's Broken Match"

    print("Match times: ", matchtimes)
    print("John wins: ", johnwinstime)
    print("Dealer wins: ", Dealerwinstime)
    print("John's money: ", JohnMoney)
    print("Dealer's money: ", DealerMoney)
    print("Match type: ", matchtype)


    # 创建一个包含两个子图的图形，每个子图有一行和两列
    fig, axs = plt.subplots(3, 1, figsize=(8, 6))

    # 第一个子图：绘制John和Dealer的MoneyFlow
    axs[0].plot( JohnMoneyFlow[0:matchtimes], label='JohnMoneyFlow', color='red')
    axs[0].plot(DealerMoneyFlow[0:matchtimes], label='DealerMoneyFlow', color='blue')
    axs[0].set_xlabel('Match times')
    axs[0].set_ylabel('Money')
    axs[0].set_title('Player Money Flow')
    axs[0].legend()

    # 第二个子图：绘制John和Dealer的MoneyRise
    axs[1].plot(JohnMoneyRise[0:matchtimes], label='JohnMoneyRise', color='red', linestyle='--')
    axs[1].plot(DealerMoneyRise[0:matchtimes], label='DealerMoneyRise', color='blue', linestyle='--')
    axs[1].set_xlabel('Match times')
    axs[1].set_ylabel('Money')
    axs[1].set_title('Player Money Rise')
    axs[1].legend()

    x = np.arange(2)
    y = [johnwinstime, Dealerwinstime]
    axs[2].bar(x, y, color=['red', 'blue'], label=['John', 'Dealer'])
    axs[2].set_xlabel('Player')
    axs[2].set_ylabel('Win times')
    axs[2].set_title('Win times')
    axs[2].legend()


    # 调整子图之间的间距
    plt.tight_layout()

    # 显示图形
    plt.show()

if __name__ == "__main__":
    main()
