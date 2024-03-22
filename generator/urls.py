from django.urls import path
from .api import (
    GameCreateAPI,
    GameGetAPI,
    GameGetInfoAPI,
    GameGetNamesAPI,
    GameDeleteAPI,
    GameUpdateAPI,
    GameUploadJsonAPI,
    GameUploadWordAPI,

    RoundCreateAPI,
    RoundUpdateAPI,
    RoundDeleteAPI,

    QuestionCreateAPI,
    QuestionGetOneAPI,
    QuestionGetAllAPI,
    QuestionUpdateAPI,
    QuestionDeleteAPI,
    QuestionSearchAPI,

    CategoryCreateAPI,
    CategoryGetAllAPI,
    CategoryGetAPI,
    CategoryGetKeysAPI,
    CategoryUpdateAPI,
    CategoryDeleteAPI,
    CategorySearchAPI,

    FileUploadAPI,
    SecondWayFileUploadAPI,
    upload_file,
    download_file
)


app_name = 'questgenerator'

urlpatterns = (

    # ------------------------------------
    # GAME
    # ------------------------------------

    # POST методы для Game
    path('api/v1/create-game/', GameCreateAPI.as_view()), # создать 1 игру

    # GET методы для Game
    path('api/v1/get-game/<int:pk>/', GameGetAPI.as_view()), # получить 1 игру с раундами, без вопросов
    path('api/v1/get-game-info/<int:pk>/', GameGetInfoAPI.as_view()), # получить 1 игру со всей информацией об игре
    path('api/v1/get-names-games/', GameGetNamesAPI.as_view()), # получить только имена всех игр

    # PATCH / PUT методы для Game
    path('api/v1/update-game/<int:pk>/', GameUpdateAPI.as_view()), # обновить / заменить 1 игру

    # DELETE методы для Game
    path('api/v1/delete-game/<int:pk>/', GameDeleteAPI.as_view()), # удалить 1 игру

    # API для выгрузки Game в json / word
    path('api/v1/download-game-to-json/<int:pk>/', GameUploadJsonAPI.as_view()), # выгрузить 1 игру в json
    path('api/v1/download-game-to-word/<int:pk>/', GameUploadWordAPI.as_view()), # выгрузить 1 игру в word


    # ------------------------------------
    # ROUND
    # ------------------------------------

    # POST методы для Round
    path('api/v1/create-round/', RoundCreateAPI.as_view()), # создать 1 раунд

    # PATH / PUT методы для Round
    path('api/v1/update-round/<int:pk>/', RoundUpdateAPI.as_view()), # обновить / заменить 1 раунд

    # DELETE методы для Round
    path('api/v1/delete-round/<int:pk>/', RoundDeleteAPI.as_view()), # удалить 1 раунд


    # ------------------------------------
    # QUESTION
    # ------------------------------------

    # POST методы для Question
    path('api/v1/create-question/', QuestionCreateAPI.as_view()), # создать 1 вопрос

    # # GET методы для Question
    path('api/v1/get-question/<int:pk>/', QuestionGetOneAPI.as_view()), # получить 1 вопрос со всей инфой
    path('api/v1/get-all-questions/', QuestionGetAllAPI.as_view()), # получить все вопросы, без ответов на вопросы
    path('api/v1/question-search/', QuestionSearchAPI.as_view()), # получить все вопросы, по указаным категориями

    # # PATCH / PUT методы для Question
    path('api/v1/update-question/<int:pk>/', QuestionUpdateAPI.as_view()), # обновить / заменить 1 вопрос

    # # DELETE для Question
    path('api/v1/delete-question/<int:pk>/', QuestionDeleteAPI.as_view()), # удалить вопрос


    # ------------------------------------
    # CATEGORY
    # ------------------------------------

    # POST методы для Category
    path('api/v1/create-category/', CategoryCreateAPI.as_view()), # создать 1 категорию

    # GET методы для категори
    path('api/v1/get-categories/', CategoryGetAllAPI.as_view()), # получить все категории
    path('api/v1/get-category/<int:pk>/', CategoryGetAPI.as_view()), # получить 1 категорию
    path('api/v1/categories/<str:ids>/', CategoryGetKeysAPI.as_view()), # получить только указаные категории
    path('api/v1/search-categories/', CategorySearchAPI.as_view()), # неполнотекстовый поиск категорий

    # PATCH / PUT методы для Category
    path('api/v1/update-category/<int:pk>/', CategoryUpdateAPI.as_view()), # обновить / заменить 1 категорию

    # # DELETE методы для Category
    path('api/v1/delete-category/<int:pk>/', CategoryDeleteAPI.as_view()), # удалить 1 категорию
    path('api/v1/upload-file/', FileUploadAPI.as_view()), # загрузить файл
    path('api/v1/upload-file2/', SecondWayFileUploadAPI.as_view()), # загрузить файл
    path('api/v1/upload/', upload_file, name='upload_file'),
    path('api/v1/download/', download_file, name='download_file')
)
