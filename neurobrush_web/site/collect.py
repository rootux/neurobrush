import ast
import redis

REDIS_URL = 'redis://redistogo:ed568b706b4474886cf3bbd5161e2166@tarpon.redistogo.com:10054'

redis = redis.from_url(REDIS_URL)
def collectData(request):
    
    global redis

    array = request.POST.items()[0][0]
    splitted = eval(array)
    print splitted
    redis.set('ExcitementShortTerm', splitted['ExcitementShortTerm'])
    #my_global = splitted['ExcitementShortTerm']
    print splitted['ExcitementShortTerm']
    #json.loads(splitted)
    #excitementShortTerm = request.POST['ExcitementShortTerm']
    #print excitementShortTerm