import pandas as pd

data = []
df = pd.read_excel('data.xlsx', usecols='B:C')
# print(df.head)
# for sheet_name, df in df.items():
#     print(df.head())
for i in range(len(df)):
    # print(i)
    # print(df.iloc[i]["Unnamed: 1"])
    # data.append(df.iloc[i]["Unnamed: 2"])
    # dt = datetime(df.iloc[i]["Unnamed: 2"]).strftime("%d.%m.%y")
    try:
        name = df.iloc[i]["Unnamed: 1"]
        birthdate = df.iloc[i]["Unnamed: 2"]
        print(name)
        print(birthdate)
        # print(pd.to_datetime((df.iloc[i]["Unnamed: 2"])).strftime("%d.%m.%y"))
    except BaseException as e:
        print(f"{e.__class__.__name__}: {e}")
        pass
