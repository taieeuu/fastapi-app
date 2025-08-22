from pydantic import field_validator, FieldValidationInfo
from datetime import datetime
from app.common.enums import MarketType

class DateRangeMixins:
    @field_validator('start_date', 'end_date')
    def validate_date_format(cls, v: str, info: FieldValidationInfo) -> str:
        try:
            datetime.strptime(v, "%Y%m%d")
            return v
        except ValueError:
            raise ValueError("日期格式必須為 YYYYMMDD")
        
    @field_validator('end_date')
    def validate_date_range(cls, v, info: FieldValidationInfo):
        if 'start_date' in info.data and v < info.data['start_date']:
            raise ValueError("結束日期不能早於開始日期")
        return v

class MarketMixins:
    @field_validator('market')
    def validate_market(cls, v):
        if v not in [market.value for market in MarketType]:
            raise ValueError(f"市場類型必須是以下之一: {', '.join([market.value for market in MarketType])}")
        return v

class TotalDividendTransformMixins:
    @field_validator('total_dividend')
    def validate_total_dividend(cls, v):
        try:
            return f"{float(v):.2f}"
        except Exception:
            return v
