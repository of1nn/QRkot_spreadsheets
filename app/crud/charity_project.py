from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, extract

from app.crud.base import CRUDBase
from app.models import CharityProject, Donation


class CRUDCharityProject(CRUDBase):
    async def get_id_by_name(
        self, name: str, session: AsyncSession
    ) -> Optional[int]:
        charity_id = await session.execute(
            select(CharityProject.id).where(CharityProject.name == name)
        )
        return charity_id.scalars().first()

    async def get_projects_by_completion_rate(
        self, session: AsyncSession
    ) -> list[CharityProject]:
        projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            ).order_by(
                (
                    extract('year', CharityProject.close_date
                            ) - extract('year', CharityProject.create_date)
                ) * 365 +
                (
                    extract('month', CharityProject.close_date
                            ) - extract('month', CharityProject.create_date)
                ) * 30 +
                (
                    extract('day', CharityProject.close_date
                            ) - extract('day', CharityProject.create_date)
                )
            )
        )
        return projects.scalars().all()


charity_project_crud = CRUDCharityProject(
    model=CharityProject, outer_model=Donation
)
