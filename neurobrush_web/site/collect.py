import ast
import redis

REDIS_URL = 'redis://redistogo:ed568b706b4474886cf3bbd5161e2166@tarpon.redistogo.com:10054'

def collectData(request):
    
    #TODO!!!
    redis = redis.from_url(REDIS_URL)

    array = request.POST.items()[0][0]
    splitted = eval(array)
    redis.set('ExcitementShortTerm', splitted['ExcitementShortTerm'])
    #my_global = splitted['ExcitementShortTerm']
    print splitted['ExcitementShortTerm']
    #json.loads(splitted)
    #excitementShortTerm = request.POST['ExcitementShortTerm']
    #print excitementShortTerm