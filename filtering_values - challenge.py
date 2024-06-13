#input: num with spaces
#output: list without spaces 
import pandas as pd
df = pd.read_csv('employees_date.csv')

def filter_even_rows(dataf, column_name):
    even_rows = dataf[dataf.index % 2 == 0]
    column_values = even_rows[column_name]
    print(f'Your even numbers inputed are {even_rows}')

print("I will help you get values  .")
filter_even_rows(df, "Name")




