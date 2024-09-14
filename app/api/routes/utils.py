import time
import pytz
import json
from app.core.api_config import *
from datetime import datetime, timedelta
from functools import wraps
from app.core.log_config import logger
import logging

def check_date(collection, code, max_limit):
    query = {'f_2':code}
    logging.debug(f'collection.count_documents(query): {collection.count_documents(query)}')
    return True if collection.count_documents(query) >= max_limit else False

def timeit(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"{func.__name__} 花費 : {elapsed_time:.4f} ")
        return result
    return wrapper

def store_response_in_redis(code, response, redis_client):
    taiwan_tz = pytz.timezone('Asia/Taipei')
    now = datetime.now(taiwan_tz)
    print(f"Now: {now}")
    # 設定今天下午5點的時間
    today_5pm = now.replace(hour=17, minute=0, second=0, microsecond=0)
    print(f"Today 5pm: {today_5pm}")
    # 如果當前時間已經過了今天下午5點，則設置為明天下午5點
    if now > today_5pm:
        today_5pm += timedelta(days=1)
    print(f"Today 5pm: {today_5pm}")
    # 計算從現在到下午5點的秒數
    seconds_until_5pm = int((today_5pm - now).total_seconds())
    print(f"Seconds until 5pm: {seconds_until_5pm}")
    # next_midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    # seconds_until_midnight = int((next_midnight - now).total_seconds())
    try:
        response_value = json.dumps(response)
        redis_client.set(code, response_value)
        redis_client.expire(code, seconds_until_5pm)
        print(f'Response for code {code} stored in Redis')
        # print(f"Response for code {code} stored in Redis under key {response_value}")
    except Exception as e:
        print(f"Error setting key in Redis: {e}")
