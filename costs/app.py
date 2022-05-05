from fastapi import FastAPI
from api import router

tags_metadata = [
    {'name': 'auth',
     'description': 'Авторизация и регистрация'},
    {'name': 'operations',
     'description': 'Операции'},
    {'name': 'reports',
     'description': 'Импорт и экспорт csv отчетов'}
]

app = FastAPI(
    title='CostCounter',
    description='Сервис учета расходов и доходов',
    version='1.0.0',
    openapi_tags=tags_metadata)

app.include_router(router)

