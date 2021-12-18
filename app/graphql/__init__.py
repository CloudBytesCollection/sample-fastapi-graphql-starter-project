import strawberry
from strawberry.asgi import GraphQL

from app.resolvers.hello.resolve_hello import *


@strawberry.type
class Query:
    hello_world = strawberry.field(resolve_hello_world)


schema = strawberry.Schema(query=Query())
graphql_app = GraphQL(schema, debug=True, )