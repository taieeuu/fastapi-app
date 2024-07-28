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
    next_midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    seconds_until_midnight = int((next_midnight - now).total_seconds())
    try:
        response_value = json.dumps(response)
        redis_client.set(code, response_value)
        redis_client.expire(code, seconds_until_midnight)
        logging.info(f"Response for code {code} stored in Redis under key {response_value}")
        logger.info(f"Response for code {code} stored in Redis under key {response_value}")
    except Exception as e:
        logging.error(f"Error setting key in Redis: {e}")
        logger.error(f"Error setting key in Redis: {e}")
