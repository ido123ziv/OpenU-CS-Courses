text = """<p><img src="gifs/triangle.jpg" width="5" height="10" alt="" border="0"> ידע קודם דרוש: צמד הקורסים <a href="http://www.openu.ac.il/courses/20474.htm" target="_blank">חשבון אינפיניטסימלי 1</a> (‏&#xFEFF;20474‎)‏ + <a href="http://www.openu.ac.il/courses/20475.htm" target="_blank">חשבון אינפיניטסימלי 2</a> (‏&#xFEFF;20475‎)‏ או הקורס <a href="http://www.openu.ac.il/courses/20406.htm" target="_blank">חשבון דיפרנציאלי ואינטגרלי א</a>.<span class="heara">2</span></p>"""
print(text)
print()
first_cut = (text.split('>'))
for part in first_cut:
    if '<' in part:
        print(part.split('<'))

print("@@@@@@@@@@@@@@@@@@@@@@@\n\n\n")

output = []
seconed_try = text.split('</a>')
print(seconed_try)
second_cut = "\r".join(seconed_try).split('>')
print(f"{second_cut}" + "\n")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
for cut in second_cut:
    cut = cut.split('\r')
    # print(cut)
    for part in cut:
        if len(cut) > 1:
            if '>' not in part and '<' not in part:
                output.append(part)

print(output)
# third_cut = " ".join((second_cut)).split('\r')
# print(f"{third_cut}" + "\n")
# forth_cut = " ".join(third_cut).split('\r')
# print(f"{forth_cut}\n")

