from app.core.config import settings


DEFAULT_ROW = 60
DEFAULT_COLUMN = 8


SPREADSHEET_DEFAULT = {
    'properties': {'title': 'Отчет',
                   'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Отчеты QRkot',
                               'gridProperties': {
                                   'rowCount': DEFAULT_ROW,
                                   'columnCount': DEFAULT_COLUMN
                               }}}]
}

PERMISSIONS_DEFAULT = {
    'type': 'user',
    'role': 'writer',
    'emailAddress': settings.email
}