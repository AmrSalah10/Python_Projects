import json
import csv
import sys

def convertor():
    if len(sys.argv) < 3:
        return "Args should be 3!"

    # Open json file from command line
    with open(sys.argv[1]) as json_file:
        data = json_file.read()

    # Convert json data into python dictionary
    py_dict = json.loads(data)

    # Extract keys of dict as headers
    headers = list(py_dict[0])

    # Create csv file from command line, Fill it with data
    with open(sys.argv[2],'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for cell in py_dict:
            writer.writerow(cell)

    return("Done!")

print(convertor())
