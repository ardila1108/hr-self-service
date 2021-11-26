from pyairtable import Table
from pyairtable.formulas import match

from gateways.database.base import DatabaseGateway
from config.settings import Settings


class AirtableDatabaseGateway(DatabaseGateway):
    def fetch_user_info(
        self, email: str, include_salary: bool, include_allowance: bool
    ) -> dict:
        table = Table("keymBysXazFI5MhUp", Settings.AIRTABLE_BASE, Settings.AIRTABLE_TABLE)
        filter_formula = match({"Factored E-mail": email})
        user_record = table.all(formula=filter_formula)

        if len(user_record) == 0:
            raise ValueError(
                "Could not retrieve information for employee: " + email
            )

        elif len(user_record) > 1:
            raise ValueError(
                "There is more than one record associated to employee: " + email
            )

        return self._parse_user_record(user_record, include_salary, include_allowance)

    @staticmethod
    def _parse_user_record(user_record, include_salary, include_allowance):
        user_fields = user_record[0]["fields"]
        table_fields = [
            "Name",
            "ID",
            "ID number",
            "ID Expedition Place",
            "Job Title",
            "Start Date",
        ]
        fields = [
            "name",
            "id_type",
            "id_number",
            "id_city",
            "position",
            "start_date",
        ]

        if include_salary:
            table_fields.append("Salary compensation")
            fields.append("salary")

        if include_allowance:
            table_fields.append("Non-salary compensation")
            fields.append("allowance")

        return {f: user_fields.get(t, None) for t, f in zip(table_fields, fields)}
