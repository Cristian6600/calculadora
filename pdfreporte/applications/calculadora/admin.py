from django.contrib import admin

from .models import laplace, laplace_2, laplace_3, laplace_4, laplace_5, laplace_6, laplace_7, laplace_8


class LaplaceAdmin(admin.ModelAdmin):
    fields = (
        ('var_1', 'var_2', 'var3'),
        ('var_s_1', 'var_s_2'),
        ('numerador'),
        ('denominador'),
        'tota'
        
    )

admin.site.register(laplace, LaplaceAdmin)
admin.site.register(laplace_2)
admin.site.register(laplace_3)
admin.site.register(laplace_4)
admin.site.register(laplace_5)
admin.site.register(laplace_6)
admin.site.register(laplace_7)
admin.site.register(laplace_8)