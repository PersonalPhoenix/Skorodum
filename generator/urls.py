from django.urls import (
    path,
)

from .api import (
    GameCreateAPI,
    GameGetAPI,
    GameGetNamesAPI,
    GameDeleteAPI,
    GameUpdateAPI,
    GameUploadJsonAPI,
    GameUploadWordAPI,
    GameGetSelectedAPI,
    GameUploadZipAPI,
    RoundCreateAPI,
    RoundGetAPI,
    RoundUpdateAPI,
    RoundDeleteAPI,
    QuestionCreateAPI,
    QuestionGetOneAPI,
    QuestionGetAllAPI,
    QuestionUpdateAPI,
    QuestionDeleteAPI,
    QuestionSearchAPI,
    QuestionWordAPI,
    CategoryCreateAPI,
    CategoryGetAllAPI,
    CategoryGetAPI,
    CategoryGetKeysAPI,
    CategoryUpdateAPI,
    CategoryDeleteAPI,
    CategorySearchAPI,
    upload_file,
    download_file,
)


app_name = 'questgenerator'

urlpatterns = (
    path('api/v1/create-game/', GameCreateAPI.as_view()), # создать 1 игру
    path('api/v1/get-game/<int:pk>/', GameGetAPI.as_view()), # получить 1 игру с раундами, без вопросов
    path('api/v1/get-names-games/', GameGetNamesAPI.as_view()), # получить только имена всех игр
    path('api/v1/get-selected-games/<str:ids>/', GameGetSelectedAPI.as_view()), # получить выбранные игры
    path('api/v1/update-game/<int:pk>/', GameUpdateAPI.as_view()), # обновить / заменить 1 игру
    path('api/v1/delete-game/<int:pk>/', GameDeleteAPI.as_view()), # удалить 1 игру
    path('api/v1/download-game-to-json/<int:pk>/', GameUploadJsonAPI.as_view()), # выгрузить 1 игру в json
    path('api/v1/download-game-to-word/<int:pk>/', GameUploadWordAPI.as_view()), # выгрузить 1 игру в word
    path('api/v1/download-selected-games-to-zip/<str:ids>/', GameUploadZipAPI.as_view()), # получить выбранные игры в zip

    path('api/v1/create-round/', RoundCreateAPI.as_view()), # создать 1 раунд
    path('api/v1/get-round/<int:pk>/', RoundGetAPI.as_view()), # получить 1 раунд
    path('api/v1/update-round/<int:pk>/', RoundUpdateAPI.as_view()), # обновить / заменить 1 раунд
    path('api/v1/delete-round/<int:pk>/', RoundDeleteAPI.as_view()), # удалить 1 раунд

    path('api/v1/create-question/', QuestionCreateAPI.as_view()), # создать 1 вопрос
    path('api/v1/get-question/<int:pk>/', QuestionGetOneAPI.as_view()), # получить 1 вопрос со всей инфой
    path('api/v1/get-all-questions/', QuestionGetAllAPI.as_view()), # получить все вопросы, без ответов на вопросы
    path('api/v1/question-search/', QuestionSearchAPI.as_view()), # получить все вопросы, по указаным категориями
    path('api/v1/update-question/<int:pk>/', QuestionUpdateAPI.as_view()), # обновить / заменить 1 вопрос
    path('api/v1/delete-question/<int:pk>/', QuestionDeleteAPI.as_view()), # удалить вопрос
    path('api/v1/questions-in-word/', QuestionWordAPI.as_view()), # выгрузить вопросы в word
    path('api/v1/questions-in-word/<str:ids>/', QuestionWordAPI.as_view()), # выгрузить вопросы в word

    path('api/v1/create-category/', CategoryCreateAPI.as_view()), # создать 1 категорию
    path('api/v1/get-categories/', CategoryGetAllAPI.as_view()), # получить все категории
    path('api/v1/get-category/<int:pk>/', CategoryGetAPI.as_view()), # получить 1 категорию
    path('api/v1/categories/<str:ids>/', CategoryGetKeysAPI.as_view()), # получить только указаные категории
    path('api/v1/search-categories/', CategorySearchAPI.as_view()), # неполнотекстовый поиск категорий
    path('api/v1/update-category/<int:pk>/', CategoryUpdateAPI.as_view()), # обновить / заменить 1 категорию
    path('api/v1/delete-category/<int:pk>/', CategoryDeleteAPI.as_view()), # удалить 1 категорию

    path('api/v1/upload/', upload_file, name='upload_file'),
    path('api/v1/download/', download_file, name='download_file')
)
