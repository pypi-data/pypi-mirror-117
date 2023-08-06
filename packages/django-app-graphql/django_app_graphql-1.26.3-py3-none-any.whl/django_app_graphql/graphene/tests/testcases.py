import abc

from django.test import LiveServerTestCase, TestCase
from graphene_file_upload.django.testing import GraphQLFileUploadTestMixin

from django_app_graphql.graphene.tests.AbstractGraphQLTestMixin import AbstractGraphQLTestMixin, RealGraphQLClientMixIn


class AbstractGraphQLTestCase(AbstractGraphQLTestMixin, RealGraphQLClientMixIn, TestCase, abc.ABC):
    """
    Graphql testclass to derive in order to test graphql
    """
    pass


class AbstractGraphQLLiveServerTestCase(AbstractGraphQLTestMixin, RealGraphQLClientMixIn, LiveServerTestCase, abc.ABC):
    pass