from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from main_app.forms import WriteLineForm
from main_app.models import Customer

class MainView(View):

    def get(self, request):
        contexst = {
            'form': WriteLineForm(),
            'title': "Form",
        }
        return render(request, 'form.html', contexst)

    def post(self, request):
        form = WriteLineForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data
            # firstname = data.get('firstname')
            # lastname = data.get('lastname')
            # age = data.get('age')
            # comment = data.get('comment')
            # print(f'{firstname}|{lastname}|{age}|{comment}')
            Customer.objects.create(
                firstname=form.cleaned_data.get("firstname"),
                lastname=form.cleaned_data.get("lastname"),
                age=form.cleaned_data.get("age")
            )
            context = {
                "users": Customer.objects.all(),
                "title": "Profile"
            }
            # data['title'] = "Profile"
            return render(request, 'profile.html', context)

def one(request):
    # return redirect(two) # view name
    # return redirect('two') # url name
    return redirect('/two/') # url

def two(request):
    return JsonResponse({'result': "Hello World!"})

