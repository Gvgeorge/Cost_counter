from fastapi import APIRouter, Depends, Response, status
from models.operations import Operation, OperationCreate, OperationKind, \
    OperationUpdate
from typing import List, Optional
from services.operations import OperationsService
from services.auth import get_current_user
from models.auth import User


router = APIRouter(
    prefix='/operations',
    tags=['operations']
)


@router.get('/', response_model=List[Operation])
def get_operations(
    kind: Optional[OperationKind] = None,
    service: OperationsService = Depends(),
    user: User = Depends(get_current_user)
):
    return service.get_list(user.id, kind=kind)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(
    operation_id: int,
    service: OperationsService = Depends(),
    user: User = Depends(get_current_user)
):
    return service.get(user.id, operation_id)


@router.post('/', response_model=Operation)
def add_operation(
    operation_data: OperationCreate,
    service: OperationsService = Depends(),
    user: User = Depends(get_current_user)
):
    return service.create(user.id, operation_data)


@router.put('/{operation_id}', response_model=Operation)
def update_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    service: OperationsService = Depends(),
    user: User = Depends(get_current_user)
):
    return service.update(user.id, operation_id, operation_data)


@router.delete('/{operation_id}')
def delete_operation(
    operation_id: int,
    service: OperationsService = Depends(),
    user: User = Depends(get_current_user)
):
    service.delete(user.id, operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
