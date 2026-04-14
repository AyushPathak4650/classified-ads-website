from django.http import HttpResponse

# Create your views here.
def myview(request):
    visited = request.session.get('nums_visited', 0) + 1
    request.session["nums_visited"] = visited
    if visited > 4: del(request.session["nums_visited"])
    resp = HttpResponse('view count='+str(visited))
    resp.set_cookie('dj4e_cookie', 'ea87054f', max_age=1000)
    return resp
