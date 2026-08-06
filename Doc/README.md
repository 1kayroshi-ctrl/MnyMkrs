Created by: Moin Siddiqui
Start date: 01/08/2026
last worked on: 05/08/2026


Purpose: 
The purpose of this program is try to develop a competitve edge or a unique insight into correlated stocks.
Becouse of current world trends I picked the GICS defined sub-sector Materials.

Program pipeline
- The program first usees Yahoo's  *yfiniance* library to get the historical data of the stocks in the Materials sub-sector.
- then we use the pandas lib to clean and prepare the data for our database
- we'll use this data to train a machine learning model to predict the future price of the stocks in the Materials sub-sector.


Machine learning model
- The model will be trained on the historical daily data of the stocks in the Materials sub-sector from 2014-2023.
- Data was exported to Azure blob storage and then imported into Azure ML Studio to train the model.
- One possible mistake I made was haveing StackEnsemble as the final model. I should have used a single model to avoid overfitting.


Time series forecasting: 
I decided to use  a time series forcasting becouse we are tyring to perdict values based on time. 
In this case we are trying to perdict the daily opening price of stock prices in the Materials sub-sector. As such the 
frequency of the data is daily at opening price. So will be using a time series forecasting model to predict the future opening 
price of the stocks in the Materials sub-sector.

Forcasting horizon: 7

Primary Regression Metric: Noramilized Root Mean Squared Error.
The reason for using RMSE is becouse we want to punish large errors that my occur. 
By using RMSE we should be close to the actual value of the stock price when something unforseen may happen in the market, as stable
perdictions are more important than a model that is only accurate on average.

I did not use R^2 becouse it doens't penalize large errors as much as RMSE does. For overall patterns it's a good metric 
but we want to be close to the actual value of the stock price even if something unforseen happens in the market.

I didn't use Normalized Mean Absolute Error becouse of it's tendency to occasinalty make large errors. This is a close contender for
our use case but becaouse it's not as good as RMSE at punishing large errors, I decided to go with RMSE.

- Leveraging Sesonal(US) trends
- Forcast Horizion: 7 days
- k-fold cross validation: 5 folds
- cross validation step size: 120 days
- instnaces: 1

Results:
At the end of computing the model, the program ran 81 diffrent child processes, each running a diffrent model.
Each model was automaticly queued after each other and the parent process ran for a total compute duration of 6h 19m 35.24s.

<img width="1574" height="657" alt="image" src="https://github.com/user-attachments/assets/7a8e570b-f4f0-4c7a-906b-8fd670c86bc0" />

