from graphene import ID, Field, Mutation
from graphene.relay import ClientIDMutation

from .models import Post, Comment
from .types import PostType, CommentType
from .inputs import CreatePostInput, UpdatePostInput, CreateCommentInput, UpdateCommentInput


class CreatePost(ClientIDMutation):
    Input = CreatePostInput
    post = Field(PostType)

    @staticmethod
    def mutate_and_get_payload(root, info, **input):
        post = Post.objects.create(**input)
        return CreatePost(post=post)


class UpdatePost(ClientIDMutation):
    Input = UpdatePostInput
    post = Field(PostType)

    @staticmethod
    def mutate_and_get_payload(root, info, **input):
        post_id = input.pop('id')
        if Post.objects.filter(pk=post_id).update(**input):
            post = Post.objects.get(pk=post_id)
            return UpdatePost(post=post)
        else:
            return UpdatePost(post=None)


class DeletePost(Mutation):
    class Arguments:
        id = ID(required=True)

    post = Field(PostType)

    def mutate(self, info, id):
        try:
            post = Post.objects.get(pk=id)
            post.delete()
            return post
        except Post.DoesNotExist:
            return DeletePost(post=None)


class CreateComment(ClientIDMutation):
    Input = CreateCommentInput
    comment = Field(CommentType)

    @staticmethod
    def mutate_and_get_payload(root, info, **input):
        comment = Comment.objects.create(**input)
        return CreateComment(comment=comment)


class UpdateComment(ClientIDMutation):
    Input = UpdateCommentInput
    comment = Field(CommentType)

    @staticmethod
    def mutate_and_get_payload(root, info, **input):
        comment_id = input.pop('id')
        if Comment.objects.filter(pk=comment_id).update(**input):
            comment = Comment.objects.get(pk=comment_id)
            return UpdateComment(comment=comment)
        else:
            return UpdateComment(comment=None)


class DeleteComment(Mutation):
    class Arguments:
        id = ID(required=True)

    comment = Field(CommentType)

    def mutate(self, info, id):
        try:
            comment = Comment.objects.get(pk=id)
            comment.delete()
            return comment
        except Comment.DoesNotExist:
            return DeleteComment(comment=None)


class BlogMutation:
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
    delete_comment = DeleteComment.Field()
