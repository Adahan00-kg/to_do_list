from .models import Book
from modeltranslation.translator import TranslationOptions,register

@register(Book)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')