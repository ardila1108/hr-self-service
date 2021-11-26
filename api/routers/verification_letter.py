from fastapi import APIRouter
from core.entities import VerificationLetter
from api.types import VerificationLetterParamsModel

router = APIRouter()


@router.post("/verification")
async def get_verification_letter(param_dict: VerificationLetterParamsModel):
    document_entity = VerificationLetter(**param_dict.dict())
    file = document_entity.render()
    return {"file": file}
