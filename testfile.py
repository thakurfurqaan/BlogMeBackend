from itsdangerous import Serializer
from api.models import Article
from api.serializers import ArticleSerializer 
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

a = Article(title="article2 title", description="article2 desc")
a.save()

serializer = ArticleSerializer(a)

serializer.data

json = JSONRenderer().render(serializer.data)
json

stream = io.BytesIO(json)
data = JSONParser().parse(stream)

serializer = ArticleSerializer(data=data)
serializer.is_valid()

serializer.validated_data

# --------------------

from api.serializers import ArticleSerializer 
serializer = ArticleSerializer()
print(repr(serializer))