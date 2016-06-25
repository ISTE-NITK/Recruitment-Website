from django.shortcuts import render

def index(request):
	return render(request, 'webapp/home.html')
	
def contact(request):
	return render(request, 'webapp/basic.html', {'content':['If you would like to contact me, please email me','shivshnkr420@gmail.com']})