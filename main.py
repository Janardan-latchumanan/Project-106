import numpy as np;
import csv;
import plotly.express as px;

def getDataSource(data):
	marksInPercentage = [];
	daysPresent = [];
	with open(data) as f:
		csv_reader = csv.DictReader(f);
		for row in csv_reader:
			marksInPercentage.append(float(row["Marks In Percentage"]))
			daysPresent.append(float(row["Days Present"]))
	return{"x":marksInPercentage,"y":daysPresent}

def findCorrelation(dataSource):
	correlation = np.corrcoef(dataSource["x"],dataSource["y"])
	print("correlation between Percentage and Days : " , correlation[0,1])

def plotFigure(data_path):
	with open(data_path)as f:
		df = csv.DictReader(f)
		fig = px.scatter(df,x="Days Present",y="Marks In Percentage")
		fig.show();

def setup():
	data_path = "data1.csv";
	dataSource = getDataSource(data_path)
	findCorrelation(dataSource);
	plotFigure(data_path)


setup();