from django.urls import path
from core.views import  (
    CheckListsAPIVIew,
    CheckListAPIView,
    CheckListItemCreateAPIView,
)

urlpatterns = [
    path('api/checklist/', CheckListsAPIVIew.as_view()),
    path('api/checklists/<int:pk>', CheckListAPIView.as_view()),
    path('api/checklistItem/create/', CheckListItemCreateAPIView.as_view()),
    path('api/checklistItem/<int:pk>/', CheckListItemCreateAPIView.as_view())
    


]