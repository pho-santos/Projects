from tabulate import tabulate
import pandas as pd
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
    employee_list_corrected = []
    for d in employee_list:
        new_dict = {
            "Full Name" : d["Full Name"],
            "Position" : d["Position"],
            "Separation Date" : d["Separation Date"]
            }
        employee_list_corrected.append(new_dict)

df = pd.DataFrame(employee_list_corrected, columns = ["FULL NAME", "POSITION", "SEPARATION DATE"])

def num_get():
    while True:
        try:
            num = input('''Please, input one of the options below:
                        0 - Filter by LAST NAME
                        1 - Filter by POSITION
                        2 - Filter by SEPARATION DATE\n''')
            if num.isnumeric:
                num = int(num)
                if num in [0, 1, 2]:
                    return num
                else:
                    print('Please, input 0, 1 or 2.')
        except:
            print('Please, input 0, 1 or 2.')

def record_filter(num):
    collumns = ["FULL NAME", "POSITION", "SEPARATION DATE"]
    use_filter = collumns[num]
    filtered_df = df.loc[df[use_filter]]
    print(f"Dataframe: \n, {df}")
