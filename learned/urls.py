from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers, serializers, viewsets
from .models import Learning, Tag

from . import views

# Serializers define the API representation.
class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
    
class LearningSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Learning
        fields = ['id', 'learning_title', 'learning_text', 'created_date', 'modified_date', 'tags', '__str__', 'status']
    
# ViewSets define the view behavior.
class LearningViewSet(viewsets.ModelViewSet):
    queryset = Learning.objects.filter(status='published')
    serializer_class = LearningSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'learnings', LearningViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    path('', views.index, name='index'),
    path('learning/<int:id>', views.learning, name='learning'),
]
