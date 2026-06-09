import sys
print("arguments", sys.argv)

day = int(sys.argv[1])

print(f"Running pipeline for day {day}")

import pandas as pd
# Here you would have your actual data processing logic. For demonstration, we will just create a simple DataFrame.

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

print(df.head()) 

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")