from django.contrib import admin
from django.urls import reverse

from provider.models import Supplier, Factory, Retail, Entrepreneur


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    model = Supplier

    list_display = ['title', 'city', 'suppliers']
    list_filter = ['city']


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    model = Factory

    list_display = ['title', 'city', 'debts']
    list_filter = ['city']


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    model = Retail

    list_display = ['title', 'city', 'debts', 'suppliers', 'provider_link']
    list_filter = ['city']
    list_display_links = ['suppliers', 'title', 'provider_link']
    prepopulated_fields = {'title': ('title',)}
    actions = ['clean_debts']

    @admin.action(description="clean")
    def clean_debts(modeladmin, request, queryset):
        queryset.update(debts=0)

    def provider_link(self, obj):
        return u'<a href="{0}">{1}</a>'.format(reverse('admin:provider_supplier_change', args=(obj.pk,)),
                                               obj.suppliers.title)

    provider_link.allow_tags = True
    provider_link.short_description = Supplier._meta.get_field('title').verbose_name.title()
    provider_link.admin_order_field = 'title'


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    model = Entrepreneur

    list_display = ['title', 'city', 'debts', 'suppliers']
    list_filter = ['city']
    list_display_links = ['suppliers', 'title']
    actions = ['clean_debts']

    @admin.action(description="clean")
    def clean_debts(modeladmin, request, queryset):
        queryset.update(debts=0)

    def provider_link(self, obj):
        return u'<a href="{0}">{1}</a>'.format(reverse('admin:eshop_supplier_change', args=(obj.pk,)),
                                               obj.provider_title)

    provider_link.allow_tags = True
    provider_link.short_description = Supplier._meta.get_field('title').verbose_name.title()
    provider_link.admin_order_field = 'title'
