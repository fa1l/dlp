from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.responses import JSONResponse
from independency import Container
from celery_worker.task import LeakFinderTask

from dependencies.container import create_container
from leak_finder.regexp import RegexpLeakFinder
from models.leakage import Leakage
from storage.in_memory_storage import InMemoryLeakStorage


router = APIRouter()


@router.post("/check_for_leaks")
def check_for_leaks(
    payload: str, deps_container: Annotated[Container, Depends(create_container)]
):
    task = LeakFinderTask(deps_container.resolve(RegexpLeakFinder)).apply_async(
        [payload]
    )
    result = task.get()
    if result is not None:
        storage = deps_container.resolve(InMemoryLeakStorage)
        for data in result:
            leakage = Leakage.model_validate_json(data)
            storage.save_leakage_info(leakage)
    return JSONResponse({"leaks": result})


@router.get("/get_all_leaks")
def get_all_leaks(deps_container: Annotated[Container, Depends(create_container)]):
    storage = deps_container.resolve(InMemoryLeakStorage)
    result = [leak.model_dump_json() for leak in storage.get_all_leakeges()]
    return JSONResponse({"leaks": result})
