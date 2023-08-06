
import datetime
import pyspark.sql.functions as fn
from pyspark.sql.types import *
from pyspark.sql import Window, DataFrame

class SparkCacheNotConfigError(Exception):
    def __init__(self):
        super().__init__("You must run SparkCache.regist({job}, {hdfs_prefix}) first!!")


class SparkCache(object):
    cache = None
    job = None
    hdfs_prefix = None
    registed = False
    dt = datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(days=2), '%Y-%m-%d')
    def __init__(self):
        if not self.registed:
            raise SparkCacheNotConfigError
    @classmethod
    def regist(cls, job, hdfs_prefix):
        cls.job = job
        cls.hdfs_prefix = hdfs_prefix
        cls.registed = True
        cls.cache = SparkCache()
        globals()['cache'] = cls.cache

    def hdfspath(self, field):
        return f"{self.hdfs_prefix}/{self.job}/{field}/{self.dt}"
    
    def set(self, field, df):
        assert isinstance(df, DataFrame)
        name = f"df_{field}"
        setattr(self, name, df)
    
    def get(self, field):
        name = f"df_{field}"
        assert hasattr(self, name)
        df = getattr(self, name)
        return df
