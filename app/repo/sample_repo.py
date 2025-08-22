import logging
from abc import ABC, abstractmethod
from typing import List, Dict

class SampleRepository():
    def __init__(self, conn_mdc, conn_redis):
        self.conn_mdc = conn_mdc
        self.conn_redis = conn_redis

    async def fetch_sample_data(self, search_parameter: str):
        data = [{"message": f"search_parameter: {search_parameter} to fetch db data"}]
        return data
