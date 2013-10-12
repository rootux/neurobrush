import redis

REDIS_URL = 'redis://localhost:6379'
#REDIS_URL = 'redis://redistogo:ed568b706b4474886cf3bbd5161e2166@tarpon.redistogo.com:10054'

redis = redis.from_url(REDIS_URL)
def getlatest(request):
    
    global redis

    # ExcitementShortTerm = redis.get('ExcitementShortTerm')
    # ExcitementLongTerm = redis.get('ExcitementLongTerm')
    # FrustrationScore = redis.get('FrustrationScore')
    # Lowerface = redis.get('Lowerface')
    # LowerfaceValue = redis.get('LowerfaceValue')
    # Upperface = redis.get('Upperface')
    # UpperfaceValue = redis.get('UpperfaceValue')
    
    int_fields = { 'ExcitementShortTerm', 'ExcitementLongTerm', 'FrustrationScore', 'LowerfaceValue', 'UpperfaceValue'}
    js_dict = { f: int(round(100 * float(redis.get(f) or 0))) for f in int_fields }

    str_fields = {'Lowerface', 'Upperface'}
    js_dict.update( {f: redis.get(f) for f in str_fields} )


    #create data
    print js_dict
    return js_dict