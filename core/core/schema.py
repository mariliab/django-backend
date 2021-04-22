import graphene
from graphene import Schema, ObjectType
import ads.schema
import users.qql.schema


class Query(ads.schema.Query, users.qql.schema.Query, graphene.ObjectType):
    pass


class Mutation(ads.schema.Mutation, users.qql.schema.Mutation, graphene.ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)