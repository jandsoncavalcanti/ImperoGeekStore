import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	os.system('python manage.py clearsessions')
	return render(request, 'index.html', {})