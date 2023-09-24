from pickle import load
import numpy as np
import pandas as pd
import os
import model
import chart
import asyncio
import pickle
import datetime

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"

'''
The overall flow of the application is as follows:

1. Spin up the model (if a pickled model exists, load it, otherwise train a new model)
2. Generate both the pie chart and the line chart (chart.py)

Because these things take time, we want to do them asynchronously. This is where asyncio comes in.
'''


async def main():
    # Load the pickled model if it exists
    regressor = await model.CropPriceLassoRegressor.create()

    # Now we have a model, we can generate the charts
    await chart.generate_charts(regressor, 1)


asyncio.run(main())

# we want to send a json update to the frontend when the graphs are generated
# this is a bit of a hack, but it works for now

with open(dir_path + 'pychart.json', 'rb') as f:
    chart_json = pickle.load(f)
