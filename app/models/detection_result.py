from pydantic import BaseModel, Field

class DetectionResult(BaseModel):
    xmin: float
    ymin: float
    xmax: float
    ymax: float
    confidence: float
    class_id: int = Field(..., alias='class')
    name: str