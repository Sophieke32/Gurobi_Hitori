import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

def save_graph_ntest(csv1, csv2, csv3, generate_for_poster):
    # Define the fonts
    font = {'fontname': 'Nimbus Roman'}
    font_manager = fm.FontProperties(family='Nimbus Roman')
    if generate_for_poster:
        font = {'fontname': 'DejaVu Sans'}
        font_manager = fm.FontProperties(family='DejaVu Sans')

    fig, ax = plt.subplots(figsize=(6, 5))

    sizes = np.unique(csv1['n'])

    data1 = []
    data2 = []
    data3 = []
    for i in sizes:
        data1.append(np.mean(csv1[csv1['n']==i]['cpu time']))
        data2.append(np.mean(csv2[csv2['n']==i]['cpu time']))
        data3.append(np.mean(csv3[csv3['n']==i]['cpu time']))

    # data1, data2 = csv1['cpu time'], csv2['cpu time']
    ax.plot(sizes, data2, label="Duplicates model", color='red')
    ax.plot(sizes, data1, label="Optimised naive model", color='#49c3fb')
    ax.plot(sizes, data3, label="Path model", color='#8c52ff')

    ax.set_ylabel('Mean solving time (s)', size=15, **font)
    ax.set_xlabel('Instance size', size=15, **font)

    # Create legend and set its, and the ticks' font
    ax.legend(prop=font_manager)
    for label in ax.get_xticklabels():
        label.set_fontproperties(font_manager)

    for label in ax.get_yticklabels():
        label.set_fontproperties(font_manager)

    # Only show ticks on the left and bottom spines
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_bounds(5, 10)
    ax.spines["left"].set_bounds(0, 0.14)

    if generate_for_poster:
        # Set title
        ax.set_title("Solving time of naive and duplicate model", size=15, color='white', **font)

        # Set axes colours to white
        ax.spines["bottom"].set_color("white")
        ax.spines['left'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        # plt.show()
        plt.savefig('figures/poster/graph_ntest.png', transparent=True)

    else:
        # plt.show()
        plt.savefig('figures/graph_ntest.svg')