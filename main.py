import pandas as pd
import json

mess_menu_df = pd.read_excel("messmenu.xlsx", sheet_name="Sheet1")
mess_menu_json = {}

def format_cell_value(cell_value):
    if isinstance(cell_value, str):
        if set(cell_value.strip()) == {"*"}:
            return ""
        cell_value = " ".join(cell_value.split())
    return cell_value

def daily_menu(df):
    for col in range(df.shape[1]):
        daily_menu = {"Breakfast": [], "Lunch": [], "Dinner": []}
        date_str = df.iloc[0, col]
        formatted_date = date_str.strftime("%d-%m-%Y")

        for item in range(2, 30):
            cell_value = df.iloc[item, col]
            cell_value = format_cell_value(cell_value)
            if pd.isna(cell_value) or cell_value == "":
                continue

            if 2 <= item <= 10:
                daily_menu["Breakfast"].append(cell_value)
            elif 13 <= item <= 20:
                daily_menu["Lunch"].append(cell_value)
            elif 23 <= item <= 29:
                daily_menu["Dinner"].append(cell_value)

        mess_menu_json[formatted_date] = daily_menu

    return mess_menu_json

def export_json(json_file):
    with open("mess_menu.json", "w") as json_file:
        json.dump(mess_menu_json, json_file, indent=4)

daily_menu(mess_menu_df)
export_json(mess_menu_json)