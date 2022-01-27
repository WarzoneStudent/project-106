import numpy as np
import csv

def getDatasource(datapath):
    list1 = []
    list2 = []
    with open(datapath) as f:
        reader = csv.DictReader(f)

        for i in reader:
            list1.append(float(i["Coffee in ml"]))
            list2.append(float(i["sleep in hours"]))

    return {"x":list1,"y":list2}

def findCorr(datasource):
    corr = np.corrcoef(datasource["x"],datasource["y"])
    print("The correlation is: ",corr[0,1])

def setup():
    datapath = "coffee.csv"
    datasource = getDatasource(datapath)
    findCorr(datasource)

setup()