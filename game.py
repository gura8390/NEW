from __future__ import annotations

import random
from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    race: str
    faction: str
    path: str
    hp: int = 100
    attack: int = 8
    magic: int = 8
    wood: int = 0
    food: int = 5
    farmland: int = 0
    shelter_level: int = 0
    tech_level: int = 0
    day: int = 1
    flags: set[str] = field(default_factory=set)

    def status(self) -> str:
        return (
            f"\n===== 第 {self.day} 天 =====\n"
            f"姓名：{self.name} | 种族：{self.race} | 阵营：{self.faction} | 成长方向：{self.path}\n"
            f"生命：{self.hp} | 武力：{self.attack} | 魔法：{self.magic}\n"
            f"木材：{self.wood} | 食物：{self.food} | 农田：{self.farmland} 级\n"
            f"庇护所：{self.shelter_level} 级 | 科技：{self.tech_level} 级\n"
        )


def choose(prompt: str, options: list[str]) -> str:
    while True:
        print(prompt)
        for i, o in enumerate(options, start=1):
            print(f"{i}. {o}")
        ans = input("请输入编号：").strip()
        if ans.isdigit() and 1 <= int(ans) <= len(options):
            return options[int(ans) - 1]
        print("输入无效，请重试。\n")


def intro() -> Player:
    print("欢迎来到《荒境纪元：文字生存冒险》")
    print("你将从荒野开始，砍伐木材、收集食物、建立农田与科技，发展庇护所并踏上冒险。\n")

    name = input("请输入你的名字：").strip() or "无名旅者"
    race = choose("选择你的种族：", ["人类", "兽人", "精灵", "矮人"])
    faction = choose("选择要加入的阵营：", ["晨光同盟", "钢铁部族", "暮影议会"])
    path = choose("选择主要成长方向：", ["武力修行", "奥术研习"])

    p = Player(name=name, race=race, faction=faction, path=path)

    if race == "兽人":
        p.attack += 4
        p.hp += 15
    elif race == "精灵":
        p.magic += 4
    elif race == "矮人":
        p.wood += 3

    if path == "武力修行":
        p.attack += 3
    else:
        p.magic += 3

    if faction == "晨光同盟":
        p.food += 2
    elif faction == "钢铁部族":
        p.wood += 2
    else:
        p.magic += 2

    print("\n你已踏入荒境，第一天从生存开始！")
    return p


def gather_wood(p: Player) -> None:
    gained = random.randint(3, 8)
    p.wood += gained
    print(f"你砍伐树木，获得木材 {gained}。")


def gather_food(p: Player) -> None:
    gained = random.randint(2, 6)
    p.food += gained
    print(f"你采集并狩猎，获得食物 {gained}。")


def build_farm(p: Player) -> None:
    cost_wood, cost_food = 6 + p.farmland * 2, 3
    if p.wood >= cost_wood and p.food >= cost_food:
        p.wood -= cost_wood
        p.food -= cost_food
        p.farmland += 1
        print(f"你开垦了新的农田，农田等级提升到 {p.farmland}。")
    else:
        print(f"资源不足，建造农田需要木材 {cost_wood}、食物 {cost_food}。")


def develop_tech(p: Player) -> None:
    cost_wood, cost_food = 5 + p.tech_level * 3, 4
    if p.wood >= cost_wood and p.food >= cost_food:
        p.wood -= cost_wood
        p.food -= cost_food
        p.tech_level += 1
        if p.path == "武力修行":
            p.attack += 2
        else:
            p.magic += 2
        print(f"你研究了新技术，科技等级提升到 {p.tech_level}。")
    else:
        print(f"资源不足，发展科技需要木材 {cost_wood}、食物 {cost_food}。")


def upgrade_shelter(p: Player) -> None:
    cost_wood = 8 + p.shelter_level * 4
    if p.wood >= cost_wood:
        p.wood -= cost_wood
        p.shelter_level += 1
        p.hp += 8
        print(f"庇护所升级成功，当前等级 {p.shelter_level}，生命上限提高！")
    else:
        print(f"资源不足，升级庇护所需要木材 {cost_wood}。")


def train(p: Player) -> None:
    if p.path == "武力修行":
        gain = random.randint(1, 3)
        p.attack += gain
        print(f"你进行战斗训练，武力 +{gain}。")
    else:
        gain = random.randint(1, 3)
        p.magic += gain
        print(f"你冥想并操控魔力，魔法 +{gain}。")


def adventure(p: Player) -> None:
    enemy = random.choice(["荒野狼群", "堕落兽人", "迷雾妖灵", "遗迹守卫"])
    enemy_power = random.randint(8, 20) + p.day // 2
    player_power = p.attack + p.magic // 2 + random.randint(0, 6)

    print(f"你踏上冒险，遭遇了【{enemy}】！")
    print(f"敌方战力：{enemy_power} | 你的战力判定：{player_power}")

    if player_power >= enemy_power:
        wood_reward = random.randint(2, 6)
        food_reward = random.randint(2, 6)
        p.wood += wood_reward
        p.food += food_reward
        print(f"你获胜了！获得木材 {wood_reward}、食物 {food_reward}。")
        if "首次冒险" not in p.flags:
            p.flags.add("首次冒险")
            print("你完成了首次冒险，声望在阵营中提升！")
    else:
        damage = random.randint(8, 18)
        p.hp -= damage
        print(f"你战败撤退，生命 -{damage}。")


def end_of_day(p: Player) -> bool:
    consume = max(3, 5 - p.farmland)
    p.food -= consume
    if p.food < 0:
        p.hp += p.food
        p.food = 0
        print("食物短缺，你因饥饿受到伤害！")

    if p.day % 3 == 0 and p.farmland > 0:
        harvest = p.farmland * random.randint(2, 4)
        p.food += harvest
        print(f"农田迎来收成，你获得食物 {harvest}。")

    p.day += 1

    if p.hp <= 0:
        print("\n你在荒境中倒下了。游戏结束。")
        return False

    if p.shelter_level >= 3 and p.tech_level >= 3 and p.day > 12:
        print("\n你建立了稳固的文明据点！荒境在你手中重获秩序。")
        print("恭喜达成胜利结局：拓荒领主")
        return False

    return True


def main() -> None:
    player = intro()

    actions = {
        "砍伐木材": gather_wood,
        "收集食物": gather_food,
        "建设农田": build_farm,
        "发展科技": develop_tech,
        "升级庇护所": upgrade_shelter,
        "训练（武力/魔法）": train,
        "外出冒险": adventure,
    }

    running = True
    while running:
        print(player.status())
        action = choose("今天你要做什么？", list(actions.keys()) + ["结束游戏"])
        if action == "结束游戏":
            print("你选择暂时离开荒境。")
            break

        actions[action](player)
        running = end_of_day(player)


if __name__ == "__main__":
    main()
