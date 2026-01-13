import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np



def save_boxplots_spearman_vs_time(csv, generate_for_poster, file_addition, title, attribute, x_label):
    # Define the fonts
    font = {'fontname': 'Nimbus Roman'}
    font_manager = fm.FontProperties(family='Nimbus Roman')
    if generate_for_poster:
        font = {'fontname': 'DejaVu Sans'}
        font_manager = fm.FontProperties(family='DejaVu Sans')

    # csv = remove_outliers_csv(csv)

    values = np.unique(csv[attribute])
    example_data = []

    for v in values:
        indices = np.where(csv[attribute] == v)
        example_data.append(csv['cpu time'][indices])

    fig, ax = plt.subplots(figsize=(6, 5))
    color = "#49c3fb"
    whisker_props_color = 'black'

    if generate_for_poster:
        whisker_props_color = 'white'

    plot = ax.boxplot(example_data, patch_artist=True,
        boxprops=dict(facecolor = color, color = color),
        capprops=dict(color = whisker_props_color),
        whiskerprops=dict(color = whisker_props_color),
        flierprops=dict(color = color, markeredgecolor = color),
        medianprops=dict(color = 'red'),
        tick_labels=values,
        orientation='horizontal',
        )
    ax.set_xscale('log')

    # Set the ticks' font
    for label in ax.get_xticklabels():
        label.set_fontproperties(font_manager)

    for label in ax.get_yticklabels():
        label.set_fontproperties(font_manager)

    # Set labels and title
    ax.set_ylabel(x_label, size=15, **font)
    ax.set_xlabel('Time (s)', size=15, **font)
    ax.set_title(title, size=15, color='white', **font)

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    ax.grid()
    # ax.grid(which="minor", color="0.8")

    ax.tick_params(axis='both', labelsize=10)
    if len(ax.get_yticklabels()) > 10: plt.setp(ax.get_yticklabels()[::2], visible=False)

    if generate_for_poster:
        # Set axes colours to white
        ax.spines["bottom"].set_color("white")
        ax.spines['left'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white', labelsize=25)
        ax.tick_params(axis='y', colors='white', labelsize=15)

        plt.savefig('figures/poster/boxplot_' + attribute + '_vs_time_' + file_addition + '_poster.png', transparent=True)

    else:
        # plt.show()
        plt.savefig('figures/boxplot_' + attribute + '_vs_time_' + file_addition + '.svg')

