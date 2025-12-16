import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def save_boxplot_two_models(csv1, csv2, generate_for_poster):
    # Define the fonts
    font = {'fontname': 'Nimbus Roman'}
    font_manager = fm.FontProperties(family='Nimbus Roman')
    if generate_for_poster:
        font = {'fontname': 'DejaVu Sans'}
        font_manager = fm.FontProperties(family='DejaVu Sans')

    fig, ax = plt.subplots(figsize=(6, 4))

    # data1, data2 = remove_outliers_two_arrays(csv1['cpu time'], csv2['cpu time'])
    data1, data2 = csv1['cpu time'], csv2['cpu time']
    data = [data1, data2]

    blue_color = "#49c3fb"
    whisker_props_color = 'black'

    if generate_for_poster:
        whisker_props_color = 'white'

    ax.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=blue_color, color=blue_color),
               capprops=dict(color=whisker_props_color),
               whiskerprops=dict(color=whisker_props_color),
               flierprops=dict(color=blue_color, markeredgecolor=blue_color),
               medianprops=dict(color='red'),
               tick_labels=["Naive model", "Duplicates model"]
               )
    ax.set_yscale('log')

    ax.set_ylabel('Time (s)', size=15, **font)

    # Set the ticks' font
    for label in ax.get_xticklabels():
        label.set_fontproperties(font_manager)

    for label in ax.get_yticklabels():
        label.set_fontproperties(font_manager)

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    ax.grid()
    ax.grid(which="minor", color="0.5")

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
        plt.savefig('figures/poster/boxplot_plot_two_models_poster.png', transparent=True)

    else:
        # plt.show()
        plt.savefig('figures/boxplot_plot_two_models.svg')
