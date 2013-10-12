import ast
import redis

#REDIS_URL = 'redis://localhost:6379'
REDIS_URL = 'redis://redistogo:ed568b706b4474886cf3bbd5161e2166@tarpon.redistogo.com:10054'

redis = redis.from_url(REDIS_URL)
def collectData(request):
    
    global redis

    array = request.POST.items()[0][0]
    if not array: return

    print 'about to eval:'
    print array
    splitted = eval(array)
    print splitted
    redis.set('ExcitementShortTerm', splitted['ExcitementShortTerm'])
    redis.set('ExcitementLongTerm', splitted['ExcitementLongTerm'])
    redis.set('EngagementBoredom', splitted['EngagementBoredom'])
    redis.set('FrustrationScore', splitted['FrustrationScore'])
    redis.set('Lowerface', splitted['Lowerface'])
    redis.set('LowerfaceValue', splitted['LowerfaceValue'])
    redis.set('Upperface', splitted['Upperface'])
    redis.set('UpperfaceValue', splitted['UpperfaceValue'])