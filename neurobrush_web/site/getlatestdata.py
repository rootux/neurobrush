import redis

"""
Returns a json for the collected values from redis db
For example:
{
    ExcitementShortTerm: 93,
    FrustrationScore: 44,
    Upperface: "LeftWink",
    LowerfaceValue: 21,
    ExcitementLongTerm: 94,
    Lowerface: "Smile",
    UpperfaceValue: 0
}
"""

#REDIS_URL = 'redis://localhost:6379'
REDIS_URL = 'redis://redistogo:ec568a103b3474221cc3abd1121e2166@tarpon.redistogo.com:10054'

redis = redis.from_url(REDIS_URL)
def getlatest(request):
    
    global redis
    
    int_fields = { 'ExcitementShortTerm', 'ExcitementLongTerm', 'FrustrationScore', 'LowerfaceValue', 'UpperfaceValue'}
    js_dict = { f: int(round(100 * float(redis.get(f) or 0))) for f in int_fields }

    str_fields = {'Lowerface', 'Upperface'}
    js_dict.update( {f: redis.get(f) for f in str_fields} )

    #create data
    print js_dict
    return js_dict