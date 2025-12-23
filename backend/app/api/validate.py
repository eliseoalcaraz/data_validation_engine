import pandas as pd
from core.validator import validate_csv

df_clean = pd.read_csv("../../test/data/test_data_clean.csv")
df_dirty = pd.read_csv("../../test/data/test_data_dirty.csv")

result_clean = validate_csv(df_clean)
print("=== CLEAN DATA ===")
print(result_clean)

result_dirty = validate_csv(df_dirty)
print("\n=== DIRTY DATA ===")
print(result_dirty)
