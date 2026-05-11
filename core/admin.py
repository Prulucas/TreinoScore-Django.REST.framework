from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/style.css',)  # O caminho para o seu CSS suave
        }
