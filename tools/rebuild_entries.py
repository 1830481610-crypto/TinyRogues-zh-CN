import json, re

with open(r'C:\Users\zengj\Desktop\小小肉鸽汉化制作\community_full.json', 'r', encoding='utf-8') as f:
    comm = json.load(f)

def c(key):
    val = comm.get(key, '')
    return re.sub(r'<[^>]+>', '', val).replace('_x000d_', ' ').strip()

entries = []

# === Ability Titles ===
entries.append(('<color=#008E05>Druidic Rite</color>', c('CLASS_DRUID_ability_name')))
entries.append(('<color=#26AFFF>Wisdom</color>', c('CLASS_WIZARD_ability_name')))
entries.append(('<color=#3A3A79>Cursed Might</color>', c('CLASS_NECROMANCER_ability_name')))
entries.append(('<color=#3B3B7A>Shapechanger</color>', c('CLASS_DOPPELGANGER_ability_name')))
entries.append(('<color=#3E3E9C>Shadow Jutsu</color>', c('CLASS_NINJA_ability_name')))
entries.append(('<color=#45D6C5>Master of Ki</color>', c('CLASS_MONK_ability_name')))
entries.append(('<color=#76428A>Transmutation Guild</color>', c('CLASS_ALCHEMIST_ability_name')))
entries.append(('<color=#7C8A91>Cybernetic Growth</color>', c('CLASS_CYBORG_ability_name')))
entries.append(('<color=#D77BBA>Psychokinesis</color>', c('CLASS_ESPER_ability_name')))
entries.append(('<color=#DD02C0>Chimera</color>', c('CLASS_CHAOS_ability_name')))
entries.append(('<color=#FB0034>Deception</color>', c('CLASS_JESTER_ability_name')))
entries.append(('<color=#FCC926>Crusader</color>', c('CLASS_PALADIN_ability_name')))
entries.append(('<color=#FF0000>Path Of Vengeance</color>', c('CLASS_DEMON HUNTER_ability_name')))
entries.append(('<color=#FF2666>Berserker Strength</color>', c('CLASS_BARBARIAN_ability_name')))
entries.append(('<color=#FF3326>Super Power</color>', c('CLASS_SUPER HERO_ability_name')))
entries.append(('<color=#6ABE30>Double Flourish</color>', c('CLASS_DANCER_ability_name')))
entries.append(('<color=#653187>Lancer</color>', c('CLASS_DRAGOON_ability_name')))
entries.append(('<color=#7C8A91>Preparation</color>', c('CLASS_SOLDIER_ability_name')))
entries.append(('Landlubber', c('CLASS_PIRATE_ability_name')))

# === Ability Descriptions ===
entries.append(('Gain <color=#00E61A>+1</color> <color=#26B0FF>Mana</color><sprite name="Mana"> at level <color=#00E317>2</color>, <color=#00E317>4</color> and <color=#00E317>6</color>.', c('CLASS_WIZARD_ability_desc')))
entries.append(('Gain <color=#00E317>+10%</color> Stats from <color=#FF2666>Strength</color>, <color=#26FF66>Dexterity</color> and <color=#26B0FF>Intelligence</color> per <color=#3B3B7A>Curse</color><sprite name="Curse"> on you.\n', c('CLASS_DEPRIVED_ability_desc')))
entries.append(('<color=#A61FFF>On Dash</color>, summon a Shadow Clone Companion<sprite name="Companion"> for <color=#00E317>8 seconds</color>.\n', c('CLASS_NINJA_ability_desc')))
entries.append(('<color=#A61FFF>On Dash</color>, your next <color=#00E317>3</color> <color=#A61FFF>Attacks</color> deal a guaranteed <color=#FF3326>Critical Hit</color><sprite name="Critical_Hit">.\n', c('CLASS_THIEF_ability_desc')))
entries.append(('When you dash, you can immediately dash again without it costing any <color=#6BBD30>Stamina</color><sprite name="Stamina">.\n', c('CLASS_DANCER_ability_desc')))
entries.append(('Points of <color=#FF2666>Strength</color>, <color=#26FF66>Dexterity</color> or <color=#26B0FF>Intelligence</color>\nadditionally grant <color=#A61FFF>Weapon</color> <color=#A61FFF>Upgrade Level</color>.\n', c('CLASS_CYBORG_ability_desc')))
entries.append(('Gets random Ability, Equipment, <color=#A61FFF>Weapon</color>, Stats and <color=#A61FFF>Skill</color> from other classes.\n', c('CLASS_CHAOS_ability_desc')))
entries.append(('Each point of <color=#FF2666>Strength</color> additionally grants you <color=#00E61A>+1%</color> <color=#FFFFFF>Attack Speed </color>and <color=#00E61A>+0.5%</color> <color=#FF3326>Critical Hit Chance</color><sprite name="Critical_Hit">.', c('CLASS_BARBARIAN_ability_desc')))
entries.append(('At Level 1 you get to choose a Super Power <color=#A61FFF>Trait</color>.\n', c('CLASS_SUPER HERO_ability_desc')))
entries.append(('At Level 1 you get to choose a Psychic Ability <color=#A61FFF>Trait</color>.\n', c('CLASS_ESPER_ability_desc')))
entries.append(('Your Fist <color=#A61FFF>Attacks</color> grant you a <color=#45D6C5>Ki-Charge</color> <color=#A61FFF>on Hit</color>.\n', c('CLASS_MONK_ability_desc')))
entries.append(('You always count as being at <color=#FF2666>Close Range</color><sprite name="Close"> and at <color=#26FF66>Far Range</color><sprite name="Far">.\n', c('CLASS_DRAGOON_ability_desc')))
entries.append(('Rooms can appear <color=red>Tainted</color>, adding additional Enemies but also <color=#00E317>x2.00</color> the Reward.\n', c('CLASS_DEMON HUNTER_ability_desc')))
entries.append(('Gain <color=#00E61A>+15</color> <color=#00E317>to</color> <color=#00E61A>30</color> <color=#EDDE99>Radiant Damage </color>per <color=#406E7D>Armor Container</color><sprite name="Armor"> you have.', c('CLASS_PALADIN_ability_desc')))
entries.append(('Gain <color=#00E61A>+20%</color> Effect of <color=#A61FFF>Debuffs</color> per <color=#A61FFF>Weapon</color> <color=#A61FFF>Upgrade Level </color>you have.', c('CLASS_SOLDIER_ability_desc')))

# === Skill Descriptions ===
entries.append(('Mimic the <color=#A61FFF>Skill</color> of the Class you currently take the form of.', c('CLASS_DOPPELGANGER_skill_desc')))
entries.append(('Jinx all Enemies to inflict <color=#00E317>permanent</color> <color=#3B3B7A>Gloom</color> on them or <color=#3B3B7A>Curse</color><sprite name="Curse"> Doors to upgrade their Rewards if possible.', c('CLASS_DEPRIVED_skill_desc')))
entries.append(('Create a circle on the ground that grants you a Damage <color=#A61FFF>Buff</color> while you stand in it. The <color=#A61FFF>Buff</color> scales with your amount of <color=#26B0FF>Mana</color><sprite name="Mana">.', c('CLASS_WIZARD_skill_desc')))
entries.append(('Leave behind Poses. Dashing consumes Poses to deal <color=#6E5442>Slashing Damage</color>. Activating this <color=#A61FFF>Skill</color> teleports you to your last <color=#A61FFF>Pose</color>.', c('CLASS_DANCER_skill_desc')))
entries.append(('Unleash a barrage of seeking missiles that deal <color=#E03D00>Explosion Damage </color>for a short duration.', c('CLASS_CYBORG_skill_desc')))
entries.append(('Flex your muscles and become <color=#00E61A>Invulnerable</color> for a short duration. If you would have taken damage in that duration, gain an <color=#FFFFFF>Attack Speed </color><color=#A61FFF>Buff</color>.', c('CLASS_BARBARIAN_skill_desc')))
entries.append(('Turn an enemy into a harmless sheep.\nCan also be used on Treasure Chests and Shrines at your own risk!', c('CLASS_ALCHEMIST_skill_desc')))
entries.append(('Fly up in the air, before dropping down and smashing the ground with your Fists to deal massive <color=#6E5442>Striking Damage</color>.', c('CLASS_SUPER HERO_skill_desc')))
entries.append(('Call in some Pirate Companions<sprite name="Companion"> for a short duration.', c('CLASS_PIRATE_skill_desc')))
entries.append(('Emit a cone of holy light that protects you from Enemy Projectiles and inflicts <color=#EBD98D>Judgement</color> for a short duration.', c('CLASS_PALADIN_skill_desc')))
entries.append(('Turn <color=#00E61A>intangible</color> and mark Enemies by touching them, inflicting Damage when the <color=#A61FFF>Skill</color> ends.', c('CLASS_NINJA_skill_desc')))
entries.append(('Become <color=#00E61A>Invulnerable</color> to all Enemy Damage for a short duration.', c('CLASS_MONK_skill_desc')))
entries.append(('Blink away and leave behind a decoy. Enemies will attack the decoy for a short duration.', c('CLASS_JESTER_skill_desc')))
entries.append(('Deflect all Enemy Projectiles around you for a short duration, retaliating with <color=#6E5442>Physical Damage</color>.', c('CLASS_ESPER_skill_desc')))
entries.append(('Jump to a targeted location dealing <color=#6E5442>Physical Damage </color>in an area.', c('CLASS_DRAGOON_skill_desc')))
entries.append(('For a short duration, with each <color=#A61FFF>Attack</color> a shadow of your past also shoots a bullet.', c('CLASS_DEMON HUNTER_skill_desc')))
entries.append(('Arrest an Enemy, inflicting a <color=#A61FFF>Debuff</color> and removing its <color=#FF00FF>Enchantment</color> Modifiers.', c('CLASS_SOLDIER_skill_desc')))

# === Class Description ===
entries.append(('A master of material transformation, the Alchemist harnesses the ancient art of transmutation, turning the ordinary into the extraordinary.', c('CLASS_ALCHEMIST_class_desc')))

# === Items/Equipment ===
entries.append(('Alchemical Concoction', '炼金药剂'))
entries.append(('PARAGON', '巅峰'))
entries.append(('Paragon Level 50', '巅峰等级 50'))

# === NPC Dialogues ===
entries.append(('You are no exception\nto this rule.', '你也不例外。\n在死亡面前无人幸免。'))
entries.append(('And today shall\nbe no exception!', '而今天也不会\n是例外！'))
entries.append(('That was an exceptional\nperformance.', '那真是精彩绝伦的\n表现。'))
entries.append(("*You got a feeling it's\ntime to stop throwing\ngold into a random well.*", '*你感觉到是时候\n停止往一口随机井里\n扔金币了.*'))
entries.append(('*You permanently gained\n[[+1]] maximum mana<sprite name="Mana">.*', '*你永久获得了\n[[+1]]点最大法力<sprite name="Mana">.*'))
entries.append(('*You permanently gained\n[[+1]] stamina<sprite name="Stamina">.*', '*你永久获得了\n[[+1]]点耐力<sprite name="Stamina">.*'))
entries.append(("That's alright.\nSometimes, the greatest answers\ncome not from tools, but from within.\nGo in peace.", '没关系。\n有时候，最伟大的答案\n并非来自工具，而是来自你的内心。\n愿平安与你同在。'))
entries.append(("That's quite alright.\nSometimes, the greatest gift\nis the one we don't take.", '没关系的。\n有时候，最珍贵的礼物\n恰恰是那些我们没有拿走的。'))
entries.append(('These <color=#5FCDE4>Ethereal Dice</color> are not about\nwinning or losing.\nThey are a reflection of faith —\nfaith in yourself, and in the path before you.\nDo you wish to carry them? <color=grey>(x3)</color>', '这些<color=#5FCDE4>灵骰</color>无关\n输赢。\n它们是一种信念的映照——\n对自己的信念，对前路的信念。\n你愿意带上它们吗？<color=grey>(x3)</color>'))

# Write
with open(r'D:\SteamLibrary\steamapps\common\Tiny Rogues\BepInEx\Translation\zh\Text\TinyRogues_zh.txt', 'r', encoding='utf-8') as f:
    existing = f.read()

added = 0
with open(r'D:\SteamLibrary\steamapps\common\Tiny Rogues\BepInEx\Translation\zh\Text\TinyRogues_zh.txt', 'a', encoding='utf-8') as f:
    for en, zh in entries:
        if en not in existing:
            f.write(f'{en}={zh}\n')
            added += 1

# Count total
with open(r'D:\SteamLibrary\steamapps\common\Tiny Rogues\BepInEx\Translation\zh\Text\TinyRogues_zh.txt', 'r', encoding='utf-8') as f:
    total = len(f.readlines())

print(f'Added {added} entries. Total: {total} lines.')
