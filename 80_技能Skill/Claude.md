# 财经每日要闻自动抓取系统

## 用户画像

**身份**: 炒股和投资的 AI 产品经理

**关注重点**:
- 🎯 **AI行业动态**: AI应用、大模型、算力、芯片等相关新闻
- 📊 **投资机会**: 政策利好、行业趋势、龙头企业动向
- 🌍 **宏观政策**: 国内政策变化、地缘政治对市场的影响
- 💡 **技术创新**: 半导体、新能源、生物医药等前沿科技
- 📈 **市场情绪**: 涨停板分析、热点板块轮动、资金流向

**信息需求**:
1. **快速浏览**: 标题要一目了然，核心信息提炼清晰
2. **深度阅读**: 重要新闻需要保留原文链接，方便深入研究
3. **分类整理**: 按照投资逻辑分类（政策、企业、技术、市场等）
4. **时效性强**: 每天早上9:05自动更新，不错过任何重要信息

**工作流程**:
- 早上 9:05 查看日报，了解隔夜重要新闻
- 对感兴趣的新闻点击链接深入阅读
- 周末查看周报，回顾本周重大事件
- 将关键信息整理到投资研究笔记中

## 项目简介

本系统为 AI 产品经理量身定制，自动抓取每日财经热点要闻和 RSS 订阅内容，整理成结构化的 Obsidian 笔记，聚焦投资决策所需的关键信息。

## 功能特性

### 📰 日报功能
- **时间范围**: 前一日 18:00 至今日 08:00
- **新闻来源**: 财联社、新浪财经
- **自动运行**: 每天早上 9:05 自动生成
- **输出格式**: 标题 + 核心内容摘要 + 原文链接
- **内容分类**:
  1. 🔥 重大事件 - 涨停板分析、市场异动
  2. 🤖 AI科技 - 人工智能、芯片、算力、大模型
  3. 📋 中国政策 - 央行政策、监管动向、产业规划
  4. 🏢 企业动态 - 龙头企业、并购重组、业绩预告
  5. 🌍 地缘政治 - 国际局势、贸易摩擦
  6. 📰 其他新闻

### 📊 周报功能
- **数据来源**: LingoWhale RSS 订阅（需要登录）
- **生成周期**: 手动运行或定时生成
- **内容分类**: 同日报分类体系
- **详细内容**: 包含标题、摘要、链接等完整信息

## 文件结构

```
Fin_Daily/
├── CLAUDE.md              # 本说明文件
├── config.json            # 配置文件（新闻源、分类关键词等）
├── fetch_daily_news.py    # 日报抓取脚本
├── fetch_weekly_rss.py    # 周报抓取脚本（RSS）
├── requirements.txt       # Python 依赖
├── setup_cron.sh          # 定时任务安装脚本
├── Daily/                 # 日报存放目录
│   └── MM-DD [事件标题].md
├── Weekly/                # 周报存放目录
│   └── 第N周 RSS周报 MM-DD.md
└── logs/                  # 运行日志
    └── daily_YYYYMMDD.log
```

## 快速开始

### 1. 安装依赖

```bash
cd "/Users/timon/Library/Mobile Documents/iCloud~md~obsidian/Documents/iCloud Vault/06_ClaudeTasks/Fin_Daily"
pip3 install -r requirements.txt

# 如果需要使用周报功能（LingoWhale），还需要安装 Playwright
pip3 install playwright
playwright install
```

### 2. 配置新闻源（可选）

编辑 `config.json` 文件，可以：
- 修改新闻源地址
- 调整分类关键词
- 设置输出格式
- 添加 LingoWhale 登录凭据

### 3. 手动运行

#### 生成日报
```bash
python3 fetch_daily_news.py
```

#### 生成周报
```bash
# 不带登录（如果 LingoWhale 不需要登录）
python3 fetch_weekly_rss.py

# 带登录凭据
python3 fetch_weekly_rss.py --username 你的用户名 --password 你的密码
```

### 4. 设置自动运行（推荐）

运行安装脚本，设置每天早上 9:05 自动生成日报：

```bash
./setup_cron.sh
```

安装完成后，可以查看定时任务：
```bash
crontab -l
```

## 配置说明

### config.json 结构

```json
{
  "news_sources": {
    "财联社": "新闻源URL",
    "同花顺": "新闻源URL"
  },
  "categories": {
    "分类名": ["关键词1", "关键词2", ...]
  },
  "output": {
    "daily_folder": "Daily",
    "weekly_folder": "Weekly",
    "max_items_per_category": 10,
    "max_others": 5
  },
  "rss": {
    "lingowhale_url": "https://lingowhale.com/channels",
    "require_login": true
  }
}
```

### 自定义分类关键词

在 `config.json` 中修改 `categories` 部分，例如：

```json
{
  "categories": {
    "AI科技": ["人工智能", "ChatGPT", "AI", "机器学习"],
    "新能源": ["电池", "光伏", "风电", "新能源汽车"]
  }
}
```

## 输出格式

### 日报格式示例

```markdown
# MM-DD 事件标题

> 抓取时间: YYYY-MM-DD HH:MM:SS
> 新闻范围: MM-DD 18:00 - MM-DD 08:00

## 🔥 重大事件

- **HH:MM** | 新闻标题内容 _(来源)_

## 🌍 地缘政治

- **HH:MM** | 新闻标题内容 _(来源)_

## 📊 统计信息

- 重大事件: X 条
- 地缘政治: X 条
- 总计: X 条新闻
```

### 周报格式示例

```markdown
# 第 N 周 RSS 周报

> 生成时间: YYYY-MM-DD HH:MM:SS
> 周期: YYYY-MM-DD - YYYY-MM-DD

## 🌍 地缘政治

### 新闻标题

新闻摘要内容...

- **来源**: LingoWhale
- **时间**: 发布时间
- **链接**: [URL](URL)

---

## 📊 统计信息

- 地缘政治: X 条
- 总计: X 条内容
```

## 使用技巧

### 1. 查看运行日志

```bash
# 查看今天的日志
cat logs/daily_$(date +%Y%m%d).log

# 查看最近的日志
tail -f logs/daily_*.log
```

### 2. 手动测试定时任务

```bash
cd "/Users/timon/Library/Mobile Documents/iCloud~md~obsidian/Documents/iCloud Vault/06_ClaudeTasks/Fin_Daily"
python3 fetch_daily_news.py
```

### 3. 临时停用定时任务

```bash
# 编辑 crontab
crontab -e

# 在相关行前添加 # 注释掉，或直接删除该行
```

### 4. LingoWhale 登录配置

如果您不想每次都输入用户名密码，可以：

**方法一：使用环境变量**
```bash
export LINGOWHALE_USERNAME="你的用户名"
export LINGOWHALE_PASSWORD="你的密码"
python3 fetch_weekly_rss.py
```

**方法二：修改脚本**
直接在 `fetch_weekly_rss.py` 中添加默认凭据（不推荐，安全风险）

**方法三：使用 Cookie**
从浏览器导出登录态的 Cookie，修改脚本使用 Cookie 方式（需要自行实现）

## 故障排除

### 问题：定时任务未运行

1. 检查 crontab 是否正确安装：
   ```bash
   crontab -l
   ```

2. 检查日志文件是否有错误信息：
   ```bash
   ls -l logs/
   cat logs/daily_*.log
   ```

3. 确认 Python 路径正确：
   ```bash
   which python3
   ```

### 问题：抓取失败或内容为空

1. 检查网络连接
2. 确认新闻源 URL 是否可访问
3. 网站结构可能变化，需要更新抓取逻辑
4. 查看具体错误信息：
   ```bash
   python3 fetch_daily_news.py
   ```

### 问题：LingoWhale 登录失败

1. 确认用户名和密码正确
2. 检查是否安装了 Playwright：
   ```bash
   pip3 show playwright
   playwright install
   ```
3. 尝试增加等待时间或手动登录后导出 Cookie

### 问题：分类不准确

编辑 `config.json`，在对应分类中添加更多关键词：

```json
{
  "categories": {
    "企业动态": [
      "现有关键词...",
      "新增关键词1",
      "新增关键词2"
    ]
  }
}
```

## 进阶功能

### 添加新的新闻源

1. 在 `config.json` 中添加新闻源 URL
2. 在 `fetch_daily_news.py` 中添加对应的抓取函数
3. 参考现有的 `fetch_cailian_news()` 和 `fetch_tonghuashun_news()` 实现

### 自定义输出格式

修改 `fetch_daily_news.py` 中的 `_generate_markdown_content()` 方法。

### 集成到其他系统

脚本返回值：
- 成功：返回 0，生成的文件路径会打印到标准输出
- 失败：返回 1，错误信息打印到标准错误

可以在其他脚本中调用：
```bash
python3 fetch_daily_news.py && echo "日报生成成功"
```

## 注意事项

- ⚠️ 新闻内容仅供参考，不构成投资建议
- ⚠️ 如遇网络问题可能抓取失败，请手动重试
- ⚠️ 建议每日定时运行，避免遗漏重要信息
- ⚠️ LingoWhale 需要登录，请妥善保管账号密码
- ⚠️ 定期检查日志，确保定时任务正常运行
- ⚠️ 新闻源网站结构变化可能导致抓取失败，需要及时更新脚本

## 更新日志

### v1.0.0 (2026-01-13)
- ✅ 初始版本发布
- ✅ 支持财联社、同花顺新闻抓取
- ✅ 实现自动分类功能
- ✅ 支持定时任务（每天 9:05）
- ✅ 添加 LingoWhale RSS 周报功能
- ✅ 生成结构化 Obsidian 笔记

## 联系与支持

如有问题或建议，请通过以下方式联系：
- 项目位置: `/Users/timon/Library/Mobile Documents/iCloud~md~obsidian/Documents/iCloud Vault/06_ClaudeTasks/Fin_Daily`
- 在 Claude Code 中执行: `请修复财经新闻抓取问题`

---

📅 最后更新: 2026-01-13
