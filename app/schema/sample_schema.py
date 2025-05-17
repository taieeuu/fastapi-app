from app.mixins.validation_mixins import DateRangeMixins, MarketMixins, TotalDividendTransformMixins
from typing import List
from pydantic import BaseModel, Field

class PageRequest(BaseModel):
    page: int = Field(1, description="page")
    size: int = Field(20, description="size")

class PageResponse(BaseModel):
    item_datas: List[dict] = Field([], description="item_datas")
    total: int = Field(0, description="total")
    page: int = Field(1, description="page")
    size: int = Field(20, description="size")
    pages: int = Field(0, description="pages")

class SampleDataRequest(BaseModel):
    msg: str = Field("", description="msg")
    page: int = Field(1, description="now page")
    size: int = Field(20, description="page size")

    @property
    def pagination(self) -> PageRequest:
        return PageRequest(page=self.page, size=self.size)

class SampleDataResponse(BaseModel):
    item_datas: List[dict] = Field([], description="data")
    total: int = Field(0, description="total")
    page: int = Field(1, description="page")
    size: int = Field(20, description="size")
    pages: int = Field(0, description="pages")
