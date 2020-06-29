from collections import Counter, OrderedDict
import datetime
now = datetime.datetime.now()


resfile = open("otto_" + "topic-25349116_38313695" + ".csv", 'r', encoding='utf-8', errors='ignore')
links = []
m = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
links_by_year = {str(b + " " + str(a)): [] for a in range(2010,2021) for b in m}

avatars = {}
# a_name, a_href, dattime[0], dattime[1], clear_text, avatar, text, media

for line in resfile:
    data = line.split("\t")
    links.append(data[1])

    try:
        year = data[2].split(" ")[2]
    except:
        year = str(now.year)

    try:
        month = data[2].split(" ")[1]
    except:
        month = m[now.month - 1]

    try:
        avatars[data[1]]
    except:
        avatars[data[1]] = [data[5],data[0]]



    links_by_year[month + " " + year].append(data[1])


c = Counter(links).most_common(100)
print(c)

html_file = open("result.html", "w", encoding="utf-8")
html_file.write("<div style='width: 100%;'>")

for cc in c:
    print(cc)
    html_file.write("<div style='width: 19%; display:inline; text-align: center; float: left;'>"
                    "<a href='" + cc[0] + "'>" + "<p align='center'>" + avatars[cc[0]][1] + "</p>"
                    "<p align='center'>" + "<img src='" + avatars[cc[0]][0] + "' width='150'>" + "</a></p>"
                    "<p align='center'>" + str(cc[1]) + "</p>"
                    "</div>")


html_file.write("</div>")
for yy in range(2018,2021):
    for mm in m:
        if links_by_year.get(mm + " " + str(yy)):
            print(mm + " " + str(yy))
            c2 = Counter(links_by_year.get(mm + " " + str(yy))).most_common(100)
            print(c2)