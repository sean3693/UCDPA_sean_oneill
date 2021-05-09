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

# ----------------- Visualization 1 ------------------------
# Create visualization one dataframe
# Remove any with empty daily rate
vis_one_df = attrition.dropna(subset=['MonthlyIncome'])


def subplot_graph(x_axis, y_axis, subplot_location):
    sns.barplot(data=vis_one_df, x=x_axis, y=y_axis, hue="Attrition",
                ci="sd", palette="dark", alpha=.6, ax=subplot_location)


fig1, ax1 = plt.subplots(2, 2, figsize=(12, 8))
subplot_graph("Education", "MonthlyIncome", ax1[0, 0])
subplot_graph("Department", "MonthlyIncome", ax1[0, 1])
subplot_graph("MaritalStatus", "JobLevel", ax1[1, 0])
subplot_graph("OverTime", "PercentSalaryHike", ax1[1, 1])
plt.savefig('visualization_one.png')


# ----------------- Visualization 2 ------------------------
# Average Satisfaction - Environment, Job, Relationship

# numpy array with all satisfaction columns from the dataset - WORKING
satisfaction_df = attrition[['EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction']]
satisfaction_array = satisfaction_df.to_numpy()

# initialize list
average_satisfaction = []
# find average and fill array
for i, row in enumerate(satisfaction_array):
    average_satisfaction.append(np.sum(row) / 3)

# Merge satisfaction_df dataframe with average_satisfaction list

series_sat = pd.Series(average_satisfaction, name="AverageSatisfaction")
attrition_and_satisfaction = attrition[['Attrition', 'YearsAtCompany', 'EnvironmentSatisfaction',
                                        'JobSatisfaction', 'RelationshipSatisfaction']]
vis_two_df = pd.concat([attrition_and_satisfaction, series_sat], axis=1)


def subplot_graph_2d(x_axis, subplot_location):
    sns.countplot(data=vis_two_df, x=x_axis, hue="Attrition",
                palette="colorblind", ax=subplot_location)


fig2, ax2 = plt.subplots(4, 1, figsize=(12, 8))
subplot_graph_2d("EnvironmentSatisfaction", ax2[0])
plt.xlabel("JobSatisfaction")
subplot_graph_2d("JobSatisfaction", ax2[1])
subplot_graph_2d("RelationshipSatisfaction", ax2[2])
subplot_graph_2d("AverageSatisfaction", ax2[3])

plt.sca(ax2[3])
plt.xticks(range(10), ['1', '1.34', '1.67', '2', '2.34', '2.67', '3', '3.34', '3.67', '4'])
plt.tight_layout()
plt.savefig('visualization_two.png')
plt.close(4)

plt.show()
