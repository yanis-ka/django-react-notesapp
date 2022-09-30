from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


def updateNote(request, id):
    note = Note.objects.get(id=id)
    serializer = NoteSerializer(instance=note, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


def getNoteDetail(request, id):
    note = Note.objects.get(id=id)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def getNotesList(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


def createNote(request):
    data = request.data
    note = Note.objects.create(body=data['body'])
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def deleteNote(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return Response('Note deleted!')