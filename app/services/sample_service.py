from app.repo.sample_repo import SampleRepository
from app.schema.sample_schema import SampleDataResponse
from fastapi_pagination import Params, paginate

import logging

class SampleService:
    def __init__(self, sample_repo: SampleRepository):
        self.repo = sample_repo

    async def get_sample_data(self, msg: str, params: Params) -> SampleDataResponse:
        try:
            logging.info(f"@@@ get_sample_data")
            res = self.repo.fetch_sample_data(msg)
            item_datas = paginate(res, params)
            return SampleDataResponse(
                item_datas=item_datas,
                total=len(res),
                page=1,
                size=len(res),
                pages=1
            )
        except Exception as e:
            logging.error(f"Error searching stock tags: {str(e)}")
            return []

