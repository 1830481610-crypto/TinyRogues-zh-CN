@echo off
echo ============================================
echo   HOT switch to ENGLISH (no restart needed)
echo   Plugin hot-reloads dicts within ~1s.
echo ============================================
set "G=%~dp0"
set "BK=%G%BepInEx\_en_mode_backup"
if not exist "%BK%\Translation\zh\Text" mkdir "%BK%\Translation\zh\Text"
if not exist "%BK%\plugins\TinyRogues.TmpFallback" mkdir "%BK%\plugins\TinyRogues.TmpFallback"
move /Y "%G%BepInEx\Translation\zh\Text\TinyRogues_zh.txt" "%BK%\Translation\zh\Text\" >nul 2>&1
move /Y "%G%BepInEx\Translation\zh\Text\RuntimeOverrides_zh.txt" "%BK%\Translation\zh\Text\" >nul 2>&1
move /Y "%G%BepInEx\Translation\zh\Text\RuntimeRegex_zh.txt" "%BK%\Translation\zh\Text\" >nul 2>&1
move /Y "%G%BepInEx\plugins\TinyRogues.TmpFallback\RuntimeRegex_zh.txt" "%BK%\plugins\TinyRogues.TmpFallback\" >nul 2>&1
move /Y "%G%BepInEx\plugins\TinyRogues.TmpFallback\RuntimeFragments_zh.txt" "%BK%\plugins\TinyRogues.TmpFallback\" >nul 2>&1
move /Y "%G%BepInEx\plugins\TinyRogues.TmpFallback\RuntimeItemFragments_zh.txt" "%BK%\plugins\TinyRogues.TmpFallback\" >nul 2>&1
move /Y "%G%BepInEx\plugins\TinyRogues.TmpFallback\RuntimeDialogue_zh.txt" "%BK%\plugins\TinyRogues.TmpFallback\" >nul 2>&1
echo.
echo Done. Game now ENGLISH in ~1s.
echo Re-hover items to see English text.
echo Switch back with restore_cn_hot.bat
pause
