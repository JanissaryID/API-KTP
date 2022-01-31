from typing import Optional
from pydantic import BaseModel


class KtpBase(BaseModel):
    nik: str
    status: bool


class KtpAdd(KtpBase):
    name: str
    # streaming_platform: Optional[str] = None
    # membership_required: bool

    class Config:
        orm_mode = True


class KTP(KtpAdd):
    nik: str

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class UpdateKtp(BaseModel):
    status: bool
    # Optional[str] is just a shorthand or alias for Union[str, None].
    # It exists mostly as a convenience to help function signatures look a little cleaner.
    # streaming_platform: Optional[str] = None
    # membership_required: bool

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True