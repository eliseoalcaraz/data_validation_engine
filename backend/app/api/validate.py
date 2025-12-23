import pandas as pd
from  core.validator import validate_csv

df = pd.read_csv("../test/data/test_data_dirty.csv")
result = validate_csv(df)
print(result)