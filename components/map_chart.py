import json
import pandas as pd
import plotly.express as px

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from urllib.request import urlopen

from .loader import DataSchema
from . import ids

with urlopen(
    "https://raw.githubusercontent.com/apisit/thailand.json/master/thailandWithName.json"
) as response:
    thai_map = json.load(response)

df = pd.read_csv("data\province_name.csv")
# print(df)
data_eng_name = []
for i, j in zip(df["schools_province"].to_list(), df["eng_name"].to_list()):
    data_eng_name.append({"label": i, "value": j})
# print(data_eng_name)


def render(app: Dash, data: pd.DataFrame) -> html.Div:

    @app.callback(Output(ids.MAP_CHART, "children"), Input(ids.DROPDOWN, "value"))
    def update_pie_chart(schools_provinces: list[str]) -> html.Div:
        filtered_data = data.query("schools_province in @schools_provinces")
        hover_data = filtered_data[DataSchema.PROVINCE].to_list()
        print(hover_data)
        value_lst = []
        for locate_eng_name in data_eng_name:
            label = locate_eng_name["label"]
            if label in filtered_data["schools_province"].tolist():
                value = locate_eng_name["value"]
                value_lst.append(value)
        print(value_lst)

        if filtered_data.shape[0] == 0:
            return html.Div(id=ids.MAP_CHART)

        def create_pivot_table() -> pd.DataFrame:
            pt = filtered_data.pivot_table(
                values=[DataSchema.MALE, DataSchema.FEMALE],
                index=data_eng_name,
                aggfunc="sum",
                fill_value=0,
            )
            return pt.reset_index()

        pivot_table = create_pivot_table()
        map_fig = px.choropleth_mapbox(
            pivot_table,
            geojson=thai_map,
            featureidkey="properties.name",
            locations=value_lst,
            color=filtered_data[DataSchema.STD],
            color_continuous_scale="Bluyl",
            hover_name=hover_data,
            mapbox_style="carto-positron",
            center={"lat": 13.342077, "lon": 100.5018},
            zoom=4.3,
            opacity=0.7,
            labels={
                "locations": "จังหวัด",
                "color": "จำนวนคนทั้งหมด",
            },
        )

        map_fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        return html.Div(dcc.Graph(figure=map_fig), id=ids.MAP_CHART)

    return html.Div(id=ids.MAP_CHART)
