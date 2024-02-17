from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question,Note
from django.urls import reverse
from .forms import NoteForm


def index(request):
    template = loader.get_template("create.html")
    return HttpResponse(template.render())

def create_note(request):
  if request.method == 'POST':
    form = NoteForm(request.POST)
    if form.is_valid():
      note = Note.objects.create(
        title=form.cleaned_data['title'],
        content=form.cleaned_data['content'],
        reminder_date=form.cleaned_data['reminder_date'],
        category=form.cleaned_data['category'],
      )
      return redirect('note_detail', pk=note.pk)
  else:
    form = NoteForm()
  return render(request, 'create_note.html', {'form': form})

def note_detail(request, pk):
  note = Note.objects.get(pk=pk)
  return render(request, 'note_detail.html', {'note': note})

def delete_note(request, pk):
  note = Note.objects.get(pk=pk)
  note.delete()
  return redirect('home')
