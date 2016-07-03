from django.shortcuts import render

from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required(login_url='/admin/login/')
def home(request):
    return render_to_response('useradmin/home.html', context_instance=RequestContext(request))
