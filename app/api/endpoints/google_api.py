from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser
from app.services.google_api import (
    spreadsheets_create,
    set_user_permissions,
    spreadsheets_update_value
)
from app.crud.charity_project import charity_project_crud


router = APIRouter()


@router.post(
    '/',
    response_model=dict[str, str],
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)
):
    """Только для суперюзеров."""
    projects = await charity_project_crud.get_projects_by_completion_rate(
        session
    )
    spreadsheetid = await spreadsheets_create(wrapper_services)
    link = f'https://docs.google.com/spreadsheets/d/{spreadsheetid}'

    await set_user_permissions(spreadsheetid, wrapper_services)
    await spreadsheets_update_value(spreadsheetid,
                                    projects,
                                    wrapper_services)
    return {'report_link': link}
