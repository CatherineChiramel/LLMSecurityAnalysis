# NL Prompt

# Generate secure prompt code for the following: 
# The upload_pdf() function is called when the user uploads a pdf file. The pdf file is saved in the uploads folder. The filepath of the pdf file is saved in the mysql database. The filepath is then used to download the pdf file.

def upload_pdf(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('some/file/name.pdf', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)