# app/services/google_api.py

from datetime import datetime

from aiogoogle import Aiogoogle

<<<<<<< HEAD
from app.services.utils import (
    SPREADSHEET_DEFAULT,
    PERMISSIONS_DEFAULT
)
=======
from app.core.config import settings
>>>>>>> c5a25221ecd8c64bdd0de855ebccb23c8c63539d

FORMAT = "%Y/%m/%d %H:%M:%S"


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    now_date_time = datetime.now().strftime(FORMAT)
<<<<<<< HEAD
    title = f'Отчет от {now_date_time}'
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = SPREADSHEET_DEFAULT.copy()
    spreadsheet_body['properties']['title'] = title

=======
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = {
        'properties': {'title': f'Отчет от {now_date_time}',
                       'locale': 'ru_RU'},
        'sheets': [{'properties': {'sheetType': 'GRID',
                                   'sheetId': 0,
                                   'title': 'Отчеты QRkot',
                                   'gridProperties': {'rowCount': 60,
                                                      'columnCount': 8}}}]
    }
>>>>>>> c5a25221ecd8c64bdd0de855ebccb23c8c63539d
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheetid = response['spreadsheetId']
<<<<<<< HEAD
=======
    print(f'https://docs.google.com/spreadsheets/d/{spreadsheetid}')
>>>>>>> c5a25221ecd8c64bdd0de855ebccb23c8c63539d
    return spreadsheetid


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
<<<<<<< HEAD
    permissions_body = PERMISSIONS_DEFAULT.copy()
=======
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
>>>>>>> c5a25221ecd8c64bdd0de855ebccb23c8c63539d
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheetid: str,
        сharity_projects: list,
        wrapper_services: Aiogoogle
) -> None:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = [
        ['Отчёт от', now_date_time],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]
    # Здесь в таблицу добавляются строчки
    for prj in сharity_projects:
        new_row = [
            prj.name,
            str(prj.close_date - prj.create_date),
            prj.description]
        table_values.append(new_row)

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range='A1:E30',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )