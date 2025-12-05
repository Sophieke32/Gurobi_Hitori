import matplotlib.pyplot as plt

from data_analysis.helper_methods.remove_outliers import remove_outliers

def save_plot_naive_vs_duplicates(csv1, csv2):
    fig, ax = plt.subplots(figsize=(6, 5))

    cpu_time_1_cleaned, cpu_time_2_cleaned = remove_outliers(csv1['cpu time']), remove_outliers(csv2['cpu time'])
    ax.plot(cpu_time_2_cleaned, label="naive model", color='#49c3fb')
    ax.plot(cpu_time_1_cleaned, label="duplicates model", color='red')
    ax.set_ylabel('Time (s)', size=15)
    ax.set_xlabel('Problem instance', size=15)
    ax.legend()

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # Only show ticks on the left and bottom spines
    ax.spines["bottom"].set_bounds(0, 1000)
    ax.spines["left"].set_bounds(0, 0.8)

    # Set axes colours to white
    ax.spines["bottom"].set_color("white")
    ax.spines['left'].set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # plt.show()
    plt.savefig('figures/plot_naive_vs_duplicates.png', transparent=True)