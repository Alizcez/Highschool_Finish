import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output


from components.loader import DataSchema
from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [
            Input(ids.DROPDOWN, "value"),
        ],
    )
    def update_bar_chart(schools_provinces: list[str]) -> html.Div:
        filtered_data = data.query("schools_province in @schools_provinces")
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.BAR_CHART)

        def create_pivot_table() -> pd.DataFrame:
            pt = filtered_data.pivot_table(
                values=[DataSchema.MALE, DataSchema.FEMALE],
                index=[DataSchema.PROVINCE],
                aggfunc="sum",
                fill_value=0,
            )
            return pt.reset_index()

        pivot_table = create_pivot_table()
        fig = px.bar(
            pivot_table,
            x=DataSchema.PROVINCE,
            y=[DataSchema.MALE, DataSchema.FEMALE],
            title="จำนวนนักเรียนจบชั้นมัธยมศึกษาปีที่ 6 ปีการศึกษา 2566",
            labels={
                DataSchema.PROVINCE: "Province",
                "value": "Number of People",
                "variable": "Gender",
            },
            color="variable",
            barmode="group",
        )

        fig.update_layout(
            xaxis_title="จังหวัด",
            yaxis_title="จำนวนตนในแต่ละจังหวัด",
            legend_title="เพศ",
            yaxis=dict(tickformat=","),
        )

        fig.update_traces(texttemplate="%{y}", textposition="outside")

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)
