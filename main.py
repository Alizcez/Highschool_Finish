from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from components.layout import create_layout
from components.loader import (
    load_transaction_data,
)

DATA_PATH = "https://gpa.obec.go.th/reportdata/pp3-4_2566_province.json"


def main() -> None:
    data = load_transaction_data(DATA_PATH)
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Rongrean dashboard"
    app.layout = create_layout(app, data)
    app.run(debug=True)


if __name__ == "__main__":
    main()
