
class SparkCache(object):
    cache = None
    @staticmethod
    def singleton_cache():
        if not SparkCache.cache:
            SparkCache.cache = SparkCache()
        return SparkCache.cache
    def __init__(self):
        pass

singleton_cache = SparkCache.singleton_cache
