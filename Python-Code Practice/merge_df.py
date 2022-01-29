import pandas as pd
A_df = pd.DataFrame({'A_c1': [1],
                    'c2': [2]})

B_df = pd.DataFrame({'B_c1': [1],
                    'c2': [2],
                     'Test': ['a']})
print(A_df.head())
print(B_df.head())

#new_df = pd.concat([A_df, B_df], ignore_index=True)
new_df = pd.merge(A_df, B_df,  how='left', left_on=['A_c1','c2'], right_on = ['B_c1','c2'])
print(new_df.head())