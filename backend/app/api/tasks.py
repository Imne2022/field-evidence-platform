from fastapi import APIRouter, Depends, HTTPException, Query, status as http_status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.task import EvidenceTask

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("")
def list_tasks(
    status: str = Query("open", description="Filter tasks by status"),
    db: Session = Depends(get_db),
):
    return (
        db.query(EvidenceTask)
        .filter(EvidenceTask.status == status)
        .all()
    )


@router.post("/{task_id}/accept")
def accept_task(
    task_id: int,
    partner_id: int,
    db: Session = Depends(get_db),
):
    task = db.get(EvidenceTask, task_id)
    if not task or task.status != "open":
        raise HTTPException(
            status_code=http_status.HTTP_409_CONFLICT,
            detail=f"Task {task_id} not available",
        )

    task.status = "assigned"
    task.assigned_partner_id = partner_id
    db.commit()
    db.refresh(task)

    return {"task_id": task.id, "status": task.status}