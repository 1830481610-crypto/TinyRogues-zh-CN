@echo off
echo ============================================
echo   Switch to ENGLISH MODE
echo   IMPORTANT: quit the game first!
echo ============================================
set "G=%~dp0"
set "BK=%G%BepInEx\_en_mode_backup"
if not exist "%BK%\Translation\zh\Text" mkdir "%BK%\Translation\zh\Text"
if not exist "%BK%\plugins\TinyRogues.TmpFallback" mkdir "%BK%\plugins\TinyRogues.TmpFallback"
move /Y "%G%BepInEx\Translation\zh\Text\TinyRogues_zh.txt" "%BK%\Translation\zh\Text\" >nul
move /Y "%G%BepInEx\Translation\zh\Text\RuntimeOverrides_zh.txt" "%BK%\Translation\zh\Text\" >nul
move /Y "%G%BepInEx\Translation\zh\Text\RuntimeRegex_zh.txt" "%BK%\Translation\zh\Text\" >nul
move /Y "%G%BepInEx\plugins\TinyRogues.TmpFallback\RuntimeRegex_zh.txt" "%BK%\plugins\TinyRogues.TmpFallback\" >nul
move /Y "%G%BepInEx\plugins\TinyRogues.TmpFallback\RuntimeFragments_zh.txt" "%BK%\plugins\TinyRogues.TmpFallback\" >nul
move /Y "%G%BepInEx\plugins\TinyRogues.TmpFallback\RuntimeItemFragments_zh.txt" "%BK%\plugins\TinyRogues.TmpFallback\" >nul
move /Y "%G%BepInEx\plugins\TinyRogues.TmpFallback\RuntimeDialogue_zh.txt" "%BK%\plugins\TinyRogues.TmpFallback\" >nul
echo.
echo Done. Game now shows ENGLISH text.
echo After checking, run "restore_cn.bat" to bring Chinese back.
pause
