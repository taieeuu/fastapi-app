import logging
from abc import ABC, abstractmethod
from typing import List, Dict

class SampleRepository():
    def __init__(self, conn_mdc, conn_dfa, conn_redis):
        self.conn_mdc = conn_mdc
        self.conn_dfa = conn_dfa
        self.conn_redis = conn_redis

    async def fetch_sample_data(self, msg: str):
        data = [f"Hello {msg}"]
        return data
