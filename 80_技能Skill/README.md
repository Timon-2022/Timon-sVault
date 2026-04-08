# 财经新闻自动抓取系统

每天 9:05 自动生成财经日报，整理 RSS 周报到 Obsidian。

## 快速开始

### 1. 安装依赖
```bash
cd "/Users/timon/Library/Mobile Documents/iCloud~md~obsidian/Documents/iCloud Vault/06_ClaudeTasks/Fin_Daily"
pip3 install -r requirements.txt
```

### 2. 设置定时任务（每天 9:05 自动运行）
```bash
./setup_cron.sh
```

### 3. 手动运行

**生成日报：**
```bash
python3 fetch_daily_news.py
```

**生成周报（LingoWhale RSS）：**
```bash
# 首次使用，需要先登录保存 cookies
pip3 install playwright
playwright install
python3 login_lingowhale.py

# 之后可以直接生成周报
python3 fetch_weekly_rss.py
```

## 文件说明

- `fetch_daily_news.py` - 日报抓取（财联社、同花顺）
- `fetch_weekly_rss.py` - 周报抓取（LingoWhale RSS）
- `login_lingowhale.py` - LingoWhale 登录工具
- `config.json` - 配置文件（新闻源、关键词等）
- `setup_cron.sh` - 定时任务安装脚本
- `Daily/` - 日报存放目录
- `Weekly/` - 周报存放目录

## 输出示例

**日报文件名：** `01-13 [最重要事件标题].md`

**周报文件名：** `第3周 RSS周报 01-13.md`

## 内容分类

- 🔥 重大事件
- 🌍 地缘政治
- 📋 中国政策
- 🏢 企业动态
- 📰 其他新闻

## 查看日志

```bash
cat logs/daily_$(date +%Y%m%d).log
```

## 完整文档

详细说明请查看 [CLAUDE.md](CLAUDE.md)

---

**更新时间：** 2026-01-13
