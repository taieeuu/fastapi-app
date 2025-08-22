# app/dependencies.py
from fastapi import Depends

from app.services.sample_service import SampleService
from app.repo.sample_repo import SampleRepository
from app.db.connect_to_mdc import to_mdc_prod
from app.db.connect_to_redis import RedisConnectionFactory
import logging

def get_sample_repository():
    logging.debug("@@@ get_sample_repository")
    conn_mdc = to_mdc_prod()
    conn_redis = RedisConnectionFactory.get_client()
    return SampleRepository(conn_mdc, conn_redis)

def get_sample_service(repo: SampleRepository = Depends(get_sample_repository)):
    logging.debug('@@@ get_sample_repository')
    return SampleService(repo)
