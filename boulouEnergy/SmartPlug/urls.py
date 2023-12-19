from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import (
        SwitchOn,
        SwitchOff,
        CheckStatus,
        GetStatistics,
        CustomPower,
        TimerCountDown,
        TimerCountDown,
        TimerSchedule,
        Home,
        Login,
        Login,
        Inventaire,
        Control,
        UserManagement,
        UserSettings,
        OverLoad,
        SendSMS,
    )


urlpatterns = [
    path('switch-ON', SwitchOn.as_view()),
    path('switch-OFF', SwitchOff.as_view()),
    path('send-sms', SendSMS.as_view()),
    path('overload', OverLoad.as_view()),
    path('checkStatus', CheckStatus.as_view()),
    path('getStatistics', GetStatistics.as_view()),
    path('customPower', CustomPower.as_view()),
    path('timerCountDown', TimerCountDown.as_view()),
    path('timerSchedule', TimerSchedule.as_view()),
    path('home/', Home.as_view()),
    path('login/', Login.as_view()),
    path('inventaire/', Inventaire.as_view()),
    path('control/', Control.as_view()),
    path('user-management/', UserManagement.as_view()),
    path('user-settings/', UserSettings.as_view())
]

