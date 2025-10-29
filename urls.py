from django.urls import path
from . import views

urlpatterns = [
    path('api/screen_time_by_age/', views.screen_time_by_age, name='screen_time_by_age'),
    path('api/screen_time_summary/', views.ScreenTimeSummaryView.as_view(), name='screen_time_summary'),
    path('screen-timing-page/', views.screen_timing_page, name='screen_timing_page'),
    path('screen-summary-page/', views.screen_summary_page, name='screen_summary_page'),
    path('api/health_impact/', views.health_impact_data, name='health_impact_data'),
    path('health-impact-page/', views.health_impact_page, name='health_impact_page'),
]
