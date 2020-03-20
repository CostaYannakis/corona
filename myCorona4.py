import csv
import math
List = []
Australia = []
country = []
countries = []
fileName = 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
dailyCumalativeCount = []
growthFactor = []
daysNonCumulative = []
logofdaysNonCumulative =[]


def readingcsv(thefile,thecount):
    with open(thefile) as csv_file1:
        csv_reader1 = csv.reader(csv_file1, delimiter=',')
        line_count1 = 0

        for row1 in csv_reader1:
            List.append(row1)
        return List


readingcsv(fileName, 0)
print(len(List))



def manipulatethelist(myList,thecountry):
    for x in range(len(myList)):
        if myList[x][1] == thecountry:
            country.append(myList[x])
    return country


def thedailycumulative(mycountry):

    for y in range(len(mycountry[0]) - 4):
        count = 0
        for z in range(len(mycountry)):
            count += int(mycountry[z][y + 4])
        dailyCumalativeCount.append(count)
    return dailyCumalativeCount


manipulatethelist(List, "Spain")
thedailycumulative(country)


# for x in range(len(country)):
#    print(country[x])
# Get the daily summary
# print(len(country))



print(dailyCumalativeCount)
f = open("index.html", "w+")
html = '<html>\n'
html += '  <head>\n'
html += '    <script src="https://www.gstatic.com/charts/loader.js" type="text/javascript"></script>\n'
html += '    <script type="text/javascript">\n'
html += "        google.charts.load('current', {'packages':['corechart', 'line']});\n"
html += "      google.charts.setOnLoadCallback(drawChart);\n"
html += " \n"
html += "    function drawChart() {\n"
html += " \n"
html += "      var data = new google.visualization.DataTable();\n"
html += "      data.addColumn('number', 'Day');\n"
html += "      data.addColumn('number', 'Current Cases');\n"

html += " \n"
html += " \n"
html += "      data.addRows([\n"

for x in range(len(dailyCumalativeCount)-2):
    html += "        [" + str(x+1) + "," + str(dailyCumalativeCount[x]) + "],\n"
html += "        [" + str(len(dailyCumalativeCount)-1) + "," + str(dailyCumalativeCount[len(dailyCumalativeCount)-1]) + "]\n"
html += "      ]);\n"
html += "      var options = {\n"
html += "        chart: {\n"
html += "          title: 'Cumalative Australian Cases of novel Corona virus',\n"
html += "        },\n"
html += "        width: 900,\n"
html += "        height: 500\n"
html += "      };\n"

html += "var logOptions = {\n"
html += "title: 'Cumalative Australian Cases of novel Corona virus',\n"
html += "\n"
html += "						legend: 'none',\n"
html += "width: 450,\n"
html += "height: 500,\n"
html += " hAxis: {\n"
html += "  title: 'Date'\n"
html += "},\n"
html += "vAxis: {\n"
html += "  title: 'Population (millions)',\n"
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
html += '    <div id="linechart_material" style="width: 900px; height: 500px"></div>\n'
html += '    <div id="log_div" style="width: 900px; height: 500px"></div>\n'
html += '  </body>\n'
html += '</html>\n'
f.write(html)
f.close()

print(html)
print(len(dailyCumalativeCount))

for i in range(len(dailyCumalativeCount)-1):
    daysNonCumulative.append(dailyCumalativeCount[i+1]-dailyCumalativeCount[i])


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


print(daysNonCumulative)
print(dailyCumalativeCount)





