#%% Task[1]: Read random rows from our data
import pandas as pd

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku'],
		'Age':[27, 24, 22, 32, 15],
		'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
		'Qualification':['Msc', 'MA', 'MCA', 'Phd', '10th']}

df = pd.DataFrame(data)
print(df.sample(n=2))

#%% Task[2]: a) Append to an existing CSV file

import pandas as pd

data = {'Name':['A', 'B', 'C', 'D', 'E'],
		'Age':[11, 22, 33, 44, 55],
		'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
		'Qualification':['Msc', 'MA', 'MCA', 'Phd', '10th']        }

df = pd.DataFrame(data)
df.to_csv('1hi.csv', mode='a', header=False, index=False)

#%% Task[2]: b) Append to an existing Excel file

import pandas as pd
from openpyxl import load_workbook

data = {'Name':['A', 'B', 'C', 'D', 'E'],
		'Age':[11, 22, 33, 44, 55],
		'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
		'Qualification':['Msc', 'MA', 'MCA', 'Phd', '10th']        }

df = pd.DataFrame(data) 

FilePath = "1hi.xlsx"
ExcelWorkbook = load_workbook(FilePath)
writer = pd.ExcelWriter(FilePath, engine = 'openpyxl')
writer.book = ExcelWorkbook
df.to_excel(writer, sheet_name = 'new')

writer.save()
writer.close()

#%% Task[4]: Replace values in specific columns pandas with specific values
df = pd.DataFrame({
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica'],
     'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional']
})

df["score"].replace({
    'poor': 8,
    'average': 2,
    'good': 27,
    'exceptional': 4
}, inplace=True)
df

#%% Task[5]: Combine more than 2 dataframes
df = pd.concat( [df1,df2,df3], ignore_index=True )
df
# OR
df4 = pd.merge(df1, df2, how='outer')
df_merge = pd.merge(df4, df3, how='outer')
df_merge