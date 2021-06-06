import pandas as pan
import plotly.express as pe

dataFrame = pan.read_csv("copyOfData.csv")

figure = pe.bar(dataFrame, x='date', y='cases')
figure.show()