from fastapi import APIRouter
from app.schema.sample_schema import (
    SampleDataRequest,
    SampleDataResponse
)
from app.schema.base import ApiResponse
from app.dependencies.sample_depd import (
    get_sample_service
)

from app.services.sample_service import (
    SampleService
)
from app.dependencies.sample_depd import (
    get_sample_service
)
from fastapi import Depends

from app.apis.return_code import Return_Code

from fastapi_pagination import add_pagination, Params

from app.core.log_config import logger

router = APIRouter()

add_pagination(router)

@router.get("/search_sample_data", response_model=ApiResponse[SampleDataResponse])
async def get_sample_data(
    request: SampleDataRequest = Depends(SampleDataRequest),
    sample_service: SampleService = Depends(get_sample_service)
):
    try:
        logger.info(f"@@@ search_sample_data request {request.pagination=}")
        params = Params(page=request.pagination.page, size=request.pagination.size)
        res = sample_service.get_sample_data(request.msg, params)
        return ApiResponse[SampleDataResponse](
            return_code=100,
            message=Return_Code[100],
            data=res
        )
    except Exception as e:
        logger.error(f"@@@ /customer/search_stock request error {e}")
        return ApiResponse[SampleDataResponse](
            return_code=500,
            message=f"Fetch sample data error: {str(e)}",
            data=None
        )
