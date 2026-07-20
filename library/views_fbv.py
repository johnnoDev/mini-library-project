from django.shortcuts import render, get_object_or_404, redirect
from .models import Author
from .forms import AuthorForm

# ==== READ

def author_list_fbv(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list_fbv.html', {'authors': authors})

def author_detail_fbv(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'library/author_detail_fbv.html', {'author': author})
    
    
# ==== CREATE

def author_create_fbv(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST) # Pasar los datos que tipeo el usuario
        if form.is_valid():
            form.save()
            return redirect('author_list_fbv')
    else:
        """
        si es un GET (primera visita), armás un formulario vacío, sin datos, solo para mostrarlo.
        """
        form = AuthorForm()
    return render(request, 'library/author_form_fbv.html', {'form': form})

# ==== UPDATE
def author_update_fbv(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author) # instance es el equivalente de UpdateView
        if form.is_valid():
            form.save()
            return redirect('author_list_fbv')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'library/author_form_fbv.html', {'form': form})

# === DELETE
def author_delete_fbv(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list_fbv')
    return render(request, 'library/author_confirm_delete_fbv.html', {'author': author})