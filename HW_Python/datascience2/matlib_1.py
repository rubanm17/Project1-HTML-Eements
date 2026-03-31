import matplotlib.pyplot as plt

month = [1,2,3,4,5,6,7,8,9,10,11,12]

facecream = [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]
facewash = [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
toothpaste = [5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400]
bathingsoap = [9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400]
shampoo = [1200,2100,3550,1870,1560,1890,1780,2860,2100,2300,2400,1800]
moisturizer = [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]

profit = [211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200]


def profit_line_chart():
    plt.plot(month, profit, ':o', linewidth=3, markeredgecolor='red', markerfacecolor='black')
    plt.title("Company Profit per Month")
    plt.xlabel("Month")
    plt.ylabel("Profit")
    plt.show()

profit_line_chart()


def sales_multiline_chart():
    plt.plot(month, facecream, '-o', linewidth=3, label="Face Cream")
    plt.plot(month, facewash, '-o', linewidth=3, label="Face Wash")
    plt.plot(month, toothpaste, '-o', linewidth=3, label="Toothpaste")
    plt.plot(month, bathingsoap, '-o', linewidth=3, label="Bathing Soap")
    plt.plot(month, shampoo, '-o', linewidth=3, label="Shampoo")
    plt.plot(month, moisturizer, '-o', linewidth=3, label="Moisturizer")

    plt.title("Sales Data of All Products")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.legend()
    plt.show()

sales_multiline_chart()


def face_products_bar():
    width = 0.35
    x = range(len(month))

    plt.bar(x, facecream, width, label="Face Cream")
    plt.bar([i + width for i in x], facewash, width, label="Face Wash")

    plt.title("Face Cream vs Face Wash Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.legend()
    plt.show()

face_products_bar()