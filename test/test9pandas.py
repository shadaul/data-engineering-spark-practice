import pandas as pd

data = [
    {'user_id': 101, 'action': 'buy', 'amount': 150},
    {'user_id': 102, 'action': 'click', 'amount': 0},
    {'user_id': 101, 'action': 'buy', 'amount': 250},
    {'user_id': 103, 'action': 'buy', 'amount': 500},
    {'user_id': 102, 'action': 'buy', 'amount': 50},
    {'user_id': 103, 'action': 'buy', 'amount': 100}
]
df = pd.DataFrame(data)

result = df[df['action'] == 'buy'].groupby('user_id')['amount'].sum().reset_index().sort_values(by='amount', ascending=False).head(2)

print(result)