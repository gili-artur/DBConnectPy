from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def create(request):
    # error = ''
    # if request.method == 'POST':
    #     form = UsersForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('database')
    #     else:
    #         error = 'Форма была неверной'
    #
    # form = UsersForm()
    # data = {
    #     'form': form,
    #     'error': error
    # }

    # return render(request, 'dbconn/create.html', data)
    pass
