import csv
from os import access
import pandas as pd

file = pd.read_csv('totalstars.csv')
del file["luminosity"]
del file["radius1"]
del file["mass1"]
del file["starnames1"]
del file["distance1"]
del file["1"]
file.to_csv("clean.csv")