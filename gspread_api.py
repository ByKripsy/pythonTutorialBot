import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('gsecrets.json', scope)

gc = gspread.authorize(credentials)
table = gc.open("yt-tut").sheet1


def getCellValue(row, col):
    return table.cell(row, col).value


def setCellValue(row, col, value):
    table.update_cell(row, col, value)


def setRowValues(row, values):
    for i, v in enumerate(values):
        setCellValue(row, i + 1, v)


def getNextRow():
    count = 1
    while len(table.row_values(count)[0]) > 0:
        count += 1
    return count


def append(values):
    setRowValues(getNextRow(), values)


# test = [
#     ["A1", "B1", "C1"],
#     ["A2", "B2", "C2"],
#     ["A3", "B3", "C3"]
# ]

# for v in test:
#     append(v)
