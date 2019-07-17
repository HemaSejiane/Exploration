import os
import csv
from collections import defaultdict

column = defaultdict(list)
def gettablelist():
    extract_command= "(/usr/bin/impala-shell -i impala.prod.avvo.com -B -q '"'show tables in src;'"') > gettablelist.txt"
    os.system(extract_command)
    with open("gettablelist.txt","r") as statlist:
        for i in statlist:
            os.system("(/usr/bin/impala-shell -i impala.prod.avvo.com -B --print_header --output_delimiter=',' -q \"show table stats i;\") > gettablestats.csv")

    with open("gettablestats.csv","r") as tablestats:
        reader=csv.DictReader(tablestats)
        for row in reader:
            for (k,v) in row.items():
                column[k].append(v)

    print(column())

if __name__=='__main__':
    gettablelist()

