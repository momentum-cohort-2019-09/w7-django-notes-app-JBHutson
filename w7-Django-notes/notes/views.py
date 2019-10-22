from django.shortcuts import render
from django.http import HttpResponse
from notes.models import Note, NoteForm
from django.views.generic.edit import FormView
# Create your views here.

def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/notes.html', {
        'notes': notes,
    })

def note_detail(request, pk):
    note = Note.objects.get(prim_id=pk)
    return render(request, 'notes/note_detail.html',
                {'note': note})

def add_note(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'notes/add_note.html')