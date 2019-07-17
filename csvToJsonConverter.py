import csv
import json
import sys

csv_rows=[]
def csvreadjson(csv_file,json_file):
    with open(csv_file,"r") as readcsv:
        reader= csv.DictReader(readcsv)
        for i in reader:
            csv_rows.append(i)
    json_data=json.dumps(csv_rows)
    with open(json_file,"w") as writejson:
        writejson.write(json_data)


if __name__ == '__main__':
    csv_file=sys.argv[1]
    json_file=sys.argv[2]
    csvreadjson(csv_file,json_file)


