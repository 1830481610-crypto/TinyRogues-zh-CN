param(
    [string]$Version = "",
    [switch]$DryRun = $false,
    [switch]$SkipPush = $false
)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$REPO = "1830481610-crypto/TinyRogues-zh-CN"

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Tiny Rogues 汉化补丁 - 发布新版本 (Release)" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan

# ---------- 0. 检查 gh 登录 ----------
if (-not $DryRun) {
    gh auth status 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) { Write-Host "gh 未登录，请先 gh auth login" -ForegroundColor Red; exit 1 }
}

# ---------- 1. 提交并推送未提交改动 ----------
Write-Host "`n[1/6] 检查并提交未推送的改动..." -ForegroundColor Yellow
git add -A
$staged = git diff --cached --name-only
if ($staged) {
    $msg = "补丁更新 " + (Get-Date -Format "yyyy-MM-dd HH:mm")
    git commit -m $msg
    if (-not $SkipPush) { git push }
    Write-Host ("已提交 " + $staged.Count + " 个文件") -ForegroundColor Green
} else {
    Write-Host "没有未提交的改动" -ForegroundColor Gray
}
if (-not $SkipPush) { git push 2>&1 | Out-Null }

# ---------- 2. 确定版本号 ----------
Write-Host "`n[2/6] 确定版本号..." -ForegroundColor Yellow
if ($Version -eq "") {
    # auto increment from latest tag
    git fetch --tags origin 2>&1 | Out-Null
    $lastTag = git describe --tags --abbrev=0 2>$null
    if ($lastTag -and $lastTag -match '^v?(\d+)\.(\d+)\.(\d+)$') {
        $maj=[int]$Matches[1]; $min=[int]$Matches[2]; $pat=[int]$Matches[3]
        $Version = "v$maj.$min.$($pat+1)"
    } else {
        $Version = "v1.0.0"
    }
    Write-Host ("自动版本号: " + $Version) -ForegroundColor Green
} else {
    if ($Version -notmatch '^v?') { $Version = "v" + $Version }
    Write-Host ("指定版本号: " + $Version) -ForegroundColor Green
}

# ---------- 3. 打 tag ----------
Write-Host "`n[3/6] 打 tag $Version ..." -ForegroundColor Yellow
if (-not $DryRun) {
    git tag -a $Version -m "Tiny Rogues 汉化补丁 $Version"
    if ($LASTEXITCODE -ne 0) { Write-Host "tag 已存在或创建失败" -ForegroundColor Red; exit 1 }
    git push origin $Version 2>&1 | Out-Null
    Write-Host ("tag $Version 已推送") -ForegroundColor Green
} else {
    Write-Host ("[DryRun] 将创建 tag: " + $Version) -ForegroundColor Gray
}

# ---------- 4. 打包补丁 zip ----------
Write-Host "`n[4/6] 打包补丁文件..." -ForegroundColor Yellow
$staging = Join-Path $env:TEMP ("tinyrogues_rel_" + $Version.Replace('.','_') + "_" + [guid]::NewGuid().ToString("N").Substring(0,6))
$outZip  = Join-Path $PSScriptRoot ("TinyRogues_汉化补丁_" + $Version + ".zip")
New-Item -ItemType Directory -Path $staging -Force | Out-Null
try {
    # copy patch items (reference v1.0 纯翻译发布包 structure)
    $items = @('BepInEx','dotnet','.doorstop_version','doorstop_config.ini','winhttp.dll','SourceHanSans_U2022','switch_en.bat','switch_en_hot.bat','restore_cn.bat','restore_cn_hot.bat')
    foreach($it in $items){
        $src = Join-Path $PSScriptRoot $it
        if(Test-Path $src){ Copy-Item -Path $src -Destination $staging -Recurse -Force }
    }
    # remove runtime-generated / diagnostic stuff inside BepInEx
    $bep = Join-Path $staging 'BepInEx'
    foreach($drop in @('cache','interop','_en_mode_backup','ErrorLog.log','LogOutput.log')){
        $d = Join-Path $bep $drop
        if(Test-Path $d){ Remove-Item $d -Recurse -Force }
    }
    # remove _Tmp* capture files and .bak* backups
    Get-ChildItem $bep -Recurse -Force -ErrorAction SilentlyContinue | Where-Object {
        $_.Name -like '_Tmp*' -or $_.Name -like '*.bak*'
    } | ForEach-Object { Remove-Item $_.FullName -Force -Recurse -ErrorAction SilentlyContinue }
    # write 安装说明.txt
    $readme = @"
Tiny Rogues 简体中文汉化补丁 $Version
====================================
安装：将本压缩包内全部文件覆盖到 Tiny Rogues.exe 所在目录。
卸载：删除 BepInEx、dotnet、winhttp.dll、doorstop_config.ini、.doorstop_version、SourceHanSans_U2022。
说明：本包为纯翻译补丁，含 BepInEx 框架 + 词典 + 中文字体 + 热切换脚本。
恢复旧版：在 GitHub Releases 页面下载任意历史版本覆盖即可。
"@
    [System.IO.File]::WriteAllText((Join-Path $staging '安装说明.txt'), $readme, (New-Object System.Text.UTF8Encoding($false)))
    # compress
    if(Test-Path $outZip){ Remove-Item $outZip -Force }
    Compress-Archive -Path (Join-Path $staging '*') -DestinationPath $outZip -CompressionLevel Optimal
    $sizeMB = [math]::Round((Get-Item $outZip).Length/1MB,1)
    Write-Host ("打包完成: " + $outZip + "  (" + $sizeMB + " MB)") -ForegroundColor Green
} finally {
    Remove-Item $staging -Recurse -Force -ErrorAction SilentlyContinue
}

# ---------- 5. 创建 Release ----------
Write-Host "`n[5/6] 创建 GitHub Release..." -ForegroundColor Yellow
if (-not $DryRun) {
    $notes = "Tiny Rogues 简体中文汉化补丁 $Version`n`n- 自动打包自游戏目录当前补丁文件`n- 包含: BepInEx 框架 + 全部词典 + dotnet 运行时 + 中文字体 + 热切换脚本`n- 下载后覆盖到游戏根目录即可"
    gh release create $Version $outZip --repo $REPO --title "Tiny Rogues 汉化补丁 $Version" --notes $notes
    if ($LASTEXITCODE -ne 0) { Write-Host "Release 创建失败" -ForegroundColor Red; exit 1 }
    Write-Host ("Release $Version 已发布") -ForegroundColor Green
} else {
    Write-Host ("[DryRun] 将创建 Release: " + $Version + "  附件: " + (Split-Path $outZip -Leaf)) -ForegroundColor Gray
}

# ---------- 6. 清理 ----------
Write-Host "`n[6/6] 完成"
if (-not $DryRun) {
    Write-Host "提示: 本地 zip 保留在游戏目录，可自行删除；GitHub Release 已保存。" -ForegroundColor Gray
} else {
    Write-Host "DryRun 结束，未创建 tag/Release。zip 已生成用于检查。" -ForegroundColor Gray
}