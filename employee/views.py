from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Employee


def index(request):
    employee = Employee.objects.all()
    print(employee)
    context = {'employee': employee}

    if 'edit_id' in request.GET:
        context = {**context, 'message': 'edit', 'message_id': request.GET['edit_id']}

    if 'delete_id' in request.GET:
        context = {**context, 'message': 'delete', 'message_id': request.GET['delete_id']}

    template = loader.get_template('movies/index_employee.html')
    return HttpResponse(template.render(context, request))


def create_new(request):
    print('hello')
    if request.method == 'POST':
        print(request.POST)
        print(request.POST['name'],request.POST['date_of_brith'],request.POST['description'],request.POST['os'],request.POST['title'])
        employee = Employee(
            name=request.POST['name'],
            date_of_brith=request.POST['date_of_brith'],
            description=request.POST['description'],
            os=request.POST['os'],
            title=request.POST['title']
        )
        print('employee', employee)
        employee.save()
        print('employee', employee.id)
        return HttpResponseRedirect(reverse('movies_index_employee') + '?edit_id=' + str(employee.id))

    context = {}
    template = loader.get_template('movies/create_employee.html')
    return HttpResponse(template.render(context, request))

#
# def view(request, movie_id=None):
#     movie = Movie.objects.filter(id=movie_id).first()
#     context = {'movie': movie}
#     template = loader.get_template('movies/view.html')
#     return HttpResponse(template.render(context, request))
#
#
# def edit(request, movie_id=None):
#     movie = Movie.objects.filter(id=movie_id).first()
#
#     if request.method == 'POST':
#         movie.title = request.POST['title']
#         movie.synopsis = request.POST['synopsis']
#         movie.actors = request.POST['actors']
#         movie.genre = request.POST['genre']
#         movie.duration = request.POST['duration']
#         movie.rate = request.POST['rate']
#         movie.save()
#         return HttpResponseRedirect(reverse('movies_index') + '?edit_id=' + str(movie.id))
#
#     context = {'movie': movie}
#     template = loader.get_template('movies/edit.html')
#     return HttpResponse(template.render(context, request))
#
#
# def delete(request, movie_id=None):
#     movie = Movie.objects.filter(id=movie_id).first()
#
#     if request.method == 'POST':
#         movie = Movie.objects.filter(id=movie_id).delete()
#         return HttpResponseRedirect(reverse('movies_index') + '?delete_id=' + str(movie_id))
#
#     context = {'movie': movie}
#     template = loader.get_template('movies/delete.html')
#     return HttpResponse(template.render(context, request))