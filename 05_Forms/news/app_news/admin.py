from django.contrib import admin
from .models import NewsItem, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'is_active']
    list_filter = ['is_active']
    inlines = [CommentInLine]

    actions = ['mark_as_active', 'mark_as_inactive', ]

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_as_inactive(self, request, queryset):
        queryset.update(is_active=False)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'display_content', 'news_item']
    list_filter = ['user_name']

    actions = ['mark_as_deleted', ]

    def mark_as_deleted(self, request, queryset):
        queryset.update(content='Удалено администратором')



admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(Comment, CommentAdmin)