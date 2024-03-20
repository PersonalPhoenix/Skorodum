from rest_framework import serializers

from .models import (
    Game,
    Round,
    Question,
 #   AnswerOptions, 
    Category,
    #MediaFile,
    File
)


# class AnswerOptionsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = AnswerOptions
#         fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=True, read_only=True)
    #answeroptions_set = AnswerOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'file', 'uploaded_at')

class RoundSerializer(serializers.ModelSerializer):

    question_set = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Round
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):

    round_set = RoundSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = '__all__'

# class MediaFileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MediaFile
#         fields = "__all__"