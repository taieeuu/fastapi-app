import redis
from app.core.settings.base import RedisSettings
from app.core.log_config import logger
from redis import ConnectionPool
import threading

class RedisConnectionFactory:
    _pool = None
    _lock = threading.Lock()
    
    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            with cls._lock:  # 線程安全
                if cls._pool is None:  # 雙重檢查鎖定
                    cls._pool = ConnectionPool(
                        host=RedisSettings().redis_host,
                        port=RedisSettings().redis_port,
                        password=RedisSettings().redis_pwd,
                        db=RedisSettings().redis_db,
                        decode_responses=True,
                        max_connections=20
                    )
        return cls._pool
    
    @classmethod
    def get_client(cls):
        pool = cls.get_pool()
        return redis.Redis(connection_pool=pool)
    
    @classmethod
    def cleanup(cls):
        if cls._pool:
            cls._pool.disconnect()
            cls._pool = None

