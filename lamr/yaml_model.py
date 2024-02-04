from pathlib import Path

from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from yaml import safe_load


@dataclass
class Reference:
    title: str
    url: str


class CodeMeta(BaseModel):
    questions: list[str] = []
    excercises: list[str] = []
    references: list[Reference] = []

    @classmethod
    def from_yaml(cls, path: str):
        dict_ = safe_load(Path(path).read_text())
        return cls.model_validate(dict_)
