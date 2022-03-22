from django.http import HttpResponse

def home(request):
   text = """<h1>our mind blowing home page after PR + More PRRRRRRRRRRRRR. + More PRRRRRRRRRRRRRRR with v2.1</h1>"""
   return HttpResponse(text)