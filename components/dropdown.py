from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

from . import ids
from components.loader import DataSchema


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_province: list[str] = data[DataSchema.PROVINCE].to_list()

    @app.callback(
        Output(ids.DROPDOWN, "value"),
        Input(ids.SELECT_ALL_BUTTON, "n_clicks"),
    )
    def select_all_province(_: int) -> list[str]:
        return all_province

    return html.Div(
        children=[
            html.H6("จังหวัด"),
            dcc.Dropdown(
                id=ids.DROPDOWN,
                options=[
                    {"label": province, "value": province} for province in all_province
                ],
                value=all_province,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_BUTTON,
                n_clicks=0,
            ),
        ]
    )
