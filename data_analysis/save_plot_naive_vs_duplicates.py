import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def save_plot_naive_vs_duplicates(csv1, csv2, generate_for_poster):
    # Define the fonts
    font = {'fontname': 'Nimbus Roman'}
    font_manager = fm.FontProperties(family='Nimbus Roman')
    if generate_for_poster:
        font = {'fontname': 'DejaVu Sans'}
        font_manager = fm.FontProperties(family='DejaVu Sans')

    fig, ax = plt.subplots(figsize=(6, 5))

    # cpu_time_1_cleaned, cpu_time_2_cleaned = remove_outliers(csv1['cpu time']), remove_outliers(csv2['cpu time'])
    cpu_time_1_cleaned, cpu_time_2_cleaned = csv1['cpu time'], csv2['cpu time']
    ax.plot(cpu_time_2_cleaned, label="Naive model", color='#49c3fb')
    ax.plot(cpu_time_1_cleaned, label="Duplicates model", color='red')

    ax.set_ylabel('Time (s)', size=15, **font)
    ax.set_xlabel('Problem instance', size=15, **font)

    # Create legend and set its, and the ticks' font
    ax.legend(prop=font_manager)
    for label in ax.get_xticklabels():
        label.set_fontproperties(font_manager)

    for label in ax.get_yticklabels():
        label.set_fontproperties(font_manager)

    # Only show ticks on the left and bottom spines
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_bounds(0, 1000)
    ax.spines["left"].set_bounds(0, 0.8)

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
        plt.savefig('figures/poster/plot_naive_vs_duplicates_poster.png', transparent=True)

    else:
        # plt.show()
        plt.savefig('figures/plot_naive_vs_duplicates.svg')