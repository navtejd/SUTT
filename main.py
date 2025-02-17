import pandas as pd
import json

mess_menu_df = pd.read_excel("messmenu.xlsx", sheet_name="Sheet1")
mess_menu_json = {}

def format_cell_value(cell_value): #formats the stuff we have , in the sense it removes cells with stars and nulls
    if isinstance(cell_value, str): #isinstance means it checks if cellvalue is string
        if set(cell_value.strip()) == {"*"}: #checks if cell contains only * values
            return "" #empty string essentially skips it
        cell_value = " ".join(cell_value.split()) #removes spaces
    return cell_value

def daily_menu(df):
    for col in range(df.shape[1]): #basically forloop going thru all the columns
        daily_menu = {"Breakfast": [], "Lunch": [], "Dinner": []} #dictionary for the todays menu, with seperate lists
                                                                  #for eachcourse
        date_str = df.iloc[0, col] #extracts date from first row of the column
        formatted_date = date_str.strftime("%d-%m-%Y")  #formats the date

        for item in range(2, 30): #for loop to iterate thru daily items
            cell_value = df.iloc[item, col]
            cell_value = format_cell_value(cell_value)
            if pd.isna(cell_value) or cell_value == "": #skips cells where there is a blankspace or null or stars
                continue
          #BELOW are lists for Each courses, items getting added as the loop iterates
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

daily_menu(mess_menu_df) #creating parsed menu
export_json(mess_menu_json) #json file generation