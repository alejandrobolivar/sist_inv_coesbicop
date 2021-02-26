from django.contrib import admin

# Register your models here.

from apps.medicamento.models import Medicamento
#admin.site.register(Medicamento)

@admin.register(Medicamento)
class PostAdmin(admin.ModelAdmin):
    list_display = ('cod_med', 'principio_activo_med', 'nombre_comercial_med', 'nombre_lab_med', 'grupo_med', 'subgrupo_med', 'fecha_vencimiento_med')
    list_filter = ('cod_med', 'principio_activo_med', 'nombre_comercial_med', 'nombre_lab_med')
    search_fields = ('cod_med', 'principio_activo_med')
    prepopulated_fields = {'principio_activo_med': ('cod_med',)}
    # raw_id_fields = ('nombre_comercial_med',)
    date_hierarchy = 'fecha_vencimiento_med'
    ordering = ('cod_med', 'nombre_comercial_med')