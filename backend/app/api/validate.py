import pandas as pd
from core.validator import validate_csv, read_csv_fix_quotes

df_clean = read_csv_fix_quotes('../test/data/test_data_clean.csv')
df_dirty = read_csv_fix_quotes('../test/data/test_data_dirty.csv')

result_clean = validate_csv(df_clean)
print("=== CLEAN DATA ===")
print(result_clean)

result_dirty = validate_csv(df_dirty)
print("\n=== DIRTY DATA ===")
print(result_dirty)
