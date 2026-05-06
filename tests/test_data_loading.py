import pathlib
import pandas as pd


def test_primary_csv_files_exist():
    base = pathlib.Path(__file__).resolve().parent.parent
    assert (base / "archive (2)" / "output.csv").exists(), "House price dataset is missing"
    assert (base / "clustering_customers.csv").exists(), "Customer segmentation dataset is missing"


def test_can_read_primary_csv_files():
    base = pathlib.Path(__file__).resolve().parent.parent
    df_house = pd.read_csv(base / "archive (2)" / "output.csv")
    df_customers = pd.read_csv(base / "clustering_customers.csv")
    assert not df_house.empty
    assert not df_customers.empty
