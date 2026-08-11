# Tiny Rogues 简体中文汉化补丁 v1.5.26

基于社区汉化补丁 `TinyRogues_zh_CN_v1.5.25` 补全制作。

## 补全内容

- 主字典 `TinyRogues_zh.txt` 由 **5948 → 7771 条** 翻译条目。
- 利用游戏 wiki 中文注释（武器 / 装备 / 道具 / 符咒 / 技能 / 同伴 / 特性 / 状态 / 角色 等 13 个表，共 1777 条权威「英文名→中文名」）批量补全了全部物品 / 实体名称。
- 结合游戏运行日志 `_TmpUntranslated.txt`，补齐了原补丁缺失的 **职业名（枪手 / 吟游诗人 / 强盗 / 浪人…）、Boss 名、关卡名、装备名、头衔、精英附魔、物品描述、店主对话、异常提示** 等真实出现的 UI 文本。
- 运行日志中 **194 条真实缺失串已解决约 100%**（剩余为游戏自带调试文本 `SOMETHING` / `asdasd`、怪物拟声词、平台品牌 `Steam Deck`、以及文本输入框的逐字输入中间态，均无需翻译）。

## 安装方法

1. 关闭游戏。
2. 将本文件夹内的 **所有内容**（`BepInEx/`、`dotnet/`、`winhttp.dll`、`doorstop_config.ini`、`arialuni_sdf_u2019`、`changelog.txt` 等）**复制并覆盖**到游戏根目录，即 `steamapps/common/Tiny Rogues/`。
3. 正常启动游戏即可。首次加载会生成汉化缓存，之后所有界面、物品、技能、描述均为中文。

> 若游戏目录之前已装过旧版汉化，直接覆盖即可；本补丁已包含完整的 BepInEx + XUnity.AutoTranslator 框架，无需额外安装。

## 目录说明

- `BepInEx/Translation/zh/Text/TinyRogues_zh.txt` —— 主翻译字典（核心文件）。
- `BepInEx/plugins/XUnity.AutoTranslator/` —— 自动翻译框架。
- `BepInEx/plugins/TinyRogues.TmpFallback/` —— 运行时兜底层（对个别动态串做保底翻译）。
- `dotnet/`、`winhttp.dll`、`doorstop_config.ini` —— BepInEx 运行依赖（IL2CPP 注入）。
- `arialuni_sdf_u2019` —— 支持中文显示的字体资源。

## 已知限制（非翻译缺口）

- 富文本标签相邻的连接介词（`at` / `of` / `on` / `for` / `as` / `to` 紧贴 `</color>` 标签）为 XUnity 引擎固有限制，原补丁同样如此；强行用裸碎片补全会破坏复合词，故保留。
- 怪物怪叫拟声词（如 `Zi-k`、`R-RO`）、平台名 `Steam Deck` 等按惯例保留英文。
- 若重跑游戏后 `_TmpUntranslated.txt` 出现新串，可继续按相同流程（抽取 → 清洗 → 比对 → 双写 → 模拟）迭代补全。

## 致谢

- 原汉化补丁 `TinyRogues_zh_CN_v1.5.25` 作者及 XUnity.AutoTranslator / BepInEx 项目。
- 中文名称对照来自社区整理的游戏 wiki 注释。
