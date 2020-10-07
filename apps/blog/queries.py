from graphene import ID, Field, List

from .models import Post, Comment
from .types import PostType, CommentType


class BlogQuery(object):
    post = Field(PostType, id=ID(required=True))
    posts = List(PostType)
    comment = Field(CommentType, id=ID(required=True))
    comments = List(CommentType)

    def resolve_post(self, info, id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return None

    def resolve_posts(self, info):
        return Post.objects.all()

    def resolve_comment(self, info, id):
        try:
            return Comment.objects.get(pk=id)
        except Comment.DoesNotExist:
            return None

    def resolve_comments(self, info):
        return Comment.objects.select_related("post").all()
