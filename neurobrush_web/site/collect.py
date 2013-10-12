import json
import ast

def collectData(request):
    array = request.POST.items()[0][0]
    #array is a string
    #array = [s.replace('{', '') for s in array]
    #array = [s.replace('}', '') for s in array]
    splitted = eval(array)

    print splitted['ExcitementShortTerm']
    #json.loads(splitted)
    #excitementShortTerm = request.POST['ExcitementShortTerm']
    #print excitementShortTerm