import pandas as pd
from datetime import datetime, timedelta

employee_list = [
    {
        "First Name" : "John",
        "Last Name" : "Johnson",
        "Position" : "Manager",
        "Separation Date" : "2016-12-31"
    },
    {
        "First Name" : "Tou",
        "Last Name" : "Xiong",
        "Position" : "Software Engineer",
        "Separation Date" : "2016-10-05"
        },
    {
        "First Name" : "Michaela",
        "Last Name" : "Michaelson",
        "Position" : "District Manager",
        "Separation Date" : "2015-12-19"
        },
    {
        "First Name" : "Jake",
        "Last Name" : "Jacobson",
        "Position" : "Programmer",
        "Separation Date" : ""
        },
    {
        "First Name" : "Jacquelyn",
        "Last Name" : "Jackson",
        "Position" : "DBA",
        "Separation Date" : ""
        },
    {
        "First Name" : "Sally",
        "Last Name" : "Weber",
        "Position" : "Web Developer",
        "Separation Date" : "2015-12-18"
        }
    ]

for d in employee_list:
    for d in employee_list:
        d["Full Name"] = d["Last Name"] + " " + d["First Name"]
    employee_list_corrected = [{"Full Name" : d["Full Name"], "Position" : d["Position"], "Separation Date" : d["Separation Date"]} for d in employee_list]

df = pd.DataFrame(employee_list_corrected, columns = ["Full Name", "Position", "Separation Date"])

def num_get():
    while True:
        try:
            num = input('''Please, by which collumn you want to filter:
                        0 - Filter by NAME
                        1 - Filter by POSITION
                        2 - Filter by SEPARATION DATE (if it was six months ago or more.)\nInsert number: ''')
            if num.isnumeric and int(num)  in [0, 1, 2]:
                return int(num)
            else:
                print('Please, input 0, 1 or 2.')
        except:
            print('Please, input 0, 1 or 2.')

def record_filter(num):
    try:
        if num in [0, 1]:
            collumns = ["Full Name", "Position"]
            which_collumn = collumns[num]
            filter_value = input(f"Insert the value to filter the collum {which_collumn} by:\n")
            filtered_df = df[df[which_collumn].str.contains(filter_value, na=False, case=False)]
        else:
            df['Separation Date'] = pd.to_datetime(df['Separation Date'], errors='coerce')#Converts the "Separation Date" column to datetime
            reference_date = datetime(2016, 12, 31)
            six_months_prior = reference_date - timedelta(days=6*30)
            filtered_df = df[(df["Separation Date"] <= six_months_prior)]
        print(f"Dataframe: \n, {filtered_df}")
    except Exception as e:
        print(f'An error occurred: {e}.')
    
print(f"Dataframe: \n, {df}")
num = num_get()
record_filter(num)
