import io

import rest_framework
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class drf_model:
    def __init__(self,title,content):
        self.title=title
        self.content=content

class Ser(serializers.Serializer):
    title=serializers.CharField()
    content=serializers.CharField()

def encode():
    model=drf_model('title','content')
    model_sr=Ser(model)


    json=JSONRenderer().render(model_sr.data)
    print(json)

def decode():
    data=io.BytesIO(b'{"title":"2wefgb","content":"efrvegbfrf"}')
    d=JSONParser().parse(data)
    serializers=Ser(data=d)
    serializers.is_valid()
    print(serializers.validated_data)

