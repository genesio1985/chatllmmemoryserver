from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/live")
def live():
    """
    Verifica se a API está ativa.
    """
    return {
        "status": "UP",
    }