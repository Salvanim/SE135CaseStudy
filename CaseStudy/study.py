import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

#pulls data form college grad and poverty rate csv files
collegeGrad = pd.read_csv("CaseStudy/college_graduates.csv")
povertyRate = pd.read_csv("CaseStudy/poverty_rate.csv")

#appends data from college grad names and changes to arrays
collegeGradCounty = []
collegeGradState = []
collegeChange = []

for row in collegeGrad.iterrows():
  if str(row[1]["Change_in_Fraction_of_College_Graduates"]) != 'nan' and str(row[1]['Name']) != 'nan':
    #filters out empty values
    collegeGradCounty.append(str(row[1]['Name']).split(", ")[0])
    collegeGradState.append(str(row[1]['Name']).split(", ")[1])
    collegeChange.append(row[1]["Change_in_Fraction_of_College_Graduates"])

#appends data from poverty rate names and changes to arrays
povertyRateCounty = []
povertyRateState = []
povertyChange = []

for row in povertyRate.iterrows():
  #filters out empty values
  if str(row[1]["Change_in_Poverty_Rate"]) != 'nan' and str(row[1]['Name']) != 'nan':
    povertyRateCounty.append(str(row[1]['Name']).split(", ")[0])
    povertyRateState.append(str(row[1]['Name']).split(", ")[1])
    povertyChange.append(row[1]["Change_in_Poverty_Rate"])

#Converts arrays back to dataframes
collegeGrad = pd.DataFrame.from_dict({
    "County": collegeGradCounty,
    "State" : collegeGradState,
    "Change": collegeChange
})

povertyRate = pd.DataFrame.from_dict({
    "County": povertyRateCounty,
    "State" : povertyRateState,
    "Change": povertyChange
})

#gets different state and sorting them.
states = list(set(collegeGrad['State']))
states.sort()
changes = []
averages = []

#loops through collegegrad to calculate the average and stores in averages list
for state in states:
  for gradIndex in range(len(collegeGrad)):
    if str(collegeGrad.iloc[gradIndex]['State']) == state:
      changes.append(collegeGrad.iloc[gradIndex]['Change'])
  averages.append((sum(changes)/len(changes)))
  changes = []


# list to store changes in poverty for each state and store the average change
povertyChanges = []
povertyAverages = []

#loop to calcualte average change for each state
for povertyState in states:
  for povertyIndex in range(len(povertyRate)):
    if str(povertyRate.iloc[povertyIndex]['State']) == povertyState:
      povertyChanges.append(povertyRate.iloc[povertyIndex]['Change'])
  povertyAverages.append((sum(povertyChanges)/len(povertyChanges))*-1)
  povertyChanges = []

#creating dataframe with columns for state, average changes in graduates and poverty rate
changeComparision = pd.DataFrame.from_dict({
    "State": states,
    "GraduateChange": averages,
    "PovertyChange": povertyAverages
})

#using plotly.express to create a scatter plot, shows relationship 
#between average change in poverty rate and average change in college graduates
fig = px.scatter(changeComparision, 
                  x="PovertyChange", 
                  y="GraduateChange", 
                  text="State", 
                  trendline="lowess",
                  title="Change in Graduates vs Change in Poverty per state", 
                  labels={"PovertyChange": "Change in Poverty", "GraduateChange": "Change in Graduates", "State": "States"})
fig.update_traces(textposition='top center')

#fig.write_image("figureImage.jpg")
fig.write_html('figurePage.html')