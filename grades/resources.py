from import_export import resources
from .models import GradeData

class GradeResource(resources.ModelResource):
    class Meta:
        model = GradeData
