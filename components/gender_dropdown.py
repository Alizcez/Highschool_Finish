from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

from . import ids
from loader import DataSchema


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_gender: list[str] = data[DataSchema.MALE].to_list()
    sex = ["ชาย", "หญิง"]

    @app.callback(
        Output(ids.GENDER_DROPDOWN, "value"),
        [Input(ids.DROPDOWN, "value"), Input(ids.SELECT_ALL_BUTTON, "n_clicks")],
    )
    def update_gender(genders: list[str], _: int) -> list[str]:
        filtered_data = data.query("gender in @genders")
        return filtered_data

    return html.Div(
        children=[
            html.H6("เพศ"),
            dcc.Dropdown(
                id=ids.GENDER_DROPDOWN,
                options=["ชาย", "หญิง"],
                value=all_gender,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_GENDER_BUTTON,
                n_clicks=0,
            ),
        ]
    )
