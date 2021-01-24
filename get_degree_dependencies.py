import json
from ido_crawl import crawl_for_num
import csv

with open('course-num-assets\course-num.json', 'r') as num_list:
    numbers = json.load(num_list)

print(f"numbers are here {numbers}")


dependencies_list = []
num_object = {}

numbers_list = numbers["numbers_list"]
for number in numbers_list:
    dependencies = crawl_for_num.get_course_dependencies(number)
    num_object["number"] = number
    if "must" in dependencies.keys():
        num_object["must"] = dependencies["must"]
    else:
        num_object["must"] = ""
    if "previous" in dependencies.keys():
        num_object["previous"] = dependencies["previous"]
    else:
        num_object["previous"] = ""
    if "recommended" in dependencies.keys():
        num_object["recommended"] = dependencies["recommended"]
    else:
        num_object["recommended"] = ""
    dependencies_list.append(num_object)
    num_object = {}

print(f"we got the dependencies dude!")

with open('course-num-assets\courses-dependencies.json', 'w', encoding='utf8') as result:
    json.dump(dependencies_list, result, indent=4, ensure_ascii=False)


print("throw it to json")

with open('dependencies.csv', 'w', newline='', encoding='utf8') as csvfile:
    mywriter = csv.writer(csvfile, delimiter=',',
                          quotechar='|', quoting=csv.QUOTE_MINIMAL)
    mywriter.writerow(["מספר", "חובה", "דרוש", "מומלץ"])
    for dep in dependencies_list:
        mywriter.writerow(list(dep.values()))

print("finish")
# print(numbers_list)
pass