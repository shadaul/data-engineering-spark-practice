import pandas as pd

data = {
    'product': ['Ноутбук', 'Мышка', 'Ноутбук', 'Клавиатура', 'Мышка', 'Мышка'],
    'quantity': [1, 5, 2, 3, 2, 1]
}
df = pd.DataFrame(data)

result = df.groupby('product')['quantity'].sum().sort_values(ascending=False).reset_index()

print(result)