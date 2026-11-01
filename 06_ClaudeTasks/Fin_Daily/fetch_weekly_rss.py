#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RSS 订阅周报生成系统
从 LingoWhale 等 RSS 源抓取内容，生成周报
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Dict
from collections import defaultdict
import feedparser
from credentials import load_config

# Playwright 用于处理需要登录的网站
try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    print("警告: playwright 未安装，无法处理需要登录的网站")
    print("安装方法: pip install playwright && playwright install")

class RSSItem:
    """RSS 条目类"""
    def __init__(self, title: str, link: str, published: str, summary: str = "", source: str = ""):
        self.title = title
        self.link = link
        self.published = published
        self.summary = summary
        self.source = source
        self.categories = []

    def __repr__(self):
        return f"RSSItem({self.title[:30]}..., {self.published})"

class RSSWeeklyFetcher:
    """RSS 周报抓取器"""

    def __init__(self, config_path: str = "config.json"):
        """初始化抓取器"""
        self.config = load_config(config_path)

        self.categories_keywords = self.config['categories']
        self.output_config = self.config['output']
        self.rss_config = self.config.get('rss', {})

        self.all_items = []

    def load_cookies(self, cookie_file: str = 'lingowhale_cookies.json') -> list:
        """加载保存的 cookies"""
        if os.path.exists(cookie_file):
            with open(cookie_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def fetch_lingowhale_rss(self, username: str = None, password: str = None, use_cookies: bool = True) -> List[RSSItem]:
        """
        抓取 LingoWhale RSS 订阅

        参数:
            username: 用户名（如果需要登录）
            password: 密码（如果需要登录）
            use_cookies: 是否使用保存的 cookies（默认 True）
        """
        items = []
        username = username or self.rss_config.get('lingowhale_username')
        password = password or self.rss_config.get('lingowhale_password')

        if not PLAYWRIGHT_AVAILABLE:
            print("✗ LingoWhale: 需要安装 playwright")
            print("  运行: pip install playwright && playwright install")
            return items

        # 优先使用 cookies
        cookies = []
        if use_cookies:
            cookies = self.load_cookies()
            if cookies:
                print(f"✓ 加载了 {len(cookies)} 个保存的 cookies")
            else:
                print("⚠ 未找到保存的 cookies，请先运行 login_lingowhale.py 登录")
                if not username or not password:
                    return items

        try:
            with sync_playwright() as p:
                print("启动浏览器访问 LingoWhale...")
                browser = p.chromium.launch(headless=True)
                context = browser.new_context(
                    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                )

                # 如果有 cookies，先加载
                if cookies:
                    context.add_cookies(cookies)

                page = context.new_page()

                # 访问订阅页面
                print("访问订阅频道...")
                page.goto(self.rss_config['lingowhale_url'])
                page.wait_for_load_state('networkidle')

                # 等待内容加载
                page.wait_for_timeout(2000)

                # 提取内容（需要根据实际页面结构调整）
                # 这里是示例代码，需要根据实际 DOM 结构修改
                feed_items = page.query_selector_all('.feed-item, .article-item')

                for item_elem in feed_items:
                    try:
                        title = item_elem.query_selector('.title, h2, h3')
                        link = item_elem.query_selector('a')
                        time = item_elem.query_selector('.time, .date')
                        summary = item_elem.query_selector('.summary, .description')

                        if title:
                            item = RSSItem(
                                title=title.inner_text().strip(),
                                link=link.get_attribute('href') if link else '',
                                published=time.inner_text().strip() if time else '',
                                summary=summary.inner_text().strip() if summary else '',
                                source='LingoWhale'
                            )
                            items.append(item)
                    except Exception as e:
                        continue

                browser.close()
                print(f"✓ LingoWhale: 抓取到 {len(items)} 条内容")

        except Exception as e:
            print(f"✗ LingoWhale 抓取失败: {str(e)}")

        return items

    def fetch_standard_rss(self, feed_url: str, source_name: str) -> List[RSSItem]:
        """抓取标准 RSS 源"""
        items = []
        try:
            feed = feedparser.parse(feed_url)

            for entry in feed.entries:
                item = RSSItem(
                    title=entry.get('title', ''),
                    link=entry.get('link', ''),
                    published=entry.get('published', ''),
                    summary=entry.get('summary', ''),
                    source=source_name
                )
                items.append(item)

            print(f"✓ {source_name}: 抓取到 {len(items)} 条内容")
        except Exception as e:
            print(f"✗ {source_name} 抓取失败: {str(e)}")

        return items

    def categorize_items(self, items: List[RSSItem]) -> Dict[str, List[RSSItem]]:
        """对 RSS 条目进行分类"""
        categorized = defaultdict(list)

        for item in items:
            assigned = False

            # 检查标题和摘要
            text_to_check = item.title + ' ' + item.summary

            for category, keywords in self.categories_keywords.items():
                if any(keyword in text_to_check for keyword in keywords):
                    item.categories.append(category)
                    categorized[category].append(item)
                    assigned = True

            if not assigned:
                categorized['其他'].append(item)

        return categorized

    def generate_weekly_report(self, username: str = None, password: str = None) -> str:
        """生成周报"""
        print(f"\n{'='*60}")
        print(f"开始生成 RSS 周报 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")

        # 抓取 LingoWhale RSS
        self.all_items.extend(self.fetch_lingowhale_rss(username, password))

        # 可以在这里添加其他 RSS 源
        # self.all_items.extend(self.fetch_standard_rss('https://example.com/rss', 'Example'))

        if not self.all_items:
            print("\n警告: 未抓取到任何内容，无法生成周报")
            return None

        # 分类
        categorized = self.categorize_items(self.all_items)

        # 生成文件名
        today = datetime.now()
        week_start = today - timedelta(days=today.weekday())
        filename = f"第{week_start.isocalendar()[1]}周 RSS周报 {week_start.strftime('%m-%d')}.md"

        # 生成内容
        content = self._generate_markdown_content(categorized, today, week_start)

        # 保存文件
        weekly_folder = self.output_config['weekly_folder']
        os.makedirs(weekly_folder, exist_ok=True)
        filepath = os.path.join(weekly_folder, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\n{'='*60}")
        print(f"✓ 周报生成成功: {filepath}")
        print(f"{'='*60}\n")

        return filepath

    def _generate_markdown_content(self, categorized: Dict[str, List[RSSItem]],
                                   date: datetime, week_start: datetime) -> str:
        """生成 Markdown 内容"""
        content = []

        # 标题
        week_num = week_start.isocalendar()[1]
        content.append(f"# 第 {week_num} 周 RSS 周报\n\n")
        content.append(f"> 生成时间: {date.strftime('%Y-%m-%d %H:%M:%S')}\n")
        content.append(f"> 周期: {week_start.strftime('%Y-%m-%d')} - {(week_start + timedelta(days=6)).strftime('%Y-%m-%d')}\n\n")

        # 各分类内容
        category_order = ['地缘政治', '中国政策', '企业动态', '重大事件', '其他']
        category_icons = {
            '地缘政治': '🌍',
            '中国政策': '📋',
            '企业动态': '🏢',
            '重大事件': '🔥',
            '其他': '📰'
        }

        for category in category_order:
            if category in categorized and categorized[category]:
                icon = category_icons.get(category, '📌')
                content.append(f"## {icon} {category}\n\n")

                items = categorized[category][:20]  # 限制数量

                for item in items:
                    content.append(f"### {item.title}\n\n")
                    if item.summary:
                        content.append(f"{item.summary}\n\n")
                    content.append(f"- **来源**: {item.source}\n")
                    content.append(f"- **时间**: {item.published}\n")
                    if item.link:
                        content.append(f"- **链接**: [{item.link}]({item.link})\n")
                    content.append("\n---\n\n")

        # 统计
        content.append("## 📊 统计信息\n\n")
        for category in category_order:
            if category in categorized:
                count = len(categorized[category])
                content.append(f"- {category}: {count} 条\n")
        content.append(f"\n**总计**: {len(self.all_items)} 条内容\n")

        return ''.join(content)

def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description='生成 RSS 周报')
    parser.add_argument('--username', '-u', help='LingoWhale 用户名')
    parser.add_argument('--password', '-p', help='LingoWhale 密码')
    args = parser.parse_args()

    try:
        fetcher = RSSWeeklyFetcher()
        report_path = fetcher.generate_weekly_report(args.username, args.password)
        if report_path:
            print(f"周报已保存至: {report_path}")
            return 0
        else:
            return 1
    except Exception as e:
        print(f"错误: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit(main())
