import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style="whitegrid")

def plot_views_over_time(df: pd.DataFrame, output_file='views.png'):
    if df.empty:
        return
    df_sorted = df.sort_values('date')
    plt.figure(figsize=(10,5))
    sns.lineplot(x='date', y='views', data=df_sorted, marker='o')
    plt.title('Views over Time')
    plt.xlabel('Date')
    plt.ylabel('Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
