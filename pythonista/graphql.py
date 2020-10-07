from graphene import ObjectType, Schema

from apps.blog.queries import BlogQuery
from apps.blog.mutations import BlogMutation


class Query(
        BlogQuery,

        # lastly,
        ObjectType):
    pass


class Mutation(
        BlogMutation,

        # lastly,
        ObjectType):
    pass

schema = Schema(query=Query, mutation=Mutation)
