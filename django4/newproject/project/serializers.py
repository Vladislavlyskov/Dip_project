from rest_framework import serializers
from .models import Comment, Model


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'firstname', 'lastname', 'age', 'text')

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ('title', 'price', 'amount', 'comment')