import csv
import json

with open('course-num-assets\courses-dependencies.json', 'r', encoding='utf8') as result:
    dependencies_list = json.load(result)

with open('dependencies.csv', 'w', newline='', encoding='utf8') as csvfile:
    mywriter = csv.writer(csvfile, delimiter=',',
                          quotechar='|', quoting=csv.QUOTE_MINIMAL)
    mywriter.writerow(["מספר", "חובה", "דרוש", "מומלץ"])
    for dep in dependencies_list:
        mywriter.writerow(list(dep.values()))