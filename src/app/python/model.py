# scikit learn lasso regression model for predicting price of crops

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


class CropPricePredictor:

    def __init__(self):
        self.model = self.get_model()  # returns a trained model

    def predict(self, date, crop):

        print("\n\n\n\nLoading complete...\n")
        # date: YYYY-MM-DD
        # crop: 1 = corn, 2 = oats, 3 = soybeans, 4 = wheat

        # run the preprocess() function on the input data
        # preprocess() returns a dataframe with the input data in the correct format

        # make a df with the input data and then feed it into preprocess()
        df = pd.DataFrame({'date': [date], 'crop': [crop]})
        df_preprocessed = self.preprocess(df)
        print(df_preprocessed)

    # parameters: up to four csv files containing the data for each crop

    def merge_csv(self, csv_file1, csv_file2, csv_file3=None, csv_file4=None):
        # we are combining the data from the four csv files into one dataframe,
        # for each crop csv we will add a column for the crop identifier number:
        # 1 = corn, 2 = oats, 3 = soybeans, 4 = wheat

        # read in the csv files
        df1 = pd.read_csv(csv_file1)
        df2 = pd.read_csv(csv_file2)
        df3 = pd.read_csv(csv_file3)
        df4 = pd.read_csv(csv_file4)

        # add the crop identifier column to each dataframe
        df1['crop'] = 1
        df2['crop'] = 2
        if csv_file3 != None:
            df3['crop'] = 3
        if csv_file4 != None:
            df4['crop'] = 4

        # combine the dataframes into one
        df = pd.concat([df1, df2, df3, df4])

        # drop entries with missing values
        df = df.dropna()

        return df

    def preprocess(self, df):

        # transform the date column (YYYY-MM-DD) into three columns (year, month, day)
        # convert the date column to datetime format
        df['date'] = pd.to_datetime(df['date'])

        # add the year, month, and day columns
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day'] = df['date'].dt.day

        # engineer additional features

        # time-based features
        df['day_of_week'] = df['date'].dt.dayofweek
        df['day_of_year'] = df['date'].dt.dayofyear

        # seasonal features
        df['is_spring'] = df['month'].isin([3, 4, 5])
        df['is_summer'] = df['month'].isin([6, 7, 8])
        df['is_fall'] = df['month'].isin([9, 10, 11])
        df['is_winter'] = df['month'].isin([12, 1, 2])

        # lag features (1 month, 3 months, 6 months, 1 year)
        # we can use the shift() function to do this

        # lag by 1, 3, 6, 12 months
        df['price_lag_1'] = df['price'].shift(30)  # 30 days in a month
        df['price_lag_3'] = df['price'].shift(90)  # 90 days in 3 months
        df['price_lag_6'] = df['price'].shift(180)  # 180 days in 6 months
        df['price_lag_12'] = df['price'].shift(365)  # 365 days in a year

        # moving average features (1 month, 3 months, 6 months, 1 year)
        # we can use the rolling() function to do this

        df['price_ma_1'] = df['price'].rolling(30).mean()
        df['price_ma_3'] = df['price'].rolling(90).mean()
        df['price_ma_6'] = df['price'].rolling(180).mean()
        df['price_ma_12'] = df['price'].rolling(365).mean()

        # exponential moving average features (1 month, 3 months, 6 months, 1 year)
        # we can use the ewm() function to do this

        df['price_ema_1'] = df['price'].ewm(span=30, adjust=False).mean()
        df['price_ema_3'] = df['price'].ewm(span=90, adjust=False).mean()
        df['price_ema_6'] = df['price'].ewm(span=180, adjust=False).mean()
        df['price_ema_12'] = df['price'].ewm(span=365, adjust=False).mean()

        # drop the date column
        df = df.drop(columns=['date'])

        # drop the rows with missing values
        df = df.dropna()

        # return the dataframe
        # columns: [ price, crop, year, month, day, day_of_week, day_of_year is_spring, is_summer,
        # is_fall, is_winter, price_lag_1, price_lag_3, price_lag_6, price_lag_12, price_ma_1,
        # price_ma_3, price_ma_6, price_ma_12, price_ema_1, price_ema_3, price_ema_6, price_ema_12 ]

        # Scaling
        from sklearn.preprocessing import StandardScaler

        # seperate features and get target variable
        X = df.drop(columns=['price'])
        y = df['price']

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # One-hot encoding for all categorical variables
        X = pd.get_dummies(X, columns=['crop', 'year', 'month', 'day', 'day_of_week',
                                       'day_of_year', 'is_spring', 'is_summer', 'is_fall', 'is_winter'], drop_first=True)

        return X_scaled, y

    def train_model(self, X_scaled, y):

        # Train

        from sklearn.linear_model import Lasso
        from sklearn.model_selection import train_test_split

        # seperate features and get target variable
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42)  # 80% training and 20% test

        # TODO: pick the best alpha value for the Lasso regression model
        # train the Lasso regression model
        # alpha is the regularization parameter
        lasso = linear_model.Lasso(alpha=0.1)
        lasso.fit(X_train, y_train)  # fit the model using the training data

        # now we can use the model to make predictions
        # let's do that in another function but for now we will just return the model

        return lasso, X_train, X_test, y_train, y_test

    # parameters: dataframe containing the data for all crops

    def test_model(self, lasso, X_train, X_test, y_train, y_test):

        # Evaluate using RMSE, MAE, and R2

        from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

        # predict on training and test sets
        y_train_pred = lasso.predict(X_train)
        y_test_pred = lasso.predict(X_test)

        # Compute metrics for the training set
        train_rmse = mean_squared_error(y_train, y_train_pred, squared=False)
        train_mae = mean_absolute_error(y_train, y_train_pred)
        train_r2 = r2_score(y_train, y_train_pred)

        # Compute metrics for the test set
        test_rmse = mean_squared_error(y_test, y_test_pred, squared=False)
        test_mae = mean_absolute_error(y_test, y_test_pred)
        test_r2 = r2_score(y_test, y_test_pred)

        # print the error metrics
        print("Training RMSE:", train_rmse)
        print("Test RMSE:", test_rmse)

        print("\nTraining MAE:", train_mae)
        print("Test MAE:", test_mae)

        print("\nTraining R²:", train_r2)
        print("Test R²:", test_r2)

        # let's also print the coefficients and intercept
        print("\nCoefficients:", lasso.coef_)
        print("Intercept:", lasso.intercept_)

        # Data visualization
        # plot the predicted vs actual values for the test set and make the plot look nice
        plt.figure(figsize=(10, 10))
        plt.scatter(y_test, y_test_pred, s=20)
        plt.xlabel('Actual Price')
        plt.ylabel('Predicted Price')
        plt.title('Actual vs Predicted Price')
        # smooth line
        z = np.polyfit(y_test, y_test_pred, 1)
        p = np.poly1d(z)
        plt.plot(y_test, p(y_test), color='red')
        # save the plot to a file in the plots folder
        plt.savefig('plots/actual_vs_predicted.png')

        # plot the residuals
        plt.figure(figsize=(10, 10))
        plt.scatter(y_test_pred, y_test_pred - y_test, s=20)
        plt.xlabel('Predicted Price')
        plt.ylabel('Residuals')
        plt.title('Predicted vs Residuals')
        # residual lines
        plt.hlines(y=0, xmin=y_test_pred.min(),
                   xmax=y_test_pred.max(), color='red')
        # save the plot to a file in the plots folder
        plt.savefig('plots/residuals.png')

    # main function

    def get_model(self):

        df = self.merge_csv('data/corn-price-data.csv', 'data/oats-price-data.csv',
                            'data/soybeans-price-data.csv', 'data/wheat-price-data.csv')

        X_scaled, y = self.preprocess(df)

        lasso, X_train, X_test, y_train, y_test = self.train_model(X_scaled, y)

        self.test_model(lasso, X_train, X_test, y_train, y_test)

        # now, we can use the model to make predictions
        # let's do that in another function but for now we will just return the model
        return lasso


# now that we have a model, we can use it to make predictions
# we will make a function in which the user provides a YYYY-MM-DD date and a crop identifier number, and the function will return the predicted price of that crop on that date
