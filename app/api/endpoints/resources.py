from typing import List, Any

from fastapi import APIRouter

from app import schemas

router = APIRouter()


@router.get("/",response_model=List[schemas.TestResourceNoneInteraction]
)
def get_resources(
        skip: int = 0,
        limit: int = 20,
) -> Any:
    return [schemas.testResourceNoneInteraction]


@router.get("/test",response_model=List[schemas.TestResourceInteraction])
def get_tests(
        skip: int = 0,
        limit: int = 20,
) -> Any:
    return [schemas.testResourceInteraction]

