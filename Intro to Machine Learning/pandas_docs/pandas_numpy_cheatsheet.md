# pandas and numpy cheatsheet

- .predict()

To see just a slice, use `print(predictions[:20])`.

To get a table-like view with row numbers, use `pd.Series(predictions)`, which shows the first and last 5 rows by default.

For more rows, set `pd.set_option("display.max_rows", 200)`.

For long lines that wrap awkwardly, add `linewidth=120` to `set_printoptions`.

To show the whole thing as a plain list, use `print(predictions.tolist())`.
