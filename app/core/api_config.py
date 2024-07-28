# API Config
class APIConfig():
    def __init__(self):
        # redis cache time
        self.CACHE_TIME = 3600
        self.MAX_LIMIT = 100
        self.EX_PARAM = 'ex_param'
pk_index1_cfg = APIConfig()