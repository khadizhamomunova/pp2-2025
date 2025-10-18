import csv

input = 'John,"New York, USA",25,"Student"'
fields = next(csv.reader([input]))
fields = [str(f) for f in fields]
print(fields)
