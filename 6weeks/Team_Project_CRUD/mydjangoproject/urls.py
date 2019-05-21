from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blog.views
import imageview.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.index, name ='index'),
    path('blog/', include('blog.urls')),
    path('imageview/', imageview.views.imageview, name ="imageview"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
    
    path('post/<int:post_id>', blog.views.detail, name ='detail'),
    path('new/', blog.views.new, name = 'new'),
    path('create/', blog.views.create, name = 'create'),
    path('modify/<int:post_id>', blog.views.modify, name = 'modify'),
    path('update/<int:post_id>', blog.views.update, name = 'update'),
    path('delete/<int:post_id>', blog.views.delete, name = 'delete'),
    path('newpost/', blog.views.newpost, name = "newpost"),
'''