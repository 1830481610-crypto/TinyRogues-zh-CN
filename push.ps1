$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Tiny Rogues 汉化补丁 - 一键推送 GitHub" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan

# 1. stage all changes
git add -A
if ($LASTEXITCODE -ne 0) { Write-Host "git add 失败！" -ForegroundColor Red; exit 1 }

# 2. check if anything changed
$staged = git diff --cached --name-only
if (-not $staged) {
    Write-Host "没有检测到改动，无需提交推送。" -ForegroundColor Yellow
    exit 0
}
Write-Host ("检测到 {0} 个文件变更：" -f $staged.Count) -ForegroundColor Green
$staged | ForEach-Object { Write-Host ("  - " + $_) -ForegroundColor Gray }

# 3. commit
$msg = "补丁更新 " + (Get-Date -Format "yyyy-MM-dd HH:mm")
git commit -m $msg
if ($LASTEXITCODE -ne 0) { Write-Host "git commit 失败！" -ForegroundColor Red; exit 1 }

# 4. push
git push
if ($LASTEXITCODE -ne 0) { Write-Host "git push 失败！请检查网络或 GitHub 登录。" -ForegroundColor Red; exit 1 }

Write-Host ""
Write-Host "推送成功！" -ForegroundColor Green