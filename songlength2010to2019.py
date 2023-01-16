import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("top10s.csv", encoding = 'latin-1')




df2 = df[["year", "dur"]]
# print(df2.head())

# print(df2.mean())



def averagesonglength(date):
    avg = 0
    for i in range(len(df2)):
        if date == df2.loc[i, "year"]:
            avg += df2.loc[i, "dur"]
            if date == 2010:
                avg1 = avg/50
            elif date == 2011:
                avg1 = avg/52
            elif date == 2012:
                avg1 = avg/34
            elif date == 2013:
                avg1 = avg/70
            elif date == 2014:
                avg1 = avg/57
            elif date == 2015:
                avg1 = avg/94
            elif date == 2016:
                avg1 = avg/79
            elif date == 2017:
                avg1 = avg/64
            elif date == 2018:
                avg1 = avg/63   
            elif date == 2019:
                avg1 = avg/30     


    return round(avg1, 2)         



print(f"2010 Average Song Length = {averagesonglength(2010)}")
print(f"2011 Average Song Length = {averagesonglength(2011)}")
print(f"2012 Average Song Length = {averagesonglength(2012)}")
print(f"2013 Average Song Length = {averagesonglength(2013)}")
print(f"2014 Average Song Length = {averagesonglength(2014)}")
print(f"2015 Average Song Length = {averagesonglength(2015)}")
print(f"2016 Average Song Length = {averagesonglength(2016)}")
print(f"2017 Average Song Length = {averagesonglength(2017)}")
print(f"2018 Average Song Length = {averagesonglength(2018)}")
print(f"2019 Average Song Length = {averagesonglength(2019)}")


years = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]
averages = [234.4, 247.23, 231.0, 237.84, 228.09, 225.74, 223.01, 225.64, 220.63, 207.33]

df_years_averages = pd.DataFrame({ 'years' : years, 'averagesonglengths' : averages})


graph = df_years_averages.plot(x = 'years', y = 'averagesonglengths')
tickvalues = range(0, len(years))
plt.xticks(ticks=tickvalues)
plt.show()



from sklearn import metrics

print(df_years_averages.head())
print(df_years_averages.shape)

X = df_years_averages[['years']].values.reshape(-1, 1)
y = df_years_averages[['averagesonglengths']].values.reshape(-1, 1)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, accuracy_score
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)

predictedvalue2021 = regressor.predict([[2021]])
print(predictedvalue2021)

y_pred = regressor.predict(X_test)
df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)


import math
RMSE = math.sqrt(metrics.mean_squared_error(y_test, y_pred ))
print(RMSE)

