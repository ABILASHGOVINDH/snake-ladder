import pandas as pd
#
# data = {
#     'player_id': [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
#     'name': ['Mason', 'Riley', 'Bob', 'Isabella', 'Zachary', 'Ava', 'Violet', 'Thomas', 'Jack', 'Charlie'],
#     'age': [24, 30, 30, 32, 24, 24, 18, 18, 36, 36],
#     'position': ['Forward', 'Winger', 'Striker', 'Goalkeeper', 'Midfielder', 'Defender', 'Striker', 'Striker', 'Midfielder', 'Center-back'],
#     'team': ['RealMadrid', 'Barcelona', 'ManchesterUnited', 'Liverpool', 'BayernMunich', 'Chelsea', 'Juventus', 'ParisSaint-Germain', 'ManchesterCity', 'Arsenal']
# }
#
# df = pd.DataFrame(data)
# # print(df.shape)
# #
# # print(df[['name','age']])
#
# print(df.loc[[0,1],['name','age']])
# print(df.iloc[0,1])
#
# print(df.columns)
# print()
# print()
# print(df.loc[0:2,'name':'position'])
#
# # change the index values
# df.set_index('name',inplace=True) # using inplace= True we'r changing the eniter tables as index followed
# print(df)
# print(df.loc['Mason':'Bob']) # after changing it acessing them through loc
#
# # count the value
# print(df.value_counts("age",ascending=True))
# print()
# print()
# print(df['age'].value_counts())
#
# #reset and sort the index
#
# print(df.sort_index(ascending=True))
#
# # reset the index
# df.reset_index(inplace=True)
# print(df)
#
# print()
# # filter
#
# print(df.loc[df['age'] == 24,'position'])
#
# print()
# print()
#
# # another way
# filt = (df['age']==24)
# print(df.loc[filt,'position'])


s = [
    {'employee_id': 3, 'name': 'Bob', 'department': 'Operations', 'salary': 48675},
    {'employee_id': 90, 'name': 'Alice', 'department': 'Sales', 'salary': 11096},
    {'employee_id': 9, 'name': 'Tatiana', 'department': 'Engineering', 'salary': 33805},
    {'employee_id': 60, 'name': 'Annabelle', 'department': 'InformationTechnology', 'salary': 37678},
    {'employee_id': 49, 'name': 'Jonathan', 'department': 'HumanResources', 'salary': 23793},
    {'employee_id': 43, 'name': 'Khaled', 'department': 'Administration', 'salary': 40454}
]
df = pd.DataFrame(s)

print(df.iloc[0:4])
