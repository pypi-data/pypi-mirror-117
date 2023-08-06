import abc

from django.test import LiveServerTestCase, TestCase
from graphene_file_upload.django.testing import GraphQLFileUploadTestMixin

from django_app_graphql.graphene.tests.AbstractGraphQLTestMixin import AbstractGraphQLTestMixin


class AbstractGraphQLTestCase(AbstractGraphQLTestMixin, TestCase, abc.ABC):
    """
    Graphql testclass to derive in order to test graphql
    """
    pass


class AbstractGraphQLLiveServerTestCase(AbstractGraphQLTestMixin, LiveServerTestCase, abc.ABC):
    pass