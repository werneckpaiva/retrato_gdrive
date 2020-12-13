# from django.conf import settings
# from django.views.generic import RedirectView
from django.urls import re_path, path, include
# from  import admin

urlpatterns = [
    path('', include('retrato.gdrive.album.urls')),
    # path('photo/', include('retrato.gdrive.photo.urls')),
]

# admin.autodiscover()
# urlpatterns += [
#     path('admin/', RedirectView.as_view(url='/admin/album', permanent=True)),
#     path('admin/album/', include('retrato.gdrive.admin.album.urls')),
#     path('admin/photo/', include('retrato.gdrive.admin.photo.urls'))
# ]