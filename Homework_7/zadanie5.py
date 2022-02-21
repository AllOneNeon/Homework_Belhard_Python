import pandas as pd

df = pd.DataFrame({'Name': ['Real Madrid']})
df.to_excel('./mat.xlsx', sheet_name='BestClub', index=False)
df = pd.read_excel('mat.xlsx', 'BestClub')
df.to_csv('mat.csv')