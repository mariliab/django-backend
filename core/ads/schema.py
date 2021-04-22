import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from .models import Ad, Category


class AdType(DjangoObjectType):
    class Meta:
        model = Ad
        fields = ("id", "title", "description", "category")


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "title")


class Query(ObjectType):
    get_ads = graphene.List(AdType)
    get_categories = graphene.List(CategoryType)

    def resolve_get_ads(self, info, **kwargs):
        ads = Ad.objects.all()
        return ads

    def resolve_get_categories(self, info, **kwargs):
        categories = Category.objects.all()
        return categories


class Mutation(ObjectType):
    pass