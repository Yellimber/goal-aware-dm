import os
import csv

dir = os.getcwd() + '\\tagged_diags'
with open(os.getcwd() + "\\results.txt", 'r', encoding = "utf-8") as resf:
    with open(os.getcwd() + "\\pretty_res.txt", 'w', encoding = "utf-8") as pretty:
        for dialog in os.listdir(dir):
            with open(dir + '\\' + dialog, 'r', encoding = "utf-8") as f:
                reader = csv.DictReader(f)
                fldnms = reader.fieldnames
                for row in reader:
                    pretty.write("{} {} {}".format(row["speaker"], row["text"], resf.readline()))
                pretty.write('\n')
    print("fin")
