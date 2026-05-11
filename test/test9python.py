data = [
    {'user_id': 101, 'action': 'buy', 'amount': 150},
    {'user_id': 102, 'action': 'click', 'amount': 0},
    {'user_id': 101, 'action': 'buy', 'amount': 250},
    {'user_id': 103, 'action': 'buy', 'amount': 500},
    {'user_id': 102, 'action': 'buy', 'amount': 50},
    {'user_id': 103, 'action': 'buy', 'amount': 100}
]

totals = {}

for raw in data:
    if raw['action'] == 'buy':
        if raw['user_id'] in totals:
            totals[raw['user_id']] += raw['amount']
        else:
            totals[raw['user_id']] = raw['amount']

top_2 = sorted(totals.items(), key=lambda x: x[1], reverse=True)[:2]

print(top_2)