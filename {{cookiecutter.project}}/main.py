# -*- coding: utf-8 -*-
# from fastapi import FastAPI
# from graphene import Schema

# from starlette_graphene3 import GraphQLApp, make_graphiql_handler
# # from starlette_graphene3 import GraphQLApp, make_playground_handler

# from app.db.database import prepare_database
# from app.gql.mutations import Mutation
# from app.gql.queries import Query

# schema = Schema(query=Query, mutation=Mutation)

# app = FastAPI()

# """
# This is deprecated!
# Will probably remove it and
# replace it with lifespan.
# """
# @app.on_event("startup")
# def startup_event():
#     prepare_database()
"""
We'll pass an endpoint that will return all resources of what the
GraphQL's returning.

This is so we'll have a simple REST endpoint.

"""
# @app.get("/{something}")
# def get_something():
#     with Session() as session:
#         return session.query(Employer).all()
#
#
# @app.get("/jobs")
# def get_jobs():
#     with Session() as session:
#         return session.query(Job).all()


# When deploying, you'll want it to be sent to /
#   app.mount(
#       "/",
#       GraphQLApp(
#           schema=schema,
#           on_get=make_graphiql_handler(),
#       ),
#   )

# This is for localhost testing
# app.mount(
#     "/graphql",
#     GraphQLApp(
#         schema=schema,
#         on_get=make_graphiql_handler(),
#     ),
# )
