from rest_framework import serializers
from articles.models import Article, Categories
from users.models import Account


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','first_name','last_name']
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    writer = UserInfoSerializer()
    last_edit = UserInfoSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):

    def validate(self, data):
        return data

    class Meta:
        model = Article
        fields = '__all__'


class ArticleUpdateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_empty_file=True, allow_null=False, required=False)
    class Meta:
        model = Article
        fields = ['title','description','content','last_edit','category','image','views','available']
