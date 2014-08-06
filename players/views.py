from django.shortcuts import *
from players.models import player
from forms import PlayerForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import re
from django.db.models import Q

# Create your views here.
def home (request):
	return render(request,'front.html')

def players(request):
    return render_to_response('players.html', {'players': player.objects.all() })

def players_id(request, player_id=1):
    return render_to_response('player.html', {'player': player.objects.get(id=player_id) })
 




def create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()

            return  HttpResponseRedirect('/players/all')
    else:
        form = PlayerForm()

    args = { }
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_player.html', args)
		

def search_new(request):
	"""
	** search **
	Here's the new search.
	The function get_query is defined in funcions.py file
	"""
	query_string = ''
	found_entries = None
	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		entry_query = get_query(query_string, ['name', 'fight',
	'chest', 'height','biceps','weight','rank'])
		found_entries = player.objects.filter(entry_query).order_by('name')
	temp = { 'query_string': query_string, 'found_entries': found_entries }
	return render_to_response('search_result.html', dict(temp.items() + temp.items()), context_instance=
	RequestContext(request))


def normalize_query(query_string,
	findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 


def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query