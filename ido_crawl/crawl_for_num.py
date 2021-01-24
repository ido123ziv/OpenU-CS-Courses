import requests
import re

url = "https://www.openu.ac.il/courses/"
end = ".htm"

previous_knowledge = "ידע קודם דרוש:"
recommended_knowledge = "ידע קודם מומלץ:"
this_is_a_must = "תנאי קבלה:"

def get_course_dependencies_unparsed(course):
    new_url = url + f"{course}" + end
    response = requests.get(new_url)
    print(response)
    # text = response.content.decode("windows-1255").split('\n')
    text = response.text.split('\n')
    for line in text:
        if previous_knowledge in line or recommended_knowledge in line or this_is_a_must in line:
            return line
    return ""


def get_course_dependencies(course):
    print(f"#{course}")
    unparsed = get_course_dependencies_unparsed(course)
    exp = "<.*?>"
    to_delete = re.findall(exp, unparsed)
    for d in to_delete:
        unparsed = unparsed.replace(d, '')
    # dependencies = [x for x in output if x]
    dependencies ={}
    regex_experssion_for_content = ".*?\."
    must = re.search(this_is_a_must + regex_experssion_for_content, unparsed)
    if must:
        must1 = must.group().replace(this_is_a_must, '')
        dependencies["must"] = must1
    pre = re.search(previous_knowledge + regex_experssion_for_content, unparsed)
    if pre:
        pre1 = pre.group().replace(previous_knowledge, '')
        dependencies["previous"] = pre1
    rec = re.search(recommended_knowledge + regex_experssion_for_content, unparsed)
    if rec:
        rec1 = rec.group().replace(recommended_knowledge, '')
        dependencies["recommended"] = rec1
    return dependencies

#
x= get_course_dependencies("20425")
pass
# print(x)

#
# def get_course_dependencies(course):
#     unparsed = get_course_dependencies_unparsed(course)
#     output = []
#     first_cut = unparsed.split('</a>')
#     second_cut = "\r".join(first_cut).split('>')
#     for cut in second_cut:
#         cut = cut.split('\r')
#         # print(cut)
#         for part in cut:
#             if len(cut) > 1:
#                 if '>' not in part and '<' not in part:
#                     output.append(part)
#     dependencies = [x for x in output if x]
#     return dependencies