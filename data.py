import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('fifa21_raw_data_v2.csv')  
df['height'] = pd.to_numeric(df['height'])
df['weight'] = pd.to_numeric(df['weight'])
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
long_serving_players = df[df['Joined'] > 10]
print(long_serving_players)
def convert_to_number(x):
    if 'M' in x:
        return float(x.replace('M', '')) * 1_000_000
    elif 'K' in x:
        return float(x.replace('K', '')) * 1_000
    else:
        return float(x)

df['Value'] = df['Value'].apply(convert_to_number)
df['Wage'] = df['Wage'].apply(convert_to_number)
df['Release Clause'] = df['Release Clause'].apply(convert_to_number)
star_columns = ['column1', 'column2', ...]  # Replace with actual column names
for col in star_columns:
    df[col] = df[col].str.replace('*', '').astype(float)
plt.scatter(df['Wage'], df['Value'])
plt.xlabel('Wage')
plt.ylabel('Value')
plt.title('Wage vs Value')
plt.show()
