# Moving average assignment

This repository contains a marimo notebook that computes the moving average of the instruments in the `input_data.json`-file.

The project is set up with `uv`, and it is recommended to use that for running the notebook. Python version 3.13 and above is required.

The user can interact with the code in a few ways. To see the notebook run (from the root of this repository):

```
uv run marimo run main.py
```

In the notebook you can see the prices and moving averages of the instruments in `input_data.json` as a time series graph and a table. The table data can be exported to a range of formats ("json", "csv", "parquet", ...) upon request.

If you want to be able to edit the notebook and dive deeper into it run `uv run marimo edit main.py`. The notebook can also be run as a script:

```
uv run main.py
```

When run as a script in the terminal, an overview of the polars dataframe containing the moving average is printed to the console as output.

If `uv` is not available you can also install the dependencies as specified in the `pyproject.toml` file using the command `pip install .`.

The project dependencies are `marimo`, for the notebook, `polars`, for the moving averages calcualtion, and `plotly`, for interactive plots in the notebook. Their versions are specified in the `pyproject.toml` file.

PS: One date value in the `input_data.json` was observed to be invalid ("2024-02-31"). This date has been removed from the data, as it is assumed to have been an error.

PPS: Total time used: 67 minutes.
