from dash import Dash, html
import pandas as pd

from . import bar_chart, dropdown


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    dropdown.render(app, data),
                ],
            ),
            bar_chart.render(app, data),
        ],
    )
