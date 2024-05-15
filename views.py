from django.shortcuts import render, redirect
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            instance = UploadFileForm(file=uploaded_file, user=request.user)
            instance.save()
            return redirect('success_url')  
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
