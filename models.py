from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Profession(Base):
    __tablename__ = "professions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    resources = relationship("Resource", back_populates="profession")


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    profession_id = Column(Integer, ForeignKey("professions.id"))

    profession = relationship("Profession", back_populates="resources")
    recipe_entries = relationship("Recipe", back_populates="resource")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    recipe_entries = relationship("Recipe", back_populates="item")


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)

    item_id = Column(Integer, ForeignKey("items.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))

    quantity = Column(Integer)

    item = relationship("Item", back_populates="recipe_entries")
    resource = relationship("Resource", back_populates="recipe_entries")