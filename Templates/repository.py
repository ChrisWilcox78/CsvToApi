from typing import List, Optional, Dict
from bson.objectid import ObjectId

from Helpers.decorators import db_connect, treat_not_found_as_none
from .entity import EntityMDoc


@db_connect
def retrieve_all() -> List[EntityMDoc]:
    return EntityMDoc.objects.to_json()  # pylint: disable=no-member


@db_connect
def search(restriction_dictionary: Dict[str, str]) -> List[EntityMDoc]:
    return EntityMDoc.objects(__raw__=restriction_dictionary).to_json()  # pylint: disable=no-member


@db_connect
@treat_not_found_as_none
def get_entity(id: str) -> Optional[EntityMDoc]:
    return EntityMDoc.objects.get(id=ObjectId(id)).to_json()  # pylint: disable=no-member


@db_connect
def persist_entity(entity: EntityMDoc) -> None:
    entity.save()
