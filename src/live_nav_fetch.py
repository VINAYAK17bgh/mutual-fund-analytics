import requests
import pandas as pd

schemes = {
    "HDFC_TOP_100":125497,
    "SBI_BLUECHIP":119551,
    "ICICI_BLUECHIP":120503,
    "NIPPON_LARGE_CAP":118632,
    "AXIS_BLUECHIP":119092,
    "KOTAK_BLUECHIP":120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        f"data/raw/{name}.csv",
        index=False
    )

    print(f"Saved {name}")