# 荒境纪元 · 文字生存冒险

中文文字生存游戏，包含场景切换、资源采集、人物需求、装备耐久和家园发展。A Chinese text-survival adventure for the browser, with a separate Python prototype.

## 运行网页版

```bash
git clone https://github.com/gura8390/NEW.git
cd NEW
python -m http.server 8000
```

打开 `http://localhost:8000/index.html`。现有仓库名称仍为 `NEW`，正文使用游戏名称便于识别。

## 游戏内容

- 在大本营、城镇、家园和野外地点之间行动。
- 与 NPC 互动，学习技能、采集资源和制作物品。
- 管理饥饿、口渴与休息需求。
- 使用食物、装备工具，并处理工具限制和耐久。
- 发展家园与科技，探索获得更多物品。

## 文件说明

| 文件 | 用途 |
|---|---|
| `index.html` | 中文网页游戏入口 |
| `NPC.json` | NPC 名称、技能与服务数据 |
| `ITEM.json` | 物品分类与编号数据 |
| `game.py` | 独立的 Python 文字交互原型，不是网页服务器 |

Python 原型与网页版分别保存，不假定两者功能、数据和存档完全一致。若要试运行 Python 原型，在安装 Python 后执行 `python game.py`。

## 项目关系与状态

[BIGMCXM](https://github.com/gura8390/BIGMCXM) 和 [KUBI](https://github.com/gura8390/KUBI) 是其他文字游戏项目，分别保留。本项目是实验作品，完整游戏流程仍需单独验收。

## 许可证

[MIT License](LICENSE)。
