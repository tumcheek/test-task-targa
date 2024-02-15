from typing import List, Union

from pydantic import BaseModel, EmailStr


class DirectoryInfo(BaseModel):
    files: List[List[Union[str, dict]]]
    directories: List[List[Union[str, dict]]]
    path: str


class FileInfo(BaseModel):
    name: str
    content: str
    path: str


class DirectoryCreation(BaseModel):
    name: str


class FileCreation(BaseModel):
    name: str
    content: str


class FileUpdate(BaseModel):
    content: str

