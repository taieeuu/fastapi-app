from datetime import datetime, timedelta
import pytz
import json


def store_resp_redis(redis_client, key, response, save_time: int):
    try:
        response_value = json.dumps(response)
        redis_client.set(key, response_value)
        redis_client.expire(key, save_time)
        print(f"Response for code {key} stored in Redis")
    except Exception as e:
        print(f"Error setting key in Redis: {e}")

def redis_save_time(hour: int = 17, minute: int = 0, second: int = 0, microsecond: int = 0):
    taiwan_tz = pytz.timezone("Asia/Taipei")
    now = datetime.now(taiwan_tz)
    save_time = now.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)
    if now > save_time:
        save_time += timedelta(days=1)
    trans_time = int((save_time - now).total_seconds())
    return trans_time

def redis_key(service_name: str, request: dict):
    return f"{service_name}-request:{json.dumps(request, sort_keys=True)}"

def custom_round(n: float, digits: int = 0) -> float:
    factor = 10 ** digits
    if n >= 0:
        return int(n * factor + 0.5) / factor
    else:
        return int(n * factor - 0.5) / factor