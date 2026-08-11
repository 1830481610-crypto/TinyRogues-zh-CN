@echo off
echo ============================================
echo   Restore CHINESE MODE
echo   IMPORTANT: quit the game first!
echo ============================================
set "G=%~dp0"
set "BK=%G%BepInEx\_en_mode_backup"
move /Y "%BK%\Translation\zh\Text\TinyRogues_zh.txt" "%G%BepInEx\Translation\zh\Text\" >nul
move /Y "%BK%\Translation\zh\Text\RuntimeOverrides_zh.txt" "%G%BepInEx\Translation\zh\Text\" >nul
move /Y "%BK%\Translation\zh\Text\RuntimeRegex_zh.txt" "%G%BepInEx\Translation\zh\Text\" >nul
move /Y "%BK%\plugins\TinyRogues.TmpFallback\RuntimeRegex_zh.txt" "%G%BepInEx\plugins\TinyRogues.TmpFallback\" >nul
move /Y "%BK%\plugins\TinyRogues.TmpFallback\RuntimeFragments_zh.txt" "%G%BepInEx\plugins\TinyRogues.TmpFallback\" >nul
move /Y "%BK%\plugins\TinyRogues.TmpFallback\RuntimeItemFragments_zh.txt" "%G%BepInEx\plugins\TinyRogues.TmpFallback\" >nul
move /Y "%BK%\plugins\TinyRogues.TmpFallback\RuntimeDialogue_zh.txt" "%G%BepInEx\plugins\TinyRogues.TmpFallback\" >nul
echo.
echo Done. Chinese restored.
pause
