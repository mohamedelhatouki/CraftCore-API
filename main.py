from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, services
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Economy & Crafting API", 
    description="RPG Economy resource and crafting management system"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/professions/", response_model=schemas.Profession)
def create_profession(profession: schemas.ProfessionCreate, db: Session = Depends(get_db)):
    return services.create_profession(db, profession)

@app.post("/api/resources/", response_model=schemas.Resource)
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return services.create_resource(db, resource)

@app.post("/api/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return services.create_item(db, item)

@app.post("/api/recipes/", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return services.create_recipe(db, recipe)


@app.get("/api/items/{item_id}", response_model=schemas.ItemWithRecipe)
def get_item_with_recipe(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.get("/api/items/{item_id}/calculate-cost")
def calculate_item_cost(item_id: int, quantity: int = 1, db: Session = Depends(get_db)):
    """
    Calculate crafting requirements for a specific item quantity.
    - item_id: item identifier
    - quantity: requested quantity (default 1)
    """
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than zero")

    return services.calculate_crafting_cost(db, item_id, quantity)