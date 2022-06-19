from django.http import JsonResponse
from .serializers import CommentSerializer, ModelSerializer
from .models import Comment, Model


def api_comments(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)

def api_models(request):
    if request.method == "GET":
        model = Model.objects.all()
        serializer = ModelSerializer(model, many=True)
        return JsonResponse(serializer.data, safe=False)
