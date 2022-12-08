import matplotlib.pyplot as plt

def generate_pie_charts():
    labels = ['a','b','c']
    values = [40,70,150]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()