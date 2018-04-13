from tastypie.resources import ModelResource
from narratives.models import ICMJSON
from tastypie.authorization import Authorization
authorization = Authorization()


class NarrativeResource(ModelResource):
    class Meta:
        queryset = ICMJSON.objects.all()
        resource_name = 'icmjson'
