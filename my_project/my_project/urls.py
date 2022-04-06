from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

from support.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/ticket/', TicketAPIList.as_view()),
    # path('api/v1/ticket/<int:pk>/', TicketAPIUpdate.as_view()),
    # path('api/v1/ticketdelete/<int:pk>/', TicketAPIDestroy.as_view()),
    path('api/v1/', include(router.urls)),
    # path('api/v1/auth/', include('djoser.urls')),  # new
    # re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
