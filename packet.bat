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






echo Samsung DeX
%~dp0adb shell pm uninstall --user 0 com.sec.android.desktopmode.uiservice

echo Samsung Galaxy Friends
%~dp0adb shell pm uninstall --user 0 com.samsung.android.mateagent

echo Samsung Global Goals
%~dp0adb shell pm uninstall --user 0 com.samsung.sree

echo Samsung Health
%~dp0adb shell pm uninstall --user 0 com.sec.android.app.shealth

echo Samsung Internet
%~dp0adb shell pm uninstall --user 0 com.sec.android.app.sbrowser

echo Samsung Kids
%~dp0adb shell pm uninstall --user 0 com.sec.android.app.kidshome

echo Samsung Notes
%~dp0adb shell pm uninstall --user 0 com.samsung.android.app.notes

echo Samsung Pass
%~dp0adb shell pm uninstall --user 0 com.samsung.android.authfw

echo Samsung Pass Provider
%~dp0adb shell pm uninstall --user 0 com.samsung.android.samsungpass

echo Samsung Pay
%~dp0adb shell pm uninstall --user 0 com.samsung.android.spay

echo Secure Folder
%~dp0adb shell pm uninstall --user 0 com.samsung.knox.securefolder

echo SmartThings
%~dp0adb shell pm uninstall --user 0 com.samsung.android.beaconmanager
%~dp0adb shell pm uninstall --user 0 com.samsung.android.oneconnect

echo Smart Tutor
%~dp0adb shell pm uninstall --user 0 com.rsupport.rs.activity.rsupport.aas2

echo SwiftKey factory settings
%~dp0adb shell pm uninstall --user 0 com.touchtype.swiftkey
%~dp0adb shell pm uninstall --user 0 com.swiftkey.swiftkeyconfigurator

echo Wearable Manager Installer
%~dp0adb shell pm uninstall --user 0 com.samsung.android.app.watchmanagerstub

echo YouTube
%~dp0adb shell pm uninstall --user 0 com.google.android.youtube

echo YouTube Music
%~dp0adb shell pm uninstall --user 0 com.google.android.apps.youtube.music

echo Автозаполнение с Samsung Pass
%~dp0adb shell pm uninstall --user 0 com.samsung.android.samsungpassautofill

echo Включение голосом
%~dp0adb shell pm uninstall --user 0 com.samsung.android.bixby.wakeup

echo Главный экран Samsung DeX
%~dp0adb shell pm uninstall --user 0 com.sec.android.app.desktoplauncher

echo Google Диск
%~dp0adb shell pm uninstall --user 0 com.google.android.apps.docs

echo Диспетчер вашего телефона
%~dp0adb shell pm uninstall --user 0 com.microsoft.appmanager

echo Звукозапись
%~dp0adb shell pm uninstall --user 0 com.sec.android.app.voicenote

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