# this is a chart to display historical data, and predicted data for a crop, built with matplotlib and seaborn

import os
import pickle
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import model
import asyncio

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"


def get_mongo_db():
    uri = "mongodb+srv://nico:badabing@cornhub.pclzcbt.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client.cornhub
    except Exception as e:
        print(e)
        return None


def get_all_results(db):
    df_groups = pd.DataFrame(list(db.groups.find()))
    # df_users = pd.DataFrame(list(db.user.find()))
    all_results = []

    for _, row in df_groups.iterrows():
        crops_data = row['crops']
        result = []
        for crop, data in crops_data.items():
            if isinstance(data['total'], dict) and '$numberInt' in data['total']:
                quantity = int(data['total']['$numberInt'])
            else:
                quantity = int(data['total'])
            result.append({crop: quantity})

        all_results.append(result)

    return all_results


def piechart(crops):
    # Create a list of crops and quantities
    crops_list = []
    quantities_list = []
    for crop in crops:
        for key, value in crop.items():
            crops_list.append(key)
            quantities_list.append(value)

    # Create a dataframe from the lists
    df = pd.DataFrame({'crop': crops_list, 'quantity': quantities_list})


def set_pie_chart_styles():
    # let's make it look pretty with the following customizations
    plt.rcParams['font.size'] = 20.0
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.titlesize'] = 20.0
    plt.rcParams['axes.labelsize'] = 20.0
    plt.rcParams['axes.titlepad'] = 20.0
    plt.rcParams['axes.labelpad'] = 20.0
    plt.rcParams['legend.fontsize'] = 20.0
    plt.rcParams['legend.title_fontsize'] = 20.0
    plt.rcParams['legend.title_fontsize'] = 20.0
    plt.rcParams['legend.handlelength'] = 1.0
    plt.rcParams['legend.handleheight'] = 1.0
    plt.rcParams['legend.labelspacing'] = 1.0
    plt.rcParams['legend.borderpad'] = 1.0
    plt.rcParams['legend.edgecolor'] = 'black'
    plt.rcParams['legend.fancybox'] = True
    plt.rcParams['legend.framealpha'] = 0.5
    plt.rcParams['legend.frameon'] = True
    plt.rcParams['legend.markerscale'] = 1.0
    plt.rcParams['legend.numpoints'] = 1.0
    plt.rcParams['legend.scatterpoints'] = 1.0
    plt.rcParams['text.color'] = 'white'


def piechart(crops):
    crops_list = []
    quantities_list = []
    for crop in crops:
        for key, value in crop.items():
            crops_list.append(key)
            quantities_list.append(value)

    df = pd.DataFrame({'crop': crops_list, 'quantity': quantities_list})

    set_pie_chart_styles()

    plt.pie(df['quantity'], labels=df['crop'],
            autopct='%1.1f%%', startangle=90)
    centre_circle = plt.Circle((0, 0), 0.70, fc='#183430')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.axis('equal')
    plt.savefig(dir_path + 'out/piechart.png',
                bbox_inches='tight', dpi=300, transparent=True)


def set_line_chart_styles():
    # let's make it look pretty with the following customizations
    plt.rcParams['font.size'] = 20.0
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.titlesize'] = 20.0
    plt.rcParams['axes.labelsize'] = 20.0
    plt.rcParams['axes.titlepad'] = 20.0
    plt.rcParams['axes.labelpad'] = 20.0
    plt.rcParams['legend.fontsize'] = 20.0
    plt.rcParams['legend.title_fontsize'] = 20.0
    plt.rcParams['legend.title_fontsize'] = 20.0
    plt.rcParams['legend.handlelength'] = 1.0
    plt.rcParams['legend.handleheight'] = 1.0
    plt.rcParams['legend.labelspacing'] = 1.0
    plt.rcParams['legend.borderpad'] = 1.0
    plt.rcParams['legend.edgecolor'] = 'black'
    plt.rcParams['legend.fancybox'] = True
    plt.rcParams['legend.framealpha'] = 0.5
    plt.rcParams['legend.frameon'] = True
    plt.rcParams['legend.markerscale'] = 1.0
    plt.rcParams['legend.numpoints'] = 1.0
    plt.rcParams['legend.scatterpoints'] = 1.0
    plt.rcParams['text.color'] = 'white'


def predicted_prices(model: model.CropPriceLassoRegressor, group_index: int):

    # let's get the dataframe for the group we want to predict prices for
    db = get_mongo_db()

    crops_list = []
    if db is not None:
        # grab the names of the crops from get_all_results
        all_results = get_all_results(db)
        crops = all_results[group_index]
        for crop in crops:
            for key, value in crop.items():
                crops_list.append(key)

    # from the current date, we want to plot the next 30 days in intervals of 3 days
    # so we create a list of dates

    # get the current date - 1 month
    current_date = datetime.datetime.now() - datetime.timedelta(days=30)
    # create a list of dates
    dates = [current_date + datetime.timedelta(days=x)
             for x in range(0, 30, 3)]
    # convert the dates to strings
    dates = [date.strftime("%Y-%m-%d") for date in dates]

    # let's get the predicted prices for each crop
    # we'll store the results in a dictionary

    crop_to_int = {  # mapping dictionary
        'corn': 1,
        'oats': 2,
        'soybeans': 3,
        'wheat': 4
    }

    # create a dictionary to store the results
    results = {}

    # for each crop, we want to predict the price for each date
    for crop in crops_list:
        # create a list to store the predicted prices
        predicted_prices = []
        # for each date, we want to predict the price
        for date in dates:
            # get the predicted price
            predicted_price = model.predict(
                date, crop_to_int[crop])
            # append the predicted price to the list
            predicted_prices.append(predicted_price)
        # add the list of predicted prices to the dictionary
        results[crop] = predicted_prices

    # let's use results to plot a line chart
    # first, we need to create a dataframe from the dictionary
    df = pd.DataFrame(results, index=dates)

    # Convert lists to values
    df = df.applymap(lambda x: x[0])

    # Set Seaborn style
    sns.set_style("whitegrid")
    sns.set_palette("pastel")

    # Set the figure size
    plt.figure(figsize=(10, 5))

    # Melt the dataframe for long-format plotting
    df_melted = df.reset_index().melt(id_vars='index', value_vars=[
        'corn', 'oats'], var_name='crop', value_name='price')

    # Use a lineplot to plot the data with two lines
    sns.lineplot(data=df_melted, x='index', y='price', hue='crop')

    set_line_chart_styles()

    # Set the x-axis to display dates
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=3))

    # Set color of the axis labels to white
    plt.gca().tick_params(axis='x', colors='white')
    plt.gca().tick_params(axis='y', colors='white')

    # make the smooth lines thicker and more visible
    plt.gca().lines[0].set_linewidth(4)
    plt.gca().lines[1].set_linewidth(4)

    # make x and y labels light gray
    plt.gca().set_xlabel('Date', color='#d3d3d3')
    plt.gca().set_ylabel('Price ($)', color='#d3d3d3')

    # make title white
    plt.gca().set_title('Predicted Crop Prices', color='white')

    # Set the x-axis labels to be rotated 45 degrees
    plt.xticks(rotation=45)

    # Set the y-axis label
    plt.ylabel('Price ($)')

    # Set the title
    plt.title('Predicted Crop Prices')

    # Save the figure
    plt.savefig(dir_path + 'out/linechart.png',
                bbox_inches='tight', dpi=300, transparent=True)


async def generate_charts(model: model.CropPriceLassoRegressor, group_index: int):
    db = get_mongo_db()
    if db is not None:
        all_results = get_all_results(db)
        piechart(all_results[group_index])
        predicted_prices(model, group_index)
