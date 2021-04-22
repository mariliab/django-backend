from graphene import Field, List, ObjectType, Schema
from .mutations import UserCreate
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required
from graphql_jwt import ObtainJSONWebToken, Verify, Refresh
from .types import UserType

User = get_user_model()


class Query(ObjectType):
    current_user = Field(UserType)

    def resolve_users(self, info):
        return User.objects.all()

    @login_required
    def resolve_current_user(self, info):
        user = info.context.user
        return user


class Mutation(ObjectType):
    user_create = UserCreate.Field()
    token_auth = ObtainJSONWebToken.Field()
    verify_token = Verify.Field()
    refresh_token = Refresh.Field()


schema = Schema(query=Query, mutation=Mutation)