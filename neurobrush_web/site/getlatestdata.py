import redis

REDIS_URL = 'redis://redistogo:ed568b706b4474886cf3bbd5161e2166@tarpon.redistogo.com:10054'

def getlatest(request):
    
    #TODO!!!
    redis = redis.from_url(REDIS_URL)

    return redis.get('ExcitementShortTerm')