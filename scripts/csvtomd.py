import csv

def toMarkdown(item):
    newTemp = "---"+"\n"+"layout: default"+"\n"+"section: "+item[0]+"\n"+"objectID: "+item[1]+"\n"
    newTemp += "image: /images/"+item[1]+"\n"
    newTemp += "---"+"\n"
    newTemp += "![]({{site.baseurl}}/images/"+item[1]+"){: .img-fluid }\n"
    newTemp += item[2]+"\n"
    newTemp += item[3]+"\n"
    newTemp += item[4]+"\n"
    newTemp += item[5]+"\n"
    return newTemp

with open('../csv/netsuke.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_ALL)
    i = 1
    for row in reader:
        i = i+1
        with open('/Users/danielpett/Documents/GitHub/netsuke/_explore/object-' + str(i) + '.md', 'w') as output:
            output.write(toMarkdown(row))
