import pandas as pd

df_success = df[df['status'] == 'SUCCESS']

grouped = df_success.groupby('user_id').agg(
    total_amount=('amount', 'sum'),
    tx_amount=('amount', 'count')
).reset_index()

loyal_users = grouped[grouped['tx_count'] >= 2]

top3 = loyal_users.sort_values(by='total_amount', ascending=False).head(3)

result = top3[['user_id', 'total_amount']]

print(result)