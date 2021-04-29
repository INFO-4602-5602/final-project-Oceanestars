#code written by Alexander Vingardt. Link: https://medium.com/@sashavingardt/recipe-of-the-day-json-to-csv-6632423514d

import pandas as pd

with open('listings_flat.json') as f_input:
    df = pd.read_json(f_input)
    df.to_csv('_AsianRestaurant.csv', index=False)
