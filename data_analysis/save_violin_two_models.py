import matplotlib.pyplot as plt
import seaborn as sns

from data_analysis.helper_methods.remove_outliers import remove_outliers, remove_outliers_two_arrays


def save_violin_two_models(csv1, csv2):
    fig, ax = plt.subplots(figsize=(6, 5))

    data1, data2 = remove_outliers_two_arrays(csv1['cpu time'], csv2['cpu time'])

    print(len(data1), min(data1))
    print(len(data2), min(data2))

    data = [data1, data2]

    sns.violinplot(data=data)

    # ax.violinplot(remove_outliers(csv1['cpu time']),
    #               showmeans=False,
    #               showmedians=True,
    #               side='high')
    #
    # ax.violinplot(remove_outliers(csv2['cpu time']),
    #               showmeans=False,
    #               showmedians=True,
    #               side='high')

    ax.set_yscale('log')

    plt.show()
