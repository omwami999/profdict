class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
