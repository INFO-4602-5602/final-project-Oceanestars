# How to run this locally

To use the Json to csv converter, first type in the Shell script below on terminal. This will help you flatten keys under "business" in "listings.json" and generate a new file called "listings_flat.json". Feel free to change "listings.json" to your file name.

```
cat listings.json \
| jq -r '[.businesses[] | [paths(scalars) as $path | { ($path | join(".")): getpath($path) }] | add]' \
> listings_flat.json
```
After flattening the json file, convert "listings_flat.json" into a csv file by typing the script below on terminal.
```
python json_to_csv.py listings_flat.json

```
You should see a file named "_AsianRestaurant.csv" in the same folder 😉

# Resources

This code was written by Alexander Vingardt. Check out his post on Medium: https://medium.com/@sashavingardt/recipe-of-the-day-json-to-csv-6632423514d
