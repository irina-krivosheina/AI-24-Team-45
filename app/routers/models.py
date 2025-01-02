from typing import Annotated
from loguru import logger
from fastapi import APIRouter, HTTPException, Depends
from app_utils.model_manager import ModelManager


router = APIRouter(tags=["models"], prefix="/models")


@router.post("/set_model")
async def set_model(model_name: Annotated[str, "Model name to set"], model_manager: ModelManager = Depends()):
    """Set the model for detection."""
    try:
        model_manager.set_model(model_name)
        return {"message": f"Model set to {model_name}"}
    except Exception as e:
        logger.error(f"Error setting model: {e}")
        raise HTTPException(status_code=400, detail="Invalid model path") from e


@router.get("/available")
async def get_available_models(model_manager: ModelManager = Depends()):
    """Get a list of available models."""
    try:
        return model_manager.get_available_models()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/current")
async def get_current_model(model_manager: ModelManager = Depends()):
    """Get the current model name."""
    return model_manager.get_current_model()
