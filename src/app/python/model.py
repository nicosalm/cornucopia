# scikit learn lasso regression model for predicting price of crops

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"


class CropPricePredictor:

    def __init__(self):
        # sets self.model to the trained model
        model, df = self.get_model()
        self.model = model
        self.df = df

    def predict(self, date: str, crop):

        if crop not in [1, 2, 3, 4]:
            raise ValueError("Crop must be in range [1, 4] and be an integer")

        print("\n\n\n\nLoading complete...\n")
        # date: YYYY-MM-DD
        # crop: 1 = corn, 2 = oats, 3 = soybeans, 4 = wheat

        # make a df with the input data and then feed it into preprocess()
        udf = pd.DataFrame({'date': [date], 'crop': [crop]})
        udf_formatted = self.format_user_input(date, crop)

        # predict the price
        price = self.model.predict(udf_formatted)

        with open(dir_path + 'out/predicted_price.txt', 'w') as f:
            # write the metrics to the file
            f.write('Predicted_Price:' + str(price) + '\n')
        f.close()

        return price

    def format_user_input(self, date: str, crop: int):
        # this is a helper function for the predict() function, it will be similar to
        # but different from the preprocess() function

        # if crop isn't formatted YYYY-MM-DD, then format it or raise an error
        # if crop isn't 1, 2, 3, or 4, then raise an error
        if crop not in [1, 2, 3, 4]:
            raise ValueError("Crop must be in range [1, 4]")

        if len(date) != 10:
            raise ValueError("Date must be in the format YYYY-MM-DD")

        # we can do these automatically
        udf = pd.DataFrame({'date': [date], 'crop': [crop]})
        udf['date'] = pd.to_datetime(udf['date'])
        udf['year'] = udf['date'].dt.year
        udf['month'] = udf['date'].dt.month
        udf['day'] = udf['date'].dt.day
        udf['day_of_week'] = udf['date'].dt.dayofweek
        udf['day_of_year'] = udf['date'].dt.dayofyear
        udf['is_spring'] = udf['month'].isin([3, 4, 5])
        udf['is_summer'] = udf['month'].isin([6, 7, 8])
        udf['is_fall'] = udf['month'].isin([9, 10, 11])
        udf['is_winter'] = udf['month'].isin([12, 1, 2])
        udf = udf.drop(columns=['date'])

        # for the remaining features, we will select lag, moving average, and exponential moving average values
        # based on historical training data and the date provided by the user

        # find the closest date in the training data to the date provided by the user

        # closest = self.df.iloc[(self.df['date']-date).abs().argsort()[:1]]

        year, month, day = udf['year'][0], udf['month'][0], udf['day'][0]
        crop = udf['crop'][0]

        closest = self.df[(self.df['year'] == year) & (
            self.df['month'] == month) & (self.df['crop'] == crop)]

        closest = closest.iloc[(closest['day']-day).abs().argsort()[:1]]

        # take these values and add them to the dataframe
        udf['price_lag_1'] = closest['price_lag_1'].values[0].astype(float)
        udf['price_lag_3'] = closest['price_lag_3'].values[0].astype(float)
        udf['price_lag_6'] = closest['price_lag_6'].values[0].astype(float)
        udf['price_lag_12'] = closest['price_lag_12'].values[0].astype(float)
        udf['price_ma_1'] = closest['price_ma_1'].values[0].astype(float)
        udf['price_ma_3'] = closest['price_ma_3'].values[0].astype(float)
        udf['price_ma_6'] = closest['price_ma_6'].values[0].astype(float)
        udf['price_ma_12'] = closest['price_ma_12'].values[0].astype(float)
        udf['price_ema_1'] = closest['price_ema_1'].values[0].astype(float)
        udf['price_ema_3'] = closest['price_ema_3'].values[0].astype(float)
        udf['price_ema_6'] = closest['price_ema_6'].values[0].astype(float)
        udf['price_ema_12'] = closest['price_ema_12'].values[0].astype(float)

        return udf

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

        # save the metrics to a file in the out folder
        with open(dir_path + 'out/metrics.txt', 'w') as f:
            # write the metrics to the file
            f.write('Training_RMSE:' + str(train_rmse) + '\n')
            f.write('Training_MAE:' + str(train_mae) + '\n')
            f.write('Training_R2:' + str(train_r2) + '\n')
            f.write('Test_RMSE:' + str(test_rmse) + '\n')
            f.write('Test_MAE:' + str(test_mae) + '\n')
            f.write('Test_R2:' + str(test_r2) + '\n')
        f.close()

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
        plt.savefig(dir_path + 'out/actual_vs_predicted.png')

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
        plt.savefig(dir_path + 'out/predicted_vs_residuals.png')

    # main function

    def get_model(self):

        df = self.merge_csv(dir_path + 'data/corn-price-data.csv', dir_path + 'data/oats-price-data.csv',
                            dir_path + 'data/soybeans-price-data.csv', dir_path + 'data/wheat-price-data.csv')

        X_scaled, y = self.preprocess(df)

        lasso, X_train, X_test, y_train, y_test = self.train_model(X_scaled, y)

        self.test_model(lasso, X_train, X_test, y_train, y_test)

        # now, we can use the model to make predictions
        # let's do that in another function but for now we will just return the model
        return lasso, df


def test():
    c = CropPricePredictor()

    date = '1980-01-01'
    crop = 1  # 1 = corn, 2 = oats, 3 = soybeans, 4 = wheat

    # run the predict() function
    out = c.predict(date, crop)

    # strip the [], and round to two decimal places, add USD to the end
    out = str(out).strip('[]')
    out = round(float(out), 2)
    out = str(out) + " USD"

    # this is the output:
    print("Price:" + out)


test()
