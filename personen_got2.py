personen = [
    {"Name": "Arya", "Haus": "Stark", "Waffe": "Schwert"},
    {"Name": "Cersei", "Haus": "Lannister", "Waffe": None},
    {"Name": "Daenerys", "Haus": "Targaryen", "Waffe": "Drachen"},
    {"Name": "Jaime", "Haus": "Lannister", "Waffe": "Schwert"},
]

for p in personen:
    if p["Waffe"] == "Schwert":
        print(p["Name"], p["Haus"])