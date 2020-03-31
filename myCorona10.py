import csv
import math
import re
import requests
from scraper import *
from modules import *
import datetime

currentDT = datetime.datetime.now()
List = []
Australia = []
country = []
countriesdailyCumalativeCount = []
countriesdailyCumalativeCount.clear()
fileName = 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
dailyCumalativeCount = []
growthFactor = []
daysNonCumulative = []
logofdaysNonCumulative =[]
htmlcode1 = ""
statecounts = []
noduplicatescountries = []



newlist=readingcsv(fileName)


allcountries = getcountries(newlist)
countries = cleancountries(allcountries)

countriesdata = []


smalllist = []
summed = []
count=0
#########################
URL = 'https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/coronavirus-covid-19-current-situation-and-case-numbers'
page = requests.get(URL)
a = str(page.content)
statecounts = []

act = '<p>Australian Capital Territory'
queensland = '<p>Queensland'
nsw = '<p>New South Wales'
vic = '<p>Victoria'
nt = '<p>Northern Territory'
tas = '<p>Tasmania'
wa = '<p>Western Australia'
sa = '<p>South Australia'
states = ['<p>Australian Capital Territory', '<p>Queensland', '<p>New South Wales', '<p>Victoria', '<p>Northern Territory', '<p>Tasmania', '<p>Western Australia', '<p>South Australia']
charactercountuntilaction = [22, 17, 17, 17, 17, 17, 17, 17]

######################### Scraper Data #####################################

URL = 'https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/coronavirus-covid-19-current-situation-and-case-numbers'
page = requests.get(URL)
a = str(page.content)
statecounts1 = []

act = '<p>Australian Capital Territory'
queensland = '<p>Queensland'
nsw = '<p>New South Wales'
vic = '<p>Victoria'
nt = '<p>Northern Territory'
tas = '<p>Tasmania'
wa = '<p>Western Australia'
sa = '<p>South Australia'
states = ['<p>Australian Capital Territory', '<p>Queensland', '<p>New South Wales', '<p>Victoria', '<p>Northern Territory', '<p>Tasmania', '<p>Western Australia', '<p>South Australia']
charactercountuntilaction = [22, 17, 17, 17, 17, 17, 17, 17]

######################################################################################################################################



def manipulatethelist(myList,thecountry):
    country.clear()
    for x in range(len(myList)):
        if myList[x][1] == thecountry:
            country.append(myList[x])
    return country


#manipulatethelist(newlist, 'Australia')
print(country)
def thedailycumulative(mycountry):
    dailyCumalativeCount.clear()
    for y in range(len(mycountry[0]) - 4):
        count = 0
        for z in range(len(mycountry)):
            if (mycountry[z][y + 4]) == '':
                count += 0
            else:
                count += int(mycountry[z][y + 4])


        dailyCumalativeCount.append(count)
    return dailyCumalativeCount



def function1(country1,thelist):
    manipulatethelist(thelist, country1)
    thedailycumulative(country)
    A = dailyCumalativeCount[:]
    countriesdailyCumalativeCount.append(A)

for them in countries:
    function1(them,newlist)

print(countriesdailyCumalativeCount[6])

print(countries)


for i in range(len(dailyCumalativeCount)-1):
    daysNonCumulative.append(dailyCumalativeCount[i+1]-dailyCumalativeCount[i])


f = open("index.html", "w+")
html = '<html>\n'
html += '  <head>\n'
style = mycss()
html += style
html += '    <script src="https://www.gstatic.com/charts/loader.js" type="text/javascript"></script>\n'
html += '    <script type="text/javascript">\n'
map = mapjavascript()
html += map
html += "        google.charts.load('current', {'packages':['corechart', 'line']});\n"
html += "      google.charts.setOnLoadCallback(drawChart);\n"
html += " \n"
html += "    function drawChart() {\n"
html += " \n"
def datatohtml(countrynumber):
    global htmlcode1
    htmlcode1 = ""
    htmlcode1 += "      var data = new google.visualization.DataTable();\n"
    htmlcode1 += "      data.addColumn('number', 'Day');\n"
    htmlcode1 += "      data.addColumn('number' );\n"
    htmlcode1 += " \n"
    htmlcode1 += " \n"
    htmlcode1 += "      data.addRows([\n"

    for x in range(len(countriesdailyCumalativeCount[countrynumber])-2):
        htmlcode1 += "        [" + str(x+1) + "," + str(countriesdailyCumalativeCount[countrynumber][x]) + "],\n"
    htmlcode1 += "        [" + str(len(countriesdailyCumalativeCount[countrynumber])-1) + "," + str(countriesdailyCumalativeCount[countrynumber][len(countriesdailyCumalativeCount[countrynumber])-1]) + "]\n"
    htmlcode1 += "      ]);\n"
    return htmlcode1
datatohtml(8)

html += " \n"

html += htmlcode1

html += "      var options = {\n"
html += "backgroundColor: '#C1C1C1',\n"
html += "colors: ['3467CC'],\n"
html += " hAxis: {\n"
html += "       gridlineColor: '#FFFF00'\n"
html += "    },\n"
html += "chart: {titlePosition: 'none' },\n"

html +=" trendlines: {\n"
html += "           0: {\n"
html += "             type: 'polynomial',\n"
html += "             degree: 3,\n"
html += "             visibleInLegend: true,\n"
html += "           }\n"
html += "         }\n"
html += "      };\n"

html += "var logOptions = {\n"
html += "backgroundColor: '#C1C1C1',\n"
html += "title: 'Log: Cumulative Australian Cases of novel Corona virus',\n"
html += "titlePosition: 'none',\n"
html += "						legend: 'none',\n"

html += " hAxis: {\n"
html += "  title: 'Day'\n"
html += "},\n"
html += "vAxis: {\n"

html += "  scaleType: 'log',\n"
html += "  ticks: [0, 10, 100, 1000, 10000]\n"
html += "}\n"
html += "};\n"





html += " \n"
html += "      var chart = new google.charts.Line(document.getElementById('linechart_material'));\n"
html += " \n"
html += "      chart.draw(data, google.charts.Line.convertOptions(options));\n"
html += "   var logChart = new google.visualization.LineChart(document.getElementById('log_div'));\n"
html += "      logChart.draw(data, logOptions);\n"


html += "    }\n"
html += "    </script>\n"
html += "  </head>\n"
html += "  <body>\n"
html += "<h1>Covid-19 Analysis: Australia</h1>"
html +=  "<p>Cumulative Cases, update: <strong>" + newlist[0][len(newlist[1])-1] + "</strong></p>\n"
html +=  "<p>Total Cases: <strong><font color='red'>" + str(countriesdailyCumalativeCount[8][len(countriesdailyCumalativeCount[8])-1]) + "</font></strong></p>"
html += '<table style="width:100%">\n'
html += '  <tr>\n'
html += '   <td> <div id="linechart_material" style="width: 750px; height: 400px;display: inline-block"></td>\n'
html += '  <td> <div id="log_div" style="width: 750px; height: 400px;display: inline-block"></td>\n'
html += '  </tr>\n'
html += '</table>\n'




html += '    <p><div id="linechart_material" style="width: 900px; height: 500px;display: inline-block"></div></p><br>\n'
html +=  "<p>Log Cumulative Cases, update: " + newlist[0][len(newlist[1])-1] + "</p>\n"
html += '    <p><div id="log_div" style="width: 900px; height: 500px;display: inline-block"></p><br></div>\n'
html += mapscripthtml()
html += '  </body>\n'
html += '</html>\n'
f.write(html)
f.close()

print(html)




for i in range(len(dailyCumalativeCount)-1):
    if dailyCumalativeCount[i] == 0:
        growthFactor.append(0)
    else:
        growthFactor.append(dailyCumalativeCount[i+1]/dailyCumalativeCount[i])

#for i in range(len(daysNonCumulative)):
#    if daysNonCumulative[i] == 0:
#        daysNonCumulative[i] = 0.9
#
#    logofdaysNonCumulative.append(math.log(daysNonCumulative[i], 10))
#
#math.log(0.01, 10)



#print(countriesdailyCumalativeCount[0])
#print(countriesdailyCumalativeCount[1])





print((countriesdailyCumalativeCount[6][len(countriesdailyCumalativeCount[6])-1]))




print(statecounts)

for i in range(len(states)):
    get_cumulative_state(states[i],i,statecounts1)

print(statecounts1)


#createfile('data3', statecounts1, str(currentDT))

#print(countriesdailyCumalativeCount[8])


#print(countriesdailyCumalativeCount)

#print((countriesdailyCumalativeCount[8]))
a1=countriesdailyCumalativeCount[8]
a2=[2,5,10,10,998,0,12,11,20000]
print(countries.index("Australia"))
b=createdayslistforpowerBI(countriesdailyCumalativeCount[8])
c=addheaderList("Count" ,countriesdailyCumalativeCount[8])
d=createcsvfrom2lists("mycsv.csv",b,c)


print(countriesdailyCumalativeCount[8])
countriesdailyCumalativeCount[8].remove('Count')
e=dailycases(countriesdailyCumalativeCount[8])

e = e[49:]
print(e)
f=growthrate(e)
print(f)

g=addheaderList("Growth",f)
print(g)
Daysforgrowth=createdayslistforpowerBI(g)
del Daysforgrowth[-1]
createcsvfrom2lists("growth1.csv", Daysforgrowth, g)

gw21=Daysforgrowth[len(Daysforgrowth)-7:len(Daysforgrowth)]
gw21=addheaderList("Days",gw21)
gw22=f[len(f)-7:len(f)]
gw22=addheaderList("Growth",gw22)
createcsvfrom2lists("growth2.csv", gw21, gw22)

gw31=Daysforgrowth[len(Daysforgrowth)-4:len(Daysforgrowth)]
gw31=addheaderList("Days",gw31)
gw32=f[len(f)-4:len(f)]
gw32=addheaderList("Growth",gw32)
createcsvfrom2lists("growth3.csv", gw31, gw32)




i=dailycases(countriesdailyCumalativeCount[8])
print(i)
daysfordaily=createdayslistforpowerBI(i)
addheaderList("Cases",i)
createcsvfrom2lists("dailycases.csv", daysfordaily, i)