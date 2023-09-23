from model import CropPricePredictor

# create new model object
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
