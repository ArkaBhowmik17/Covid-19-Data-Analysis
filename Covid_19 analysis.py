import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
corona_dataset_csv=pd.read_csv("Covid19_Confirmed_dataset.csv")#Reads the Excel file
corona_dataset_csv.head(10)
corona_dataset_csv.shape#Checks the shape of excel file
df=corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)#Removes the useless datas
#print(df.head(10))
corona_dataset_aggregated=corona_dataset_csv.groupby("Country/Region").sum()
corona_dataset_aggregated.head(10)
print(corona_dataset_aggregated.head(10))
corona_dataset_aggregated.shape
corona_dataset_aggregated.loc["China"]
'''
print(corona_dataset_aggregated.loc["China"])
print(corona_dataset_aggregated.loc["China"].plot())
print(corona_dataset_aggregated.loc["Italy"].plot())
print(corona_dataset_aggregated.loc["Australia"].plot())
print(corona_dataset_aggregated.loc["India"].plot())
print(corona_dataset_aggregated.loc["Armenia"].plot())
plt.legend()
print(corona_dataset_aggregated.loc["China"][:3].plot())#prints the graph of first 3 days of corona virus cases in China
'''
print(corona_dataset_aggregated.loc["China"].diff().plot())
print("Maximum cases in China in a day:",corona_dataset_aggregated.loc["China"].diff().max())
print("Maximum cases in Italy in a day:",corona_dataset_aggregated.loc["Italy"].diff().max())
print("Maximum cases in Spain in a day:",corona_dataset_aggregated.loc["Spain"].diff().max())
countries=list(corona_dataset_aggregated.index)
max_infection_rates=[]
for c in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
    print(max_infection_rates)
corona_dataset_aggregated["max_infection_rate"]=max_infection_rates
print(corona_dataset_aggregated.head(10))
corona_data=pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])
print(corona_data)
happiness_report_csv=pd.read_csv("worldwide_happiness_report.csv")
print(happiness_report_csv.head(10))#Unclean data
useless_cols=["Overall rank","Score","Generosity","Perceptions of corruption"]
happiness_report_csv.drop(useless_cols,axis=1,inplace=True)
print(happiness_report_csv.head(10))#Clean data
happiness_report_csv.set_index("Country or region",inplace=True)
print(happiness_report_csv.head(10))
corona_data.head(10)
corona_data.shape
happiness_report_csv.shape
data=corona_data.join(happiness_report_csv,how="inner")
data.head()
print(data.head())
data.corr()
print(data.corr())
data.head()
x=data["GDP per capita"]
y=data["max_infection_rate"]
sns.scatterplot(x,y)
print(sns.scatterplot(x,np.log(y)))
print(sns.regplot(x,np.log(y)))