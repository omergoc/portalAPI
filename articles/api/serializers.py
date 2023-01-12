from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    content = serializers.CharField()
    video_link = serializers.CharField()
    writer = serializers.IntegerField()
    last_edit = serializers.IntegerField()
    created_date = serializers.DateTimeField(read_only=True)
    category = serializers.IntegerField()
    image = serializers.ImageField()
    slug = serializers.CharField()
    views = serializers.IntegerField()
    available = serializers.BooleanField()

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.content = validated_data.get('content', instance.content)
        instance.video_link = validated_data.get('video_link', instance.video_link)
        instance.writer = validated_data.get('writer', instance.writer)
        instance.last_edit = validated_data.get('last_edit', instance.last_edit)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.category = validated_data.get('category', instance.category)
        instance.image = validated_data.get('image', instance.image)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.views = validated_data.get('views', instance.views)
        instance.available = validated_data.get('available', instance.available)
        return instance
