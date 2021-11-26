from gateways.database.mock import MockDatabaseGateway
from gateways.database.airtable import AirtableDatabaseGateway


def database_gateway_factory(database: str = "mock"):
    if database == "mock":
        return MockDatabaseGateway()
    elif database == "airtable":
        return AirtableDatabaseGateway()
    else:
        raise NotImplementedError
