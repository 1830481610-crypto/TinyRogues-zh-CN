import json, re

with open(r'C:\Users\zengj\Desktop\小小肉鸽汉化制作\community_full.json', 'r', encoding='utf-8') as f:
    comm = json.load(f)

def c(key):
    val = comm.get(key, '')
    return re.sub(r'<[^>]+>', '', val).replace('_x000d_', ' ').strip()

# Read current file
with open(r'D:\SteamLibrary\steamapps\common\Tiny Rogues\BepInEx\Translation\zh\Text\TinyRogues_zh.txt', 'r', encoding='utf-8') as f:
    content = f.read()

existing = set()
for line in content.split('\n'):
    if '=' in line:
        existing.add(line.split('=', 1)[0])

entries = []

# ===== Class titles (community text, keep = in color tags carefully) =====
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

# ===== Class Ability Descriptions =====
entries.append(('Gain <color=#00E61A>+1</color> <color=#26B0FF>Mana</color><sprite name="Mana"> at level <color=#00E317>2</color>, <color=#00E317>4</color> and <color=#00E317>6</color>.', c('CLASS_WIZARD_ability_desc')))
entries.append(('Gain <color=#00E317>+10%</color> Stats from <color=#FF2666>Strength</color>, <color=#26FF66>Dexterity</color> and <color=#26B0FF>Intelligence</color> per <color=#3B3B7A>Curse</color><sprite name="Curse"> on you.', c('CLASS_DEPRIVED_ability_desc')))
entries.append(('Gain <color=#00E61A>+20%</color> Effect of <color=#A61FFF>Debuffs</color> per <color=#A61FFF>Weapon</color> <color=#A61FFF>Upgrade Level </color>you have.', c('CLASS_SOLDIER_ability_desc')))
entries.append(('<color=#A61FFF>On Dash</color>, summon a Shadow Clone Companion<sprite name="Companion"> for <color=#00E317>8 seconds</color>.', c('CLASS_NINJA_ability_desc')))
entries.append(('<color=#A61FFF>On Dash</color>, your next <color=#00E317>3</color> <color=#A61FFF>Attacks</color> deal a guaranteed <color=#FF3326>Critical Hit</color><sprite name="Critical_Hit">.', c('CLASS_THIEF_ability_desc')))
entries.append(('When you dash, you can immediately dash again without it costing any <color=#6BBD30>Stamina</color><sprite name="Stamina">.', c('CLASS_DANCER_ability_desc')))
entries.append(('Points of <color=#FF2666>Strength</color>, <color=#26FF66>Dexterity</color> or <color=#26B0FF>Intelligence</color> additionally grant <color=#A61FFF>Weapon</color> <color=#A61FFF>Upgrade Level</color>.', c('CLASS_CYBORG_ability_desc')))
entries.append(('Gets random Ability, Equipment, <color=#A61FFF>Weapon</color>, Stats and <color=#A61FFF>Skill</color> from other classes.', c('CLASS_CHAOS_ability_desc')))
entries.append(('Each point of <color=#FF2666>Strength</color> additionally grants you <color=#00E61A>+1%</color> <color=#FFFFFF>Attack Speed </color>and <color=#00E61A>+0.5%</color> <color=#FF3326>Critical Hit Chance</color><sprite name="Critical_Hit">.', c('CLASS_BARBARIAN_ability_desc')))
entries.append(('At Level 1 you get to choose a Super Power <color=#A61FFF>Trait</color>.', c('CLASS_SUPER HERO_ability_desc')))
entries.append(('At Level 1 you get to choose a Psychic Ability <color=#A61FFF>Trait</color>.', c('CLASS_ESPER_ability_desc')))
entries.append(('Your Fist <color=#A61FFF>Attacks</color> grant you a <color=#45D6C5>Ki-Charge</color> <color=#A61FFF>on Hit</color>.', c('CLASS_MONK_ability_desc')))
entries.append(('You always count as being at <color=#FF2666>Close Range</color><sprite name="Close"> and at <color=#26FF66>Far Range</color><sprite name="Far">.', c('CLASS_DRAGOON_ability_desc')))
entries.append(('Rooms can appear <color=red>Tainted</color>, adding additional Enemies but also <color=#00E317>x2.00</color> the Reward.', c('CLASS_DEMON HUNTER_ability_desc')))
entries.append(('Gain <color=#00E61A>+15</color> <color=#00E317>to</color> <color=#00E61A>30</color> <color=#EDDE99>Radiant Damage </color>per <color=#406E7D>Armor Container</color><sprite name="Armor"> you have.', c('CLASS_PALADIN_ability_desc')))

# ===== Skill Descriptions =====
entries.append(('Mimic the <color=#A61FFF>Skill</color> of the Class you currently take the form of.', c('CLASS_DOPPELGANGER_skill_desc')))
entries.append(('Jinx all Enemies to inflict <color=#00E317>permanent</color> <color=#3B3B7A>Gloom</color> on them or <color=#3B3B7A>Curse</color><sprite name="Curse"> Doors to upgrade their Rewards if possible.', c('CLASS_DEPRIVED_skill_desc')))
entries.append(('Create a circle on the ground that grants you a Damage <color=#A61FFF>Buff</color> while you stand in it. The <color=#A61FFF>Buff</color> scales with your amount of <color=#26B0FF>Mana</color><sprite name="Mana">.', c('CLASS_WIZARD_skill_desc')))
entries.append(('Leave behind Poses. Dashing consumes Poses to deal <color=#6E5442>Slashing Damage</color>. Activating this <color=#A61FFF>Skill</color> teleports you to your last <color=#A61FFF>Pose</color>.', c('CLASS_DANCER_skill_desc')))
entries.append(('Unleash a barrage of seeking missiles that deal <color=#E03D00>Explosion Damage </color>for a short duration.', c('CLASS_CYBORG_skill_desc')))
entries.append(('Flex your muscles and become <color=#00E61A>Invulnerable</color> for a short duration. If you would have taken damage in that duration, gain an <color=#FFFFFF>Attack Speed </color><color=#A61FFF>Buff</color>.', c('CLASS_BARBARIAN_skill_desc')))
entries.append(('Turn an enemy into a harmless sheep.', c('CLASS_ALCHEMIST_skill_desc')))
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

# ===== Class Description =====
entries.append(('A master of material transformation, the Alchemist harnesses the ancient art of transmutation, turning the ordinary into the extraordinary.', c('CLASS_ALCHEMIST_class_desc')))

# ===== Items =====
entries.append(('Alchemical Concoction', '炼金药剂'))
entries.append(('PARAGON', '巅峰'))
entries.append(('Paragon Level 50', '巅峰等级 50'))
entries.append(('<color=#4CC2FF>Cap\'n\'Bells</color>', '<color=#4CC2FF>铃铛帽</color>'))

# ===== Cinder / Paragon =====
entries.append(('<color=#5ECCE3>Paragon EXP Bonus</color>', '<color=#5ECCE3>巅峰经验加成</color>'))
entries.append(('<color=#5ECCE3>+30% PARAGON EXP</color>', '<color=#5ECCE3>+30% 巅峰经验</color>'))
entries.append(('<color=#808080>+0% PARAGON EXP</color>', '<color=#808080>+0% 巅峰经验</color>'))
entries.append(('Beyond Good and Evil', '超越善恶'))

# ===== NPC Dialogues =====
entries.append(('You are no exception to this rule.', '你也不例外。在死亡面前无人幸免。'))
entries.append(('And today shall be no exception!', '而今天也不会是例外！'))
entries.append(('That was an exceptional performance.', '那真是精彩绝伦的表现。'))
entries.append(("*You got a feeling it's time to stop throwing gold into a random well.*", '*你感觉到是时候停止往一口随机井里扔金币了.*'))
entries.append(('*You permanently gained [[+1]] maximum mana<sprite name="Mana">.*', '*你永久获得了[[+1]]点最大法力<sprite name="Mana">.*'))
entries.append(('*You permanently gained [[+1]] stamina<sprite name="Stamina">.*', '*你永久获得了[[+1]]点耐力<sprite name="Stamina">.*'))
entries.append(("That's alright. Sometimes, the greatest answers come not from tools, but from within. Go in peace.", '没关系。有时候，最伟大的答案并非来自工具，而是来自你的内心。愿平安与你同在。'))
entries.append(("That's quite alright. Sometimes, the greatest gift is the one we don't take.", '没关系的。有时候，最珍贵的礼物恰恰是那些我们没有拿走的。'))
entries.append(('These <color=#5FCDE4>Ethereal Dice</color> are not about winning or losing. They are a reflection of faith — faith in yourself, and in the path before you. Do you wish to carry them? <color=grey>(x3)</color>', '这些<color=#5FCDE4>灵骰</color>无关输赢。它们是一种信念的映照——对自己的信念，对前路的信念。你愿意带上它们吗？<color=grey>(x3)</color>'))

# ===== Cinder Modifiers (translate now, community glossary for terms) =====
cinder = [
    ('<color=#FF00FF>Enchanted Enemies </color>have a <color=red>20%</color> chance to gain an additional Defensive Modifier.', '<color=#FF00FF>附魔敌人</color>有<color=red>20%</color>几率获得一个额外的防御修正。'),
    ('<color=#FF00FF>Enchanted Enemies </color>have a <color=red>50%</color> chance to gain an additional Secondary Modifier.', '<color=#FF00FF>附魔敌人</color>有<color=red>50%</color>几率获得一个额外的次级修正。'),
    ('Floors contain up to <color=red>x3.00</color> times more packs of <color=#FF00FF>Enchanted Enemies</color>.', '楼层中包含最多<color=red>x3.00</color>倍的<color=#FF00FF>附魔敌人</color>群组。'),
    ('Bosses are accompanied by <color=red>2</color> random Guardian <color=#8000FF>Automatons</color>.', 'Boss会有<color=red>2</color>个随机守护<color=#8000FF>自动人偶</color>陪同。'),
    ('A Centurion Hunter <color=#8000FF>Automaton</color> will sometimes invade combat encounters and attack you.', '百夫长猎人<color=#8000FF>自动人偶</color>有时会入侵战斗并攻击你。'),
    ('Bosses have <color=#00E317>x0.75</color> <color=#FF3326>Health</color><sprite name="Heart"> and <color=#406E7D>Armor</color><sprite name="Armor"> in the first phase but <color=red>x1.25</color> in the second phase.', 'Boss在第一阶段拥有<color=#00E317>x0.75</color>的<color=#FF3326>生命</color><sprite name="Heart">和<color=#406E7D>护甲</color><sprite name="Armor">，但在第二阶段变为<color=red>x1.25</color>。'),
    ('<color=#8000FF>Reapers</color> can now spawn regardless of how <color=#3B3B7A>Cursed</color><sprite name="Curse"> you are. <color=#8000FF>Reapers</color> gain <color=#406E7D>Armor</color><sprite name="Armor"> and an additional Attack.', '<color=#8000FF>死神</color>现在无论你有多少<color=#3B3B7A>诅咒</color><sprite name="Curse">都会出现。<color=#8000FF>死神</color>获得<color=#406E7D>护甲</color><sprite name="Armor">和额外攻击。'),
]
entries.extend(cinder)

# ===== Write =====
added = 0
with open(r'D:\SteamLibrary\steamapps\common\Tiny Rogues\BepInEx\Translation\zh\Text\TinyRogues_zh.txt', 'a', encoding='utf-8') as f:
    for en, zh in entries:
        if en not in existing:
            f.write(f'{en}={zh}\n')
            existing.add(en)
            added += 1

print(f'Added {added} new entries')
