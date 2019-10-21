from django.shortcuts import render
from django.http import HttpResponse
from notes.data import NOTES
# Create your views here.

def notes_view(request):
    return render(request, 'notes/notes.html', {
        'notes': NOTES,
    })

def note_detail(request, id):
    note = NOTES[id]
    return render(request, 'notes/note_detail.html',
                {'note': note})