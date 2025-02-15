from wordcloud import WordCloud, STOPWORDS
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="whitegrid")
plt.style.use('classic')


def generate_barplot(df, title, xLabel, yLabel, img_path):

    plt.style.use('classic')

    fig, ax = plt.subplots(figsize=(8, 6))
    df.plot.bar(ax=ax)
    plt.xticks(rotation=50)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 9), textcoords='offset points')
    plt.savefig(img_path, bbox_inches='tight', pad_inches=0, facecolor="white")
    plt.close()
