from typing import Dict

from fastapi import FastAPI, status
from pydantic import BaseModel


class Food(BaseModel):
    """Model from Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


app = FastAPI()
foods: Dict[int, Food] = {}


# write the Create endpoint

@app.post("/", status_code=status.HTTP_201_CREATED)
async def create_food(item: Food) -> Food:
    foods[item.id] = item
    return item
