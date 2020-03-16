import csv
List = []
Australia = []
fileName = 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
dailyCumalativeCount = []
with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        List.append(row)

print(len(List))

for x in range(len(List)):
    if List[x][1] == "Australia":
        Australia.append(List[x])

for x in range(len(Australia)):
    print(Australia[x])

#Get the daily summary
print(len(Australia[0]))

for x in range(len(Australia[0])-4):
    count = int(Australia[0][x+4])
    count += int(Australia[1][x+4])
    count += int(Australia[2][x+4])
    count += int(Australia[3][x+4])
    count += int(Australia[4][x+4])
    count += int(Australia[5][x+4])
    count += int(Australia[6][x+4])
    count += int(Australia[7][x+4])
    dailyCumalativeCount.append(count)

print(dailyCumalativeCount)
f = open("index.html", "w+")
html = '<html>\n'
html += '  <head>\n'
html += '    <script src="https://www.gstatic.com/charts/loader.js" type="text/javascript"></script>\n'
html += '    <script type="text/javascript">\n'
html += "        google.charts.load('current', {'packages':['line']});\n"
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
#html += "        [1,  37.8, 80.8, 41.8],\n"
#html += "        [14,  4.2,  6.2,  3.4]\n"
for x in range(len(dailyCumalativeCount)-2):
    html += "        [" + str(x+1) + "," + str(dailyCumalativeCount[x]) + "],\n"
html += "        [" + str(len(dailyCumalativeCount)-1) + "," + str(dailyCumalativeCount[len(dailyCumalativeCount)-1]) + "]\n"
html += "      ]);\n"
html += "      var options = {\n"
html += "        chart: {\n"
html += "          title: 'Cumalative Australian Cases of novel Corona virus',\n"
html += "          subtitle: ''\n"
html += "        },\n"
html += "        width: 900,\n"
html += "        height: 500\n"
html += "      };\n"
html += " \n"
html += "      var chart = new google.charts.Line(document.getElementById('linechart_material'));\n"
html += " \n"
html += "      chart.draw(data, google.charts.Line.convertOptions(options));\n"
html += "    }\n"
html += "    </script>\n"
html += "  </head>\n"
html += "  <body>\n"
html += '    <div id="linechart_material" style="width: 900px; height: 500px"></div>\n'
html += '  </body>\n'
html += '</html>\n'
f.write(html)
f.close()

print(html)
