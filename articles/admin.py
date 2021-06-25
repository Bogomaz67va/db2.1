from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        has_tag = False

        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                counter += 1
            if form.cleaned_data.get('tag'):
                has_tag = True

        if counter == 0 and has_tag:
            raise ValidationError('Укажите основной раздел')
        elif counter > 1:
            raise ValidationError('Может быть только один основной раздел')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['title', 'published_at']
    search_fields = ['title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...
