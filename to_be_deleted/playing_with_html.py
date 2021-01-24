import requests
import re


def get_html():
    new_url = "https://www.openu.ac.il/courses/20582.htm"

    response = requests.get(new_url)

    with open('html_to_work_with.html', 'w', encoding='utf8') as playground:
        playground.write(response.text)


with open('html_to_work_with.html', 'r', encoding='utf8') as playground:
    text = playground.readlines()

previous_knowledge = "ידע קודם דרוש:"
recommended_knowledge = "ידע קודם מומלץ:"
this_is_a_must = "תנאי קבלה:"


def get_course_dependencies_unparsed():
    for line in text:
        if previous_knowledge in line or recommended_knowledge in line or this_is_a_must in line:
            return line
    return ""


def get_course_dependencies():
    unparsed = get_course_dependencies_unparsed()
    output = []
    x1 = unparsed.rsplit()
    unparsed.replace('<strong>', '')
    unparsed.replace('</strong>', '')
    must = "".join(unparsed.split(this_is_a_must))
    rec = "".join(must.split(recommended_knowledge))
    prev = "".join(rec.split(previous_knowledge))
    first_cut = unparsed.split('</a>')
    second_cut = "\r".join(first_cut).split('>')
    for cut in second_cut:
        cut = cut.split('\r')
        # print(cut)
        for part in cut:
            if len(cut) > 1:
                if '>' not in part and '<' not in part:
                    output.append(part)
    dependencies = [x for x in output if x]
    return dependencies

# print(get_course_dependencies())


def remove_html():
    ido = """  <p><img src="gifs/triangle.jpg" width="5" height="10" alt="" border="0"> תנאי קבלה: עמידה בדרישות ה<strong>אנגלית</strong> ובדרישות <strong>ההדרכה הביבליוגרפית בספרייה</strong>. ידע קודם דרוש: אחד מהקורסים <a href="http://www.openu.ac.il/courses/20425.htm" target="_blank">הסתברות לתלמידי מדעי המחשב</a>, <a href="http://www.openu.ac.il/courses/30203.htm" target="_blank">מבוא לסטטיסטיקה ולהסתברות למדעים</a>, <a href="http://www.openu.ac.il/courses/30111.htm" target="_blank">מבוא לסטטיסטיקה לתלמידי מדעי החברה א</a>, <a href="http://www.openu.ac.il/courses/20416.htm" target="_blank">תורת ההסתברות</a>, וכן הקורס <a href="http://www.openu.ac.il/courses/20407.htm" target="_blank">מבני נתונים ומבוא לאלגוריתמים</a> (‏&#xFEFF;או <a href="http://www.openu.ac.il/courses/20433.htm" target="_blank">מבני נתונים</a>‎)‏. ידע קודם מומלץ: הקורס <a href="http://www.openu.ac.il/courses/20417.htm" target="_blank">אלגוריתמים</a>.</p>
    """
    exp = "<.*?>"
    to_delete = re.findall(exp, ido)
    for  d in to_delete:
        ido = ido.replace(d,'')
    print(ido)


def good_seperators():
    ido = "  תנאי קבלה: עמידה בדרישות האנגלית ובדרישות ההדרכה הביבליוגרפית בספרייה. ידע קודם דרוש: אחד מהקורסים הסתברות לתלמידי מדעי המחשב, מבוא לסטטיסטיקה ולהסתברות למדעים, מבוא לסטטיסטיקה לתלמידי מדעי החברה א, תורת ההסתברות, וכן הקורס מבני נתונים ומבוא לאלגוריתמים (‏&#xFEFF;או מבני נתונים‎)‏. ידע קודם מומלץ: הקורס אלגוריתמים."
    must = re.search(this_is_a_must+".*?\.", ido).group()
    must1 = must.replace(this_is_a_must,'')
    pre = re.search(previous_knowledge + ".*?\.", ido).group()
    rec = re.search(recommended_knowledge + ".*?\.", ido).group()


def check_key_in_dict():
    di = {}
    if "ido" in di.keys():
        print(1)
    else:
        print(0)


# import csv
# with open('dep.csv', 'w', newline='') as csvfile:
#     mywriter = csv.writer(csvfile, delimiter=',',
#                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     mywriter.writerow(["123", "", "asdasdas", "saderwds"])
pass
