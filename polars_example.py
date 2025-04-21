import polars as pl
import datetime as dt

df_csv = pl.read_csv("modified/trending_GB_1d_20250419-0948.csv", try_parse_dates=True)
print(df_csv)
df2 = pl.read_csv("modified/trending_GB_1d_20250419-0847.csv", try_parse_dates=True)
df_combined = pl.concat([df_csv, df2])
df2 = df2.with_columns( pl.lit("20250419-0847").alias("Dataset") )
df_csv = df_csv.with_columns( pl.lit("20250419-0948").alias("Dataset") )
df_combined = pl.concat([df_csv, df2])
print(df_combined)

result = df_combined.select(pl.all()).group_by(pl.col("Trends"),maintain_order=True)
print(result.agg(pl.col("Search volume"), pl.col("Started"), pl.col("Ended"), pl.col("Trend breakdown"), pl.col("Dataset")))
