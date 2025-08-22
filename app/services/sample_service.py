from app.repo.sample_repo import SampleRepository
from app.schema.sample_schema import SampleDataResponse
from fastapi_pagination import Params, paginate

import logging

class SampleService:
    def __init__(self, sample_repo: SampleRepository):
        self.repo = sample_repo

    async def get_sample_data(self, search_parameter: str, params: Params) -> SampleDataResponse:
        try:
            res = await self.repo.fetch_sample_data(search_parameter)
            page_data = paginate(res, params)
            return SampleDataResponse(
                item_datas=page_data.items,
                total=page_data.total,
                page=page_data.page,
                size=page_data.size,
                pages=page_data.pages
            )
        except Exception as e:
            logging.error(f"Error searching stock tags: {str(e)}")
            return None

