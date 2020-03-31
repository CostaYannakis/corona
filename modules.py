# Get All countries from the csv this is in the 2nd column

import csv

def getcountries(myList):
    thecountries = []
    for x in range(len(myList)):
        if x != 0:
            thecountries.append(myList[x][1])

    return thecountries


# Removes duplicates
def cleancountries(x):
  return list(dict.fromkeys(x))

#Get Raw data into a list
def readingcsv(thefile):

    thelist = []
    with open(thefile) as csv_file1:
        csv_reader1 = csv.reader(csv_file1, delimiter=',')
        for row1 in csv_reader1:
            thelist.append(row1)
    return thelist

#Matrix manipulation

def addMatrixElements(matrixA,matrixB):
    elementsAddition = []
    for i in range(len(matrixA)):
        elementsAddition.append(matrixA[i] + matrixB[i])
    return elementsAddition

def manipulatethelist(myList,thecountry):
    country = []
    for x in range(len(myList)):
        if myList[x][1] == thecountry:
            country.append(myList[x])
    return country


def mycss():

    css = '<style>'
    css += 'body {\n'
    css += '  /*background: linear-gradient(90deg, white, gray);*/\n'
    css += '  background-color: #eee;\n'
    css += '}\n\n'

    css += 'body, h1, p {\n'
    css += '  font-family: "Helvetica Neue", "Segoe UI", Segoe, Helvetica, Arial, "Lucida Grande", sans-serif;\n'
    css += '  font-weight: normal;\n'
    css += '  margin: 0;\n'
    css += '  padding: 0;\n'
    css += '  text-align: center;\n'
    css += 'display: inline - block\n'
    css += '}\n\n'

    css += '.container {\n'
    css += '  margin-left:  auto;\n'
    css += '  margin-right:  auto;\n'
    css += '  margin-top: 177px;\n'
    css += '  max-width: 1170px;\n'
    css += '  padding-right: 15px;\n'
    css += '  padding-left: 15px;\n'
    css += '}\n\n'

    css += '.row:before, .row:after {\n'
    css += '  display: table;\n'
    css += '  content: " ";\n'
    css += '}\n\n'

    css += 'h1 {\n'
    css += '  font-size: 48px;\n'
    css += '  font-weight: 300;\n'
    css += '  margin: 0 0 20px 0;\n'
    css += '}\n\n'

    css += '.lead {\n'
    css += '  font-size: 21px;\n'
    css += '  font-weight: 200;\n'
    css += '  margin-bottom: 20px;\n'
    css += '}\n\n'

    css += 'p {\n'
    css += '  margin: 0 0 10px;\n'
    css += '}\n\n'

    css += 'a {\n'
    css += '  color: #3282e6;\n'
    css += '  text-decoration: none;\n'
    css += '}\n'
    css += '</style>\n'

    return css

def mapscripthtml():
    maps = '<p><div id="geochart-colors" style="width: 900px; height: 500px;display: inline-block"></div></p>'
    return maps


def mapjavascript():
    mapsjv="          google.charts.load('current', {\n"
    mapsjv +="        'packages':['geochart'],\n"


    mapsjv +="    'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'\n"
    mapsjv += "});\n"
    mapsjv += "google.charts.setOnLoadCallback(drawRegionsMap);\n"

    mapsjv += "function drawRegionsMap() {\n"
    mapsjv += "var data = google.visualization.arrayToDataTable([\n"
    mapsjv += "['Province',   'rate'],\n"
    mapsjv += "['Victoria', 100], ['New South Wales', -8], ['AU-ACT', 6], ['Queensland', -24],\n"
    mapsjv += "['AU-TAS', 12], ['Western Australia', -3], ['South Australia', 3],\n"
    mapsjv += "['Northern Territory', 200]\n"
    mapsjv += "]);\n"

    mapsjv += "var optionsMAP = {\n"
    mapsjv += "region: 'AU', // Africa\n"
    mapsjv += "colorAxis: {colors: ['#FFFFFF', 'grey', 'black']},\n"
    mapsjv += "backgroundColor: '#81d4fa',\n"
    mapsjv += "datalessRegionColor: 'blue',\n"
    mapsjv += "defaultColor: '#FFFFFF',\n"
    mapsjv += "resolution: 'provinces'\n"
    mapsjv += "};\n"

    mapsjv += "var chart = new google.visualization.GeoChart(document.getElementById('geochart-colors'));\n"
    mapsjv += "chart.draw(data, optionsMAP);\n"
    mapsjv += "};\n"
    return mapsjv

def createfile(filename, list_to_append, the_date_time):
    f = open((filename + ".csv"), "a+")
    f.write(the_date_time + ",")
    for i in range(len(list_to_append)):
        if i == len(list_to_append)-1:
            f.write(list_to_append[i])
        else:
            f.write(list_to_append[i] + ",")
    f.write('\n')
    f.close()

a = [0,1,2,5,10,12,59]
alen = len(a)
newlist =[]
for i in range(alen):
    if i == 0:

        newlist.append(a[i])
        newlist.append(a[i+1]-a[i])
    elif i == alen-1:
        print('end')
    else:
        newlist.append(a[i+1]-a[i])

print(newlist)


#########################################################
# This code extracts the daily cases from cumulative data
#########################################################
def dailycases(mylist):
    mylistlength= len(mylist)
    dailycaselist = []
    for i in range(mylistlength-1):
        if i == 0:
            dailycaselist.append(mylist[i])
            dailycaselist.append(mylist[i+1]-mylist[i])
        elif i == alen-1:
            print('end')
        elif i == alen:
            print('end')
        else:
            dailycaselist.append(mylist[i+1]-mylist[i])
    return dailycaselist

print(dailycases(a))

def createdayslistforpowerBI(myList):
    days = [*range(1, len(myList)+1, 1)]
    days.insert(0, "Days")
    return days

def addheaderList(theheader,thelist):
    thelist.insert(0, theheader)
    return thelist

def createcsvfrom2lists(filename,list1,list2):
    with open(filename, 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(list1)
        thewriter.writerow(list2)
        f.close()

growth = [72, 50, 47, 80, 75, 116, 113, 110, 280, 478, 133, 362, 320, 446, 333]




def growthrate(thelist):
    newgrowthlist = []
    for i in range (len(thelist)):
        if i == 0:
            print("do nothing")
        else:
            newgrowthlist.append((thelist[i]/thelist[i-1]))
    return newgrowthlist




print(growthrate(growth))