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

# Sorting OR indexing OR grouping
# Replacing missing values OR dropping duplicates
# Looping OR itterows
# Merging dataframes
# Use functions
# Numpy
# Dictionary OR list
# 2 Visualizations

# first visualization. Attrition X job satisfaction, grouped by daily rate
# Remove any with empty daily rate
visOne = attrition.dropna(subset=['Age'])

# sns.set_style("whitegrid")
# g = sns.lmplot(x="Age", y="DailyRate", data=visOne, aspect=2)
# g = (g.set_axis_labels("Age","Daily Rate").set(xlim=(18, 60), ylim=(0, 1500)))
# plt.title("Daily Rate by Age")
# plt.show()

# Draw a nested barplot by species and sex
g = sns.catplot(
    data=visOne, kind="bar",
    x="Department", y="MonthlyIncome", hue="Attrition",
    ci="sd", palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("", "Monthly Income")
g.legend.set_title("")
plt.show()