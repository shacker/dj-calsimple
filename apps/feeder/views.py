import urllib2
from django.utils.simplejson import dumps, loads as jsonloader
from django.shortcuts import render
from django.utils.encoding import force_unicode


def flickr_feed(request):
	"""
	Display Flickr favorites
	"""

	url = 'https://calcentral-dev.berkeley.edu/data/colleges-and-schools.json'
	jsondata = urllib2.urlopen(url).read()
	data = jsonloader(jsondata, object_hook=_decode_dict)
	print dir(data)
	# for d in data['collegesandschools'].iterkeys():
	# 	print d


	return render(
		request, 'feeder/flickr.html', locals()
	)



# Need this hook for json loads to coerce back from unicode
def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
           key = key.encode('utf-8')
        if isinstance(value, unicode):
           value = value.encode('utf-8')
        elif isinstance(value, list):
           value = _decode_list(value)
        elif isinstance(value, dict):
           value = _decode_dict(value)
        rv[key] = value
    return rv