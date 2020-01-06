from django.contrib import admin

from .models import GradeData
from import_export.admin import ImportExportModelAdmin, ImportMixin

@admin.register(GradeData)
class GradeAdmin(ImportExportModelAdmin, ImportMixin):
    from_encoding = 'euc-kr'

    # from_encoding = 'utf-8'

    list_display = ('s_name', 'sid', 'lecture', 'year', 'semester', 'mid_term', 'final_term')
    pass


# admin.site.register(GradeData, GradeAdmin)