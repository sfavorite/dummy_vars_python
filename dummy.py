import pandas as pd

df = pd.DataFrame(['FL','CA','MD','NY','NY','NY','NY'], columns= ['State'])

pd.get_dummies(data.State)

# Add some random numbers
df.loc[:,'Random'] = pd.Series(np.random.randn(len(df)), index=df.index)

# Add a column of letters
df.insert(1, 'test', ('A', 'B', 'C', 'D', 'E', 'F', 'G'))

# Merge the two dataframes
pd.concat([df, pd.get_dummies(df.State)], axis=1)
