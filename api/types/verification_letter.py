from pydantic import BaseModel


class VerificationLetterParamsModel(BaseModel):
    email: str
    addressee: str
    include_salary: bool
    include_allowance: bool
