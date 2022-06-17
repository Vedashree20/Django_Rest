from curses import use_default_colors
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
#       title=serializers.CharField(max_length=100)
#       author=serializers.CharField(max_length=100)
#       email=serializers.EmailField(max_length=100)
#       date=serializers.DateTimeField() #according to class being used

#       #create and update for serializer

       
# def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Article.objects.create(**validated_data)

# def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance

          class Meta:
              model=Article
              fields=['id','title','author']

              