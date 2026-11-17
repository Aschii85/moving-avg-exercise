import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")

with app.setup:
    import json

    import marimo as mo
    import plotly.express as px
    import polars as pl


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Moving Average Notebook

    This notebook calculates the the (trailing) moving average of the supplied data set.
    """)
    return


@app.cell
def _():
    window_size = mo.ui.number(
        start=1,
        stop=100,
        value=10,
        label="Window size for moving average:",
    )
    window_size
    return (window_size,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    PS the data contains a date value that is not real ("2024-02-31"). The data for this date is removed...
    """)
    return


@app.cell
def _(window_size):
    with open("input_data.json", "r") as _f:
        _raw_data = json.load(_f)

    data = {}
    for _key, _records in _raw_data.items():
        if _key.startswith("Inst"):
            data[_key] = (
                pl.DataFrame(_records)
                .with_columns(pl.col("date").str.to_date(strict=False))
                .drop_nulls()
                .sort("date")
                .with_columns(
                    pl.col("price")
                    .rolling_mean(window_size=window_size.value)
                    .alias("moving_average")
                )
            )
    return (data,)


@app.cell
def _(data):
    _key = "Inst1"
    print(f"{_key}:", data[_key])
    _fig = px.line(data[_key], x="date", y=["price", "moving_average"], title=_key)
    mo.output.append(_fig)
    mo.output.append(data[_key])
    return


@app.cell
def _(data):
    _key = "Inst2"
    print(f"{_key}:", data[_key])
    _fig = px.line(data[_key], x="date", y=["price", "moving_average"], title=_key)
    mo.output.append(_fig)
    mo.output.append(data[_key])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
