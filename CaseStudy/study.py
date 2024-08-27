
import pandas as pd
import matplotlib.pyplot as plt


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

states = list(set(collegeGrad['State']))
changes = []
averages = []
for stateIndex in range(len(states)):
  for gradIndex in range(len(collegeGrad)):
      print(stateIndex)
      if str(collegeGrad.iloc[gradIndex:gradIndex+1]['State']).split("    ")[1] == str(states[stateIndex]):
        changes.append(collegeGrad.iloc[gradIndex:gradIndex+1]['Change'])
  averages.append(sum(changes)/len(changes))
  changes = []
print(averages)


#collegeGrad = collegeGrad.iloc[:10]
#collegeGrad.plot(x="State", y="Change", kind="bar")
#xticks=collegeGrad['County']
#plt.show()
