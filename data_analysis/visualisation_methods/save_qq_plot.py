import pylab
import statsmodels.api as sm
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm


def save_qq_plot(csv, file_path, generate_for_poster=False):
    # Define the fonts
    font = {'fontname': 'Nimbus Roman'}
    font_manager = fm.FontProperties(family='Nimbus Roman')
    if generate_for_poster:
        font = {'fontname': 'DejaVu Sans'}
        font_manager = fm.FontProperties(family='DejaVu Sans')

    blue_color = "#49c3fb"
    whisker_props_color = 'black'

    if generate_for_poster:
        whisker_props_color = 'white'

    fig, ax = plt.subplots(figsize=(6, 4))

    sm.qqplot(csv['cpu time'], line='45', ax=ax)

    ax.set_ylabel('Time (s)', size=15, **font)

    # Set the ticks' font
    for label in ax.get_xticklabels():
        label.set_fontproperties(font_manager)

    for label in ax.get_yticklabels():
        label.set_fontproperties(font_manager)

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    ax.set_xlim(left=0)

    # ax.grid()
    # ax.grid(which="minor", color="0.5")

    if generate_for_poster:
        # Generate with a title
        ax.set_title("Solving time of naive and duplicate model", size=15, color='white', **font)

        # Set axes colours to white
        ax.spines["bottom"].set_color("white")
        ax.spines['left'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        # plt.show()
        # plt.savefig('figures/poster/histogram.png', transparent=True)
        pylab.savefig("figures/" + file_path, transparent=True)

    else:
        # plt.show()
        plt.savefig('figures/' + file_path + '.svg')
        # pylab.savefig("figures/" + file_path)
        # pylab.show()

