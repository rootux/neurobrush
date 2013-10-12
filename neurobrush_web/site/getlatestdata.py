import redis

REDIS_URL = 'redis://redistogo:ed568b706b4474886cf3bbd5161e2166@tarpon.redistogo.com:10054'

redis = redis.from_url(REDIS_URL)
def getlatest(request):
    
    global redis

    return redis.get('ExcitementShortTerm')