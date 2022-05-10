from soyking import input_schema, output_schema
from soyking import update_shipping_cost
from soyking import solve


input_path = "data/inputs"
output_path = "data/outputs"
dat = input_schema.csv.create_pan_dat(input_path)
sln = solve(dat)
output_schema.csv.write_directory(sln, output_path)