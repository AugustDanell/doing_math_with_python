import matplotlib.pyplot as plt

if __name__ == '__main__':
    manader = int(input("Hur många månader vill du räkna på inkomster/utgifter"))
    manadar_x = []
    manadar_y = []
    change_y = []
    total = 0

    for i in range(1, manader+1):
        inkomster = 0

        while(inkomster >= 0):
            inp = float(input("Ange en inkomst för månad %d (Skriv -1 för att gå vidare)"%(i)))
            if(inp < 0):
                break

            inkomster += inp

        utgifter = 0
        while(utgifter >= 0):
            inp = float(input("Ange en utgift för månad %d (Skriv -1 för att gå vidare)" % (i)))
            if(inp < 0):
                break

            utgifter += inp

        total += inkomster-utgifter
        manadar_x.append(i)
        manadar_y.append(total)
        change_y.append(inkomster-utgifter)

    print(manadar_x, manadar_y)
    plt.scatter(manadar_x, manadar_y)
    plt.plot(manadar_x, manadar_y)
    plt.xlabel("Månad")
    plt.ylabel("Total monetär summa")
    plt.title("Inkomst/utgift beräkning")

    for i, txt in enumerate(change_y):
        plt.annotate(txt, (manadar_x[i], manadar_y[i]))

    plt.show()
