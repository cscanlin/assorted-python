import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def bar_graph():
    df = pd.read_csv('bins.csv', index_col=False, sep=';')
    df.columns = ['Bins', 'Value']
    Values = list(df['Value'])
    Bins = list(df['Bins'])

    d = dict(zip(Bins, Values))

    count = 0
    for i in Values[:]:
        if i < 14342671:
            count += i
            Values.remove(i)
    Values.append(count)

    x = np.arange(len(Values))
    plt.bar(x, Values, align='center', width=1)
    ymax = max(d.values()) + 1
    plt.ylim(0, ymax)
    plt.axis([0, 28, 0, ymax+150000])
    plt.xticks(x, Bins, rotation='vertical')
    #plt.margins(0)
    plt.show()

def histogram():
    df = pd.read_csv('graph.csv', index_col=False, sep=';')
    df.columns = ['Bins', 'Value']
    Values = list(df['Value'])
    Bins = list(df['Bins'])

    count = 0
    for i in Values[:]:
        if i < 14342671:
            count += i
            Values.remove(i)
    Values.append(count)

    ymax = max(Values)

    n, bins, patches = plt.hist(Values, bins=100, facecolor='green', alpha=0.75)
    plt.xlabel('# of Impressions')
    plt.ylabel('User per # Impressions')
    #plt.axis([0, 25, 0, ymax])
    plt.grid(True)

    plt.show()

if __name__ == '__main__':
    bar_graph()
    # histogram()
