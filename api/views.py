from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notes
from .serializers import NoteSerializer

# We will use function base views


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Create new note with data passed via post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing note '
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete an existing note'
        },

    ]

    return Response(routes)
@api_view(['GET'])
def notes(request):
    notes= Notes.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request , pk):
    note = Notes.objects.get(id = pk)
    serializer = NoteSerializer(note, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request): 
    
    data  = request.data
    note = Notes.objects.create(
        title = data['title'],
        description= data['description']
    )
    
    serializer = NoteSerializer(note , many = False)
    return Response(serializer.data)

@api_view(["PUT"])
def updateNote(request, pk):
    data = request.data
    note = Notes.objects.get(id = pk)
    serializer = NoteSerializer(note , data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Notes.objects.get(id= pk)
    note.delete()
    
    return Response('Note was deleted')
    
    
