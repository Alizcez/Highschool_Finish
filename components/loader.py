import pandas as pd


class DataSchema:
    YEAR = "pp3year"
    LEVEL = "level"
    PROVINCE = "schools_province"
    MALE = "totalmale"
    FEMALE = "totalfemale"
    STD = "totalstd"


def load_transaction_data(path: str) -> pd.DataFrame:
    data = pd.read_json(
        path,
        dtype={
            DataSchema.YEAR: int,
            DataSchema.LEVEL: str,
            DataSchema.PROVINCE: str,
            DataSchema.MALE: int,
            DataSchema.FEMALE: int,
            DataSchema.STD: int,
        },
    )
    return data
