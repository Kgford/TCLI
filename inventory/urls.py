from django.urls import pathfrom . import viewsapp_name = "inventory"urlpatterns =[    path("", views.index, name="index"),    path("searchevents", views.searchevents, name ="searchevents"),	path("loadevent", views.loadevent, name ="loadevent"),	path("save_event", views.save_event, name ="save_event"),	path("items", views.items, name ="items"),	path("item", views.item, name ="item"),	path("search", views.search, name ="search"),	path("searchall", views.searchall, name ="searchall"),	path("upload_file", views.upload_file, name ="upload_file"),    ]