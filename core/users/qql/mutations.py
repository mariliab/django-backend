from graphene import Field, Mutation, String
from django.contrib.auth import get_user_model
from .types import UserType

User = get_user_model()


class UserCreate(Mutation):
    user = Field(UserType)

    class Arguments:
        email = String(required=True)
        username = String(required=True)
        password = String(required=True)

    def mutate(self, info, email, username, password):
        user = User(email=email, username=username)
        user.set_password(password)
        user.save()
        return UserCreate(user=user)