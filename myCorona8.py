import csv
import math

from modules import *
List = []
Australia = []
country = []
countriesdailyCumalativeCount = []
countriesdailyCumalativeCount.clear()
fileName = 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
dailyCumalativeCount = []
growthFactor = []
daysNonCumulative = []
logofdaysNonCumulative =[]
htmlcode1 = ""

noduplicatescountries = []



newlist=readingcsv(fileName)


allcountries = getcountries(newlist)
countries = cleancountries(allcountries)

countriesdata = []


smalllist = []
summed = []
count=0




def manipulatethelist(myList,thecountry):
    country.clear()
    for x in range(len(myList)):
        if myList[x][1] == thecountry:
            country.append(myList[x])
    return country


manipulatethelist(newlist, 'Australia')
print(country)
def thedailycumulative(mycountry):
    dailyCumalativeCount.clear()
    for y in range(len(mycountry[0]) - 4):
        count = 0
        for z in range(len(mycountry)):
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

print(countriesdailyCumalativeCount[3])




for i in range(len(dailyCumalativeCount)-1):
    daysNonCumulative.append(dailyCumalativeCount[i+1]-dailyCumalativeCount[i])


f = open("index.html", "w+")
html = '<html>\n'
html += '  <head>\n'
style = mycss()
html += style
html += '    <script src="https://www.gstatic.com/charts/loader.js" type="text/javascript"></script>\n'
html += '    <script type="text/javascript">\n'
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
datatohtml(6)

html += " \n"

html += htmlcode1

html += "      var options = {\n"
html += "backgroundColor: '#000000',\n"
html += "colors: ['red'],\n"
html += " hAxis: {\n"
html += "       gridlineColor: '#FFFF00'\n"
html += "    },\n"
html += "chart: {titlePosition: 'none' },\n"
html += "      };\n"

html += "var logOptions = {\n"
html += "backgroundColor: '#000000',\n"
html += "title: 'Log: Cumulative Australian Cases of novel Corona virus',\n"
html += "titlePosition: 'none',\n"
html += "						legend: 'none',\n"

html += " hAxis: {\n"
html += "  title: 'Date'\n"
html += "},\n"
html += "vAxis: {\n"

html += "  scaleType: 'log',\n"
html += "  ticks: [0, 10, 100, 1000]\n"
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
html +=  "<p>Total Cases: <strong><font color='red'>" + str(countriesdailyCumalativeCount[6][len(countriesdailyCumalativeCount[6])-1]) + "</font></strong></p>"
html += '    <p><div id="linechart_material" style="width: 900px; height: 500px;display: inline-block"></div></p><br>\n'
html +=  "<p>Log Cumulative Cases, update: " + newlist[0][len(newlist[1])-1] + "</p>\n"
html += '    <p><div id="log_div" style="width: 900px; height: 500px;display: inline-block"></p><br></div>\n'
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







