#insall krna pdega - openpyxl package

#input excel file
#load excel in df
import pandas as pd
df = pd.read_excel("C:\\Users\\ADARSH MISHRA\\OneDrive\\Documents\\RealExcel.xlsx")

print("\nOur dataframe:\n", df)

#head Excel data

#display n rows
print('\n Top head \n')
d=df.head()
print('\n Top 5 rows:\n',d)

#if want to 2 only from head

print('\n Top 2 head \n')
dHead=df.head(2)
print('\n Top 2 rows:\n',dHead)

#if want to  only from tail

print('\n Top 2 Tails \n')
dTail=df.tail(2)
print('\n Top 2 Tail:\n',dTail)