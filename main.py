import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import create_engine
import pandas as pd
import seaborn as sns

attrition = pd.read_csv('data/employee_attrition_train.csv')
engine = create_engine('sqlite:///:memory:')
attrition.to_sql('data_table', engine)

# drop any duplicates in the data before any manipulation
attrition.drop_duplicates()

# first visualization. Attrition X job satisfaction, grouped by daily rate
# Remove any with empty daily rate
visOne = attrition.dropna(subset=['MonthlyIncome'])

# sns.set_style("whitegrid")
# g = sns.lmplot(x="Age", y="DailyRate", data=visOne, aspect=2)
# g = (g.set_axis_labels("Age","Daily Rate").set(xlim=(18, 60), ylim=(0, 1500)))
# plt.title("Daily Rate by Age")
# plt.show()

# Draw a nested barplot by species and sex
g = sns.catplot(data=visOne, kind="bar", x="Department", y="MonthlyIncome", hue="Attrition", ci="sd", palette="dark", alpha=.6, height=6)
g.despine(left=True)
g.set_axis_labels("", "Monthly Income")
g.legend.set_title("")
# plt.show()

# Visualization 2
# Average Satisfaction - Environment, Job, Relationship

satisfaction = ["Low", "Medium" "High", "Very High"]

# numpy array with all satisfaction columns from the dataset
visTwo = attrition[['EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction']].to_numpy()

# Sorting OR indexing OR grouping
# Looping OR itterows
# Merging dataframes
# Use functions
# 2 Visualizations

# FIX ME - I should add each row in the 2d array
def add_2_dimensional(data, index):
    sum = 0
    for val in data[index]:
        sum = sum + val
    return sum

# FINISH ME - I should call the function to add the rows and then add them to a new array - this maybe should be a dataframe so we get the merging too
sats = [len(visTwo)]
for i in range(len(visTwo)):
    sats.append(add_2_dimensional(visTwo, i))

print(sats)
