from graphene import ID, String, DateTime


class CreatePostInput:
    title = String(required=True)
    description = String()
    author = String(required=True)


class UpdatePostInput:
    id = ID(required=True)
    title = String(required=True)
    description = String()
    published_date = DateTime()
    author = String(required=True)


class CreateCommentInput:
    post_id = ID(required=True)
    text = String(required=True)
    author = String(required=True)


class UpdateCommentInput:
    id = ID(required=True)
    post_id = ID(required=True)
    text = String(required=True)
    author = String(required=True)