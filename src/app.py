import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md("# marimo + Poetry!")
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""This is a markdown""")
    return


@app.cell
def test_cell():


    from utils import add

    assert add(1, 2) == 3
    assert 2 == 2
    return


@app.cell
def _(mo):
    mo.md("# This is a print")

    print("test")
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
