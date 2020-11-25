from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView



from bars.views import (
	index,
	show_address_on_map
)


urlpatterns = [
	path("admin/", admin.site.urls),
	path("", index),
	path("map/", show_address_on_map, name='map'),
	path('sw.js', (TemplateView.as_view(template_name="sw.js", content_type='application/javascript', )), name='sw.js'),
	path('', include('pwa.urls'))
]

