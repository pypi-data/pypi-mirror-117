import abc

from django.test import LiveServerTestCase, TestCase
from graphene_file_upload.django.testing import GraphQLFileUploadTestMixin

from django_app_graphql.graphene.tests.AbstractGraphQLTestMixin import AbstractGraphQLTestMixin, RealGraphQLClientMixIn, \
    GrapheneClientTestMixIn


class AbstractGraphQLDjangoTestCase(AbstractGraphQLTestMixin, GrapheneClientTestMixIn, TestCase, abc.ABC):
    """
    Graphql testclass to derive in order to test graphql.
    We use django Client graphql implementation
    """

    def __init__(self):
        super().__init__()


class AbstractGraphQLDjangoLiveServerTestCase(AbstractGraphQLTestMixin, GrapheneClientTestMixIn, LiveServerTestCase, abc.ABC):
    """
    We use django live server to test. We use a fake graphql client to query the server
    """

    def __init__(self):
        super().__init__()


class AbstractGraphQLRealTestCase(AbstractGraphQLTestMixin, RealGraphQLClientMixIn, TestCase, abc.ABC):
    """
    Graphql testclass to derive in order to test graphql
    We use a real http connection to perform graphql queries
    """

    def __init__(self):
        super().__init__()


class AbstractGraphQLRealLiveServerTestCase(AbstractGraphQLTestMixin, RealGraphQLClientMixIn, LiveServerTestCase, abc.ABC):
    """
    We use django live server to test. We use a fake graphql client to query the server
    We use a real http connection to perform graphql queries
    """

    def __init__(self):
        super().__init__()
