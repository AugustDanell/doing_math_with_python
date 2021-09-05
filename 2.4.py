from matplotlib import pyplot as plt

# Function from the book:
def create_bar_chart(data, labels):
    num_bars = len(data)
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')
    plt.yticks(positions, labels)
    plt.xlabel('Expenditure')
    plt.ylabel('Category')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    try:
        categories = int(input("Enter in the amount of categories you want."))
        if(categories <0):
            raise Exception
    except:
        print("Error, amount of categories need to be a positive integer.")
    else:
        category_list = []
        expenditure_list = []
        for i in range(categories):
            category_list.append(input("Enter in a category."))
            expenditure_list.append(int(input("Expenditure")))

        create_bar_chart(expenditure_list, category_list)
