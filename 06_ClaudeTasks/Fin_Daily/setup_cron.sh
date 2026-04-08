#!/bin/bash
# 财经新闻自动抓取 - 定时任务安装脚本
# 每天早上 9:05 自动运行

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/fetch_daily_news.py"
LOG_DIR="$SCRIPT_DIR/logs"

# 创建日志目录
mkdir -p "$LOG_DIR"

echo "========================================"
echo "财经新闻抓取 - 定时任务安装"
echo "========================================"
echo ""
echo "脚本位置: $SCRIPT_DIR"
echo "Python 脚本: $PYTHON_SCRIPT"
echo "日志目录: $LOG_DIR"
echo ""

# 检查 Python 脚本是否存在
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "错误: 找不到 Python 脚本 $PYTHON_SCRIPT"
    exit 1
fi

# 获取当前的 crontab
TEMP_CRON=$(mktemp)
crontab -l > "$TEMP_CRON" 2>/dev/null || true

# 检查是否已经存在该任务
if grep -q "fetch_daily_news.py" "$TEMP_CRON"; then
    echo "检测到已存在的定时任务，正在删除旧任务..."
    grep -v "fetch_daily_news.py" "$TEMP_CRON" > "$TEMP_CRON.new"
    mv "$TEMP_CRON.new" "$TEMP_CRON"
fi

# 添加新的 crontab 条目
# 每天早上 9:05 运行
echo "# 财经新闻自动抓取 - 每天 9:05 运行" >> "$TEMP_CRON"
echo "5 9 * * * cd \"$SCRIPT_DIR\" && /usr/bin/python3 \"$PYTHON_SCRIPT\" >> \"$LOG_DIR/daily_\$(date +\%Y\%m\%d).log\" 2>&1" >> "$TEMP_CRON"
echo "" >> "$TEMP_CRON"

# 安装新的 crontab
crontab "$TEMP_CRON"
rm "$TEMP_CRON"

echo "✓ 定时任务安装成功！"
echo ""
echo "任务详情:"
echo "  - 运行时间: 每天早上 9:05"
echo "  - 执行脚本: $PYTHON_SCRIPT"
echo "  - 日志位置: $LOG_DIR/daily_YYYYMMDD.log"
echo ""
echo "查看当前定时任务:"
echo "  crontab -l"
echo ""
echo "手动测试运行:"
echo "  cd \"$SCRIPT_DIR\" && python3 fetch_daily_news.py"
echo ""
echo "卸载定时任务:"
echo "  crontab -e  (然后删除相关行)"
echo ""
echo "========================================"
