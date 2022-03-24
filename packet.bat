@echo off
chcp 65001 >nul

:top
cls
echo.
echo Uninstall One UI apps?
echo.
set /p input="Type "amen" to proceed> "
if /i "%input%"=="amen" goto :amen
goto :top

:amen

echo Карты
%~dp0adb shell pm uninstall --user 0 com.google.android.apps.maps

echo Каталог живых обоев
%~dp0adb shell pm uninstall --user 0 com.android.wallpaper.livepicker

echo Клавиатура Microsoft SwiftKey
%~dp0adb shell pm uninstall --user 0 com.touchtype.swiftkey

echo Клавиатура Samsung
%~dp0adb shell pm uninstall --user 0 com.samsung.android.honeyboard

echo Люди
%~dp0adb shell pm uninstall --user 0 com.samsung.android.service.peoplestripe

echo Мои файлы
%~dp0adb shell pm uninstall --user 0 com.sec.android.app.myfiles

echo Напоминания
%~dp0adb shell pm uninstall --user 0 com.samsung.android.app.reminder

echo Погода
%~dp0adb shell pm uninstall --user 0 com.sec.android.daemonapp

echo Прямая расшифровка
%~dp0adb shell pm uninstall --user 0 com.google.audio.hearing.visualization.accessibility.scribe

echo Редактор AR-эмодзи
%~dp0adb shell pm uninstall --user 0 com.samsung.android.aremojieditor

echo Руководство пользователя
%~dp0adb shell pm uninstall --user 0 com.sec.android.widgetapp.webmanual

echo SIM-карта
%~dp0adb shell pm uninstall --user 0 com.android.stk

echo Служба Bixby
%~dp0adb shell pm uninstall --user 0 com.samsung.android.bixby.service

echo Советы
%~dp0adb shell pm uninstall --user 0 com.samsung.android.app.tips

echo Стикеры AR Emoji
%~dp0adb shell pm uninstall --user 0 com.sec.android.mimage.avatarstickers

echo Сценарии Bixby
%~dp0adb shell pm uninstall --user 0 com.samsung.android.app.routines

echo Установщик Kids
%~dp0adb shell pm uninstall --user 0 com.samsung.android.kidsinstaller

echo Яндекс
%~dp0adb shell pm uninstall --user 0 ru.yandex.searchplugin

%~dp0adb kill-server
echo.

taskkill /F /IM adb.exe

RMDIR /S /Q %USERPROFILE%\.android
RMDIR /S /Q %USERPROFILE%\.dbus-keyrings
pause