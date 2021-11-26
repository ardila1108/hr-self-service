from gateways.database.base import DatabaseGateway


class MockDatabaseGateway(DatabaseGateway):
    def fetch_user_info(
        self, email: str, include_salary: bool, include_bonus: bool
    ):
        info_dict = {
            "name": "Carlos Andrés Ardila Palomino",
            "id_number": "1020798773",
            "id_city": "Bogotá",
            "start_date": "2021-06-01",
            "position": "Machine Learning Engineer III",
            "salary": None,
            "bonus": None,
        }

        if include_salary:
            info_dict["salary"] = 1234567

        if include_bonus:
            info_dict["bonus"] = 123456
        return info_dict
