import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd


def save_survival_plot(csv1, csv2, generate_for_poster):
    datapoints = list()

    for csv in [csv1, csv2]:
        y = sorted(csv['cpu time'])

        for i in range(1, len(y)):
            y[i] = y[i] + y[i-1]

        x = np.linspace(0, len(y), len(y))

        datapoints.append(y)


    # Define the fonts
    font = {'fontname': 'Nimbus Roman'}
    font_manager = fm.FontProperties(family='Nimbus Roman')
    legend_font = {'family': 'Nimbus Roman'}
    if generate_for_poster:
        font = {'fontname': 'DejaVu Sans'}
        font_manager = fm.FontProperties(family='DejaVu Sans')
        legend_font = {'family': 'DejaVu Sans'}


    fig, ax = plt.subplots(figsize=(6, 5))


    ax.plot(datapoints[0], x, label="Naive model", color='#49c3fb')
    ax.plot(datapoints[1], x, label="Duplicates model", color='red')

    ax.legend(prop=legend_font)

    ax.set_xscale('log')

    ax.set_xlabel('Time (s)', size=15, **font)
    ax.set_ylabel('Number of instances solved', size=15, **font)

    # Set the ticks' font
    for label in ax.get_xticklabels():
        label.set_fontproperties(font_manager)

    for label in ax.get_yticklabels():
        label.set_fontproperties(font_manager)

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    ax.grid()
    # ax.grid(which="minor", color="0.8")

    if generate_for_poster:
        # Generate with a title
        ax.set_title("Performance of the naive and duplicates model", size=15, color='white', **font)

        # Set axes colours to white
        ax.spines["bottom"].set_color("white")
        ax.spines['left'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        # plt.show()
        plt.savefig('figures/poster/boxplot_plot_two_models_poster.png', transparent=True)

    else:
        # plt.show()
        plt.savefig('figures/survival_plot.svg')
