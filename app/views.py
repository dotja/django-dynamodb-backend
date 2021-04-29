from django.shortcuts import render
from .models import MyTable
from .forms import MyForm
from datetime import datetime



def home(request):
	return render(request, 'home.html')



def entry(request):
	form = MyForm()
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			foo = MyTable(
				name=form.cleaned_data['name'],
				diet=form.cleaned_data['diet'],
				email=form.cleaned_data['email'],
				created_on=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
			)
			foo.save()
		else:
			return render(request,  'entry.html', {'form': form, 'error': 'Bad data entry.'})
		return render(request, 'entry.html', {'form': MyForm()})
	return render(request, 'entry.html', {'form': form})




