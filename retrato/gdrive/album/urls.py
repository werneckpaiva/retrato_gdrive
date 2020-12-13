from django.urls import re_path


from retrato.gdrive.album.views import AlbumView

urlpatterns = [
    re_path(r'api/album/(?P<album_path>.*)$', AlbumView.as_view(), name='album_data'),
    # re_path(r'(?P<album_path>.*)$', GdriveAlbumHomeView.as_view(), name="album_home")
]
