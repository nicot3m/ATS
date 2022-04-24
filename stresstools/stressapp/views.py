from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FileForm, FolderForm
from .models import File, Folder
from tools.list_files import simple_function
import glob, os

path_folder = r"C:\Users\nicot\NICO\INFO\PROJETS_PRO\AST\test\*.txt"

# Create your views here.
def index(request):

    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            print("file name", request.FILES)
            print("path", request.POST) 
            os.system('explorer')
            form.save()
            print("Current working dir :", os.getcwd())
            return HttpResponseRedirect(request.path_info)
    else:
        form = FileForm()

    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            print("path", request.POST) 
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = FolderForm()

    folder_all = Folder.objects.all()
    folder_first = Folder.objects.get(name="dir3")
    print(folder_first.name)
    print(folder_first.path)
    """
    return render(request, 'stressapp/index.html', locals())


    if request.method == 'POST' and 'run_script' in request.POST:

        # import function to run
        from script.list_files import function_to_run

        # call function
        function_to_run() 

        # return user to required page
        return HttpResponseRedirect(request.path_info)
    
    elif request.method == 'GET':
        return HttpResponseRedirect(request.path_info)
        # return render(request, "stressapp/index.html", locals())
    """
    return render(request, "stressapp/index.html", locals())
    

def call_simple_function(request):
    list_file = simple_function(path_folder)
    return render(request, "stressapp/index.html", locals())
    
