from pydantic import BaseModel, ConfigDict
from typing import List


class ProfessionBase(BaseModel):
    name: str


class ProfessionCreate(ProfessionBase):
    pass


class Profession(ProfessionBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ResourceBase(BaseModel):
    name: str
    profession_id: int


class ResourceCreate(ResourceBase):
    pass


class Resource(ResourceBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class RecipeBase(BaseModel):
    item_id: int
    resource_id: int
    quantity: int


class RecipeCreate(RecipeBase):
    pass


class Recipe(RecipeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ItemBase(BaseModel):
    name: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class RecipeIngredient(BaseModel):
    resource: Resource
    quantity: int
    model_config = ConfigDict(from_attributes=True)


class ItemWithRecipe(Item):
    recipe_entries: List[RecipeIngredient] = []
    model_config = ConfigDict(from_attributes=True)