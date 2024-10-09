from fastapi import APIRouter, HTTPException
from app.schemas import SuspectModel
from app.crud import get_all_suspects, get_suspect_by_id, format_suspect

suspect_router = APIRouter()


@suspect_router.get("/", response_model=list[SuspectModel])
def fetch_all_suspects():
    suspects = get_all_suspects()
    return [format_suspect(suspect) for suspect in suspects]


@suspect_router.get("/{suspect_id}", response_model=SuspectModel)
def fetch_suspect_by_id(suspect_id: str):
    suspect = get_suspect_by_id(suspect_id)
    if not suspect:
        raise HTTPException(status_code=404, detail="Suspect not found")
    return format_suspect(suspect)