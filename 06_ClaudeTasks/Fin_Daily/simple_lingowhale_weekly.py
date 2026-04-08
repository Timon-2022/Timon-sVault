#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化版语鲸周报 - 暂时说明
由于语鲸网站需要登录且是动态加载，暂时生成一个说明文档
"""

import json
from datetime import datetime, timedelta
import os

def generate_placeholder_weekly():
    """生成占位周报，说明语鲸功能待完善"""

    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())
    week_num = week_start.isocalendar()[1]

    # 创建目录
    weekly_folder = "Weekly"
    os.makedirs(weekly_folder, exist_ok=True)

    filename = f"第{week_num}周 RSS周报 {week_start.strftime('%m-%d')}.md"
    filepath = os.path.join(weekly_folder, filename)

    content = f"""# 第 {week_num} 周 RSS 周报

> 生成时间: {today.strftime('%Y-%m-%d %H:%M:%S')}
> 周期: {week_start.strftime('%Y-%m-%d')} - {(week_start + timedelta(days=6)).strftime('%Y-%m-%d')}

## 📝 功能说明

语鲸（LingoWhale）RSS 订阅周报功能正在开发中。

### 现有配置

- **账号**: 18810213016
- **订阅地址**: https://lingowhale.com/channels

### 待完善功能

1. **登录机制**: 语鲸需要登录才能访问订阅内容
2. **内容抓取**: 页面采用动态加载，需要等待JavaScript执行
3. **数据解析**: 需要识别RSS订阅项的具体结构

### 临时解决方案

**方案一：手动导出（推荐）**
1. 在浏览器中登录 https://lingowhale.com/channels
2. 查看是否有导出/RSS订阅链接功能
3. 如果有RSS feed URL，可以直接配置到系统中

**方案二：使用浏览器插件**
1. 安装RSS订阅管理插件（如Feedly、Inoreader）
2. 订阅语鲸提供的RSS源
3. 定期手动整理到笔记中

**方案三：API接口（如果提供）**
- 联系语鲸官方，询问是否提供API接口
- 使用API直接获取订阅内容

### 现有日报功能

目前系统的**日报功能已完善**，每天9:05自动抓取：
- 🤖 AI科技
- 🔥 重大事件
- 📋 中国政策
- 🏢 企业动态
- 🌍 地缘政治

查看今日日报：`Daily/` 文件夹

---

## 💡 建议

由于语鲸RSS抓取技术复杂，建议：

1. **优先使用日报功能** - 已完全可用，涵盖主要财经新闻
2. **手动补充语鲸内容** - 每周花10分钟从语鲸复制重要内容到Obsidian
3. **等待功能完善** - 后续会继续优化语鲸自动抓取

如需技术支持，请提供：
- 语鲸网站的实际截图
- 是否有RSS feed URL
- 是否有API文档

---

_自动生成时间: {today.strftime('%Y-%m-%d %H:%M:%S')}_
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ 周报说明文档已生成: {filepath}")
    return filepath

if __name__ == "__main__":
    generate_placeholder_weekly()
