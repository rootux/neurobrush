import ast
import redis

REDIS_URL = 'redis://localhost:6379'
#REDIS_URL = 'redis://redistogo:ed568b706b4474886cf3bbd5161e2166@tarpon.redistogo.com:10054'

redis = redis.from_url(REDIS_URL)
def collectData(request):
    
    global redis

    array = request.POST.items()[0][0]

    print 'about to eval:'
    print array
    splitted = eval(array)
    print splitted
    redis.set('ExcitementShortTerm', splitted['ExcitementShortTerm'])
    redis.set('ExcitementLongTerm', splitted['ExcitementLongTerm'])
    redis.set('EngagementBoredom', splitted['EngagementBoredom'])
    redis.set('FrustrationScore', splitted['FrustrationScore'])
    
    if splitted['Lowerface']:
        redis.set('Lowerface', splitted['Lowerface'])
    else:
        redis.set('Lowerface', splitted[''])

    redis.set('LowerfaceValue', splitted['LowerfaceValue'])
    if splitted['Upperface']:
        redis.set('Upperface', splitted['Upperface'])
    else:
        redis.set('Upperface', splitted[''])
    redis.set('UpperfaceValue', splitted['UpperfaceValue'])