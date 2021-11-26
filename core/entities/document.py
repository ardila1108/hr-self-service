from abc import ABC, abstractmethod

from gateways.database.factory import database_gateway_factory


class Document(ABC):

    database = database_gateway_factory("airtable")

    @abstractmethod
    def render(self):
        pass
