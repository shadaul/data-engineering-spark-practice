import pandas as pd

data = {
    'name': ['Али', 'Борис', 'Виктор', 'Гуля', 'Дамир'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'IT'],
    'salary': [6000, 4000, 4500, 7000, 8000]
}
df = pd.DataFrame(data)

# mask = (df['salary'] > 5000) & (df['department'] == 'IT')

# filtered_df = df[mask]

# result = filtered_df[['name', 'salary']]

# print(result)

result = df.groupby('department')['salary'].mean().reset_index()

print(result)