tables = []

for n in range(0,13):
    table = []
    for num in range(1,13):
        table.append(n * num)
    tables.append(table)

for table in tables:
    print(table)

