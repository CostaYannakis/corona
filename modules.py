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
