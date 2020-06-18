from django.contrib.auth.models import User
from django.contrib import admin
from . import models


class CommentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
        
    list_display = ('text', 'item', 'user', 'added', 'mark')
    
    fields = ('text', 'item', 'user', 'mark', 'added')
    readonly_fields = ('item', 'user', 'mark', 'added')


class CommentInLine(admin.TabularInline):
    def has_add_permission(self, request, obj):
        return False

    model = models.Comment
    fields = ('user', 'text', 'mark', 'added')
    readonly_fields = ('user', 'mark', 'added', 'text')
    ordering = ('-added',)
    show_change_link = True


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'average_mark')
    fields = ('name', 'description', 'price', 'average_mark')
    readonly_fields = ('average_mark', )

    view_on_site = True
    inlines = [CommentInLine,]


class OrderInline(admin.TabularInline):
    def has_add_permission(self, request, obj):
        return False

    model = models.OrderElement
    fields = ('item', 'amount')
    readonly_fields = ('item',)
    ordering = ('-amount',)
    show_change_link = False


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'added', 'is_done')
    fields = ('name', 'email', 'added', 'is_done')
    readonly_fields = ('added',)

    inlines = [OrderInline, ]



admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Order, OrderAdmin)

# Register your models here.
