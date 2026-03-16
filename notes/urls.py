from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("",views.home,name='home'),
    path("nvigate",views.nvigate,name="nvigate"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("login",views.login1,name="login"),
    path("admin",views.admin,name="admin"),
    path("signup/",views.signup1,name="signup"),
    path("admin_home",views.admin_home,name='admin_home'),
    path("logout",views.Logout,name="logout"),
    path("profile",views.profile,name="profile"),
    path("changepwd",views.changepwd,name="changepwd"),
    path('edit_pro',views.edit_pro,name='edit_pro'),
    path("upload_notes",views.uploadnotes,name='upload_notes'),
    path("view_notes",views.viewnotes,name="view_notes"),
    path("deletenotes/<int:pid>/",views.deletenotes,name="deletenotes"),
     path("deletenotes1/<int:pid>/",views.deletenotes1,name="deletenotes1"),
    path("view_user",views.viewuser,name="view_user"),
    path("delete_user/<int:uid>/",views.delete_user,name="delete_user"),
    path('pending',views.pending,name='pending'),
    path('assign_status/<int:id>/',views.assign,name="assign_status"),
    path('accept',views.accept_notes,name="accept"),
    path('reject',views.reject_notes,name='reject'),
    path('all_notes',views.all_notes,name="all_notes"),
    path('delete_notes/<int:id>/',views.delete_notes,name="delete_notes"),
    path('viewall_note',views.viewall_note,name="viewall_note")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

