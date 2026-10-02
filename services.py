from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas


def create_profession(db: Session, profession: schemas.ProfessionCreate):
    db_prof = models.Profession(name=profession.name)
    db.add(db_prof)
    db.commit()
    db.refresh(db_prof)
    return db_prof


def create_resource(db: Session, resource: schemas.ResourceCreate):
    db_res = models.Resource(name=resource.name, profession_id=resource.profession_id)
    db.add(db_res)
    db.commit()
    db.refresh(db_res)
    return db_res


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(
        item_id=recipe.item_id,
        resource_id=recipe.resource_id,
        quantity=recipe.quantity
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def calculate_crafting_cost(db: Session, item_id: int, target_quantity: int):
    """
    Calculate the resources required to craft a specified quantity of an item.
    """

    item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found in database")

    result = {
        "item_name": item.name,
        "target_quantity": target_quantity,
        "materials_needed": []
    }

    for entry in item.recipe_entries:
        total_needed = entry.quantity * target_quantity

        result["materials_needed"].append({
            "resource_name": entry.resource.name,
            "profession_needed": entry.resource.profession.name,
            "base_quantity": entry.quantity,
            "total_quantity": total_needed
        })

    return result