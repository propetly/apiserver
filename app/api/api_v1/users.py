from typing import Annotated

from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


from pydantic import BaseModel
from pydantic import ConfigDict


class UserRead(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    username: str
    phone: str


@router.get("", response_model=list[UserRead])
def get_users():
    return [
        {
            "id": 1,
            "username": "Chega",
            "phone": "+7 (999) 999 99 99",
        },
        {
            "id": 2,
            "username": "Tom",
            "phone": "+7 (888) 888 88 88",
        },
    ]
