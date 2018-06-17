from django.conf.urls import include, url
from django.contrib.admin.views.decorators import staff_member_required
from . import views
from .registries import global_preferences_registry
from .forms import GlobalPreferenceForm

app_name = 'dynamic_preferences'

urlpatterns = [

    url(r'^global/$',
        staff_member_required(views.PreferenceFormView.as_view(
            registry=global_preferences_registry,
            form_class=GlobalPreferenceForm)),
        name="global"),
    url(r'^global/(?P<section>[\w\ ]+)$',
        staff_member_required(views.PreferenceFormView.as_view(
            registry=global_preferences_registry,
            form_class=GlobalPreferenceForm)),
        name="global.section"),

    url(r'^user/', include('dynamic_preferences.users.urls')),
]
