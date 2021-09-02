from django.contrib import admin
# из файла models импортируем модель Post
from .models import Post

class PostAdmin(admin.ModelAdmin):
    # перечисляем поля, которые будут отображаться в админке
    list_display = ("text", "pub_date", "author")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("text",)
    # Добавляем возможность фильтрации по дате
    list_filter = ("pub_date",)

# при регистрации модели Post источником конфигурации для неё 
# назначаем класс PostAdmin
admin.site.register(Post, PostAdmin)