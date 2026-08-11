@echo off
echo ============================================
echo   HOT restore CHINESE (no restart needed)
echo ============================================
set "G=%~dp0"
set "BK=%G%BepInEx\_en_mode_backup"
move /Y "%BK%\Translation\zh\Text\TinyRogues_zh.txt" "%G%BepInEx\Translation\zh\Text\" >nul 2>&1
move /Y "%BK%\Translation\zh\Text\RuntimeOverrides_zh.txt" "%G%BepInEx\Translation\zh\Text\" >nul 2>&1
move /Y "%BK%\Translation\zh\Text\RuntimeRegex_zh.txt" "%G%BepInEx\Translation\zh\Text\" >nul 2>&1
move /Y "%BK%\plugins\TinyRogues.TmpFallback\RuntimeRegex_zh.txt" "%G%BepInEx\plugins\TinyRogues.TmpFallback\" >nul 2>&1
move /Y "%BK%\plugins\TinyRogues.TmpFallback\RuntimeFragments_zh.txt" "%G%BepInEx\plugins\TinyRogues.TmpFallback\" >nul 2>&1
move /Y "%BK%\plugins\TinyRogues.TmpFallback\RuntimeItemFragments_zh.txt" "%G%BepInEx\plugins\TinyRogues.TmpFallback\" >nul 2>&1
move /Y "%BK%\plugins\TinyRogues.TmpFallback\RuntimeDialogue_zh.txt" "%G%BepInEx\plugins\TinyRogues.TmpFallback\" >nul 2>&1
echo.
echo Done. Chinese restored in ~1s.
pause
