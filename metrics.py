import pandas as pd

def compute_metrics(df: pd.DataFrame):
    metrics = {}
    if df.empty:
        return metrics

    metrics['total_posts'] = len(df)
    metrics['average_views'] = round(df['views'].mean(), 2)
    metrics['average_length'] = round(df['text'].apply(len).mean(), 2)

    # Активность по дням недели
    df['day_of_week'] = df['date'].dt.day_name()
    metrics['active_days'] = df['day_of_week'].value_counts().to_dict()

    return metrics
