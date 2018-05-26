from csv import DictReader
from .repository import persist_entity
from .entity import EntityMDoc


def process_csv(file_path: str) -> None:
    for line in DictReader(open(file_path, "r")):
        entity = EntityMDoc()
        for k, v in line.items():
            entity.__setattr__(k, v)
        persist_entity(entity)
