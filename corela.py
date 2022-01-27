import numpy as np
import csv

def getDatasource(datapath):
    days = []
    marks = []
    with open(datapath) as f:
        reader = csv.DictReader(f)

        for i in reader:
            days.append(float(i["Days Present"]))
            marks.append(float(i["Marks In Percentage"]))

    return {"x":days,"y":marks}

def findCorr(datasource):
    corr = np.corrcoef(datasource["x"],datasource["y"])
    print("The correlation is: ",corr[0,1])

def setup():
    datapath = "SDmarks.csv"
    datasource = getDatasource(datapath)
    findCorr(datasource)

setup()
