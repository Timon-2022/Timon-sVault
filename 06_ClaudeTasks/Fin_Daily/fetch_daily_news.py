#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
财经每日要闻自动抓取系统
抓取财联社、同花顺等新闻源，生成结构化日报
"""

import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
import re
from typing import List, Dict, Tuple
from collections import defaultdict

class NewsItem:
    """新闻条目类"""
    def __init__(self, title: str, time: str, source: str, link: str = ""):
        self.title = title
        self.time = time
        self.source = source
        self.link = link
        self.categories = []

    def __repr__(self):
        return f"NewsItem({self.title[:20]}..., {self.time}, {self.source})"

class FinancialNewsFetcher:
    """财经新闻抓取器"""

    def __init__(self, config_path: str = "config.json"):
        """初始化抓取器"""
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)

        self.news_sources = self.config['news_sources']
        self.categories_keywords = self.config['categories']
        self.output_config = self.config['output']

        # 设置请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

        self.all_news = []

    def fetch_cailian_news(self) -> List[NewsItem]:
        """抓取财联社电报快讯"""
        news_list = []
        try:
            url = self.news_sources['财联社']
            response = requests.get(url, headers=self.headers, timeout=10)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')

            # 财联社每条新闻在一个大的div容器中
            news_containers = soup.select('div.p-t-20.p-b-20')

            for container in news_containers[:50]:  # 限制抓取数量
                try:
                    # 查找新闻内容
                    content_box = container.find('div', class_='telegraph-content-box')
                    if not content_box:
                        continue

                    # 时间在 telegraph-time-box 中
                    time_elem = content_box.find('span', class_='telegraph-time-box')
                    if not time_elem:
                        continue

                    time_str = time_elem.get_text(strip=True)

                    # 获取新闻内容
                    content_elem = time_elem.find_next_sibling('span')
                    if not content_elem:
                        continue

                    # 提取完整文本
                    full_text = content_elem.get_text(strip=True)

                    # 提取标题（通常在 strong 标签中）
                    title_elem = content_elem.find('strong')
                    title = title_elem.get_text(strip=True) if title_elem else full_text[:50]

                    # 提取详情链接
                    detail_link = "https://www.cls.cn/telegraph"
                    # 在底部找评论链接，从中提取detail ID
                    comment_links = container.select('a[href*="/detail/"]')
                    if comment_links:
                        detail_path = comment_links[0].get('href', '')
                        if detail_path:
                            detail_link = f"https://www.cls.cn{detail_path}"

                    if full_text and len(full_text) > 10:
                        news = NewsItem(
                            title=title,
                            time=time_str,
                            source="财联社",
                            link=detail_link
                        )
                        # 将完整内容保存为摘要
                        news.summary = full_text
                        news_list.append(news)
                except Exception as e:
                    continue

            print(f"✓ 财联社: 抓取到 {len(news_list)} 条新闻")
        except Exception as e:
            print(f"✗ 财联社抓取失败: {str(e)}")

        return news_list

    def fetch_sina_news(self) -> List[NewsItem]:
        """抓取新浪财经滚动新闻"""
        news_list = []
        try:
            url = self.news_sources['新浪财经']
            response = requests.get(url, headers=self.headers, timeout=10)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')

            # 新浪财经滚动新闻列表
            items = soup.select('div.list_009 li, ul.list_009 li')

            for item in items[:50]:
                try:
                    time_elem = item.find('span', class_='c_time')
                    title_elem = item.find('a')

                    if time_elem and title_elem:
                        time_str = time_elem.get_text(strip=True)
                        title = title_elem.get_text(strip=True)
                        link = title_elem.get('href', '')

                        if title and len(title) > 10:
                            news = NewsItem(
                                title=title,
                                time=time_str,
                                source="新浪财经",
                                link=link
                            )
                            news_list.append(news)
                except Exception as e:
                    continue

            print(f"✓ 新浪财经: 抓取到 {len(news_list)} 条新闻")
        except Exception as e:
            print(f"✗ 新浪财经抓取失败: {str(e)}")

        return news_list

    def _is_time_in_range(self, time_str: str) -> bool:
        """判断时间是否在目标范围内（前一日18:00至今日08:00）"""
        try:
            # 尝试解析不同的时间格式
            now = datetime.now()
            today = now.date()
            yesterday = today - timedelta(days=1)

            # 解析时间字符串（格式：HH:MM 或 MM-DD HH:MM）
            if ':' in time_str:
                parts = time_str.split()
                if len(parts) == 2:  # MM-DD HH:MM
                    date_part, time_part = parts
                    month, day = map(int, date_part.split('-'))
                    hour, minute = map(int, time_part.split(':'))
                    news_datetime = datetime(now.year, month, day, hour, minute)
                else:  # HH:MM
                    hour, minute = map(int, time_str.split(':'))
                    # 根据小时判断日期
                    if hour >= 18:
                        news_datetime = datetime.combine(yesterday, datetime.min.time()).replace(hour=hour, minute=minute)
                    else:
                        news_datetime = datetime.combine(today, datetime.min.time()).replace(hour=hour, minute=minute)

                # 判断是否在范围内
                start_time = datetime.combine(yesterday, datetime.min.time()).replace(hour=18, minute=0)
                end_time = datetime.combine(today, datetime.min.time()).replace(hour=8, minute=0)

                return start_time <= news_datetime <= end_time
        except Exception as e:
            pass

        return True  # 如果无法解析时间，默认保留

    def categorize_news(self, news_list: List[NewsItem]) -> Dict[str, List[NewsItem]]:
        """对新闻进行分类"""
        categorized = defaultdict(list)

        for news in news_list:
            assigned = False

            # 检查每个分类的关键词
            for category, keywords in self.categories_keywords.items():
                if any(keyword in news.title for keyword in keywords):
                    news.categories.append(category)
                    categorized[category].append(news)
                    assigned = True

            # 如果没有匹配任何分类，放入"其他"
            if not assigned:
                categorized['其他'].append(news)

        return categorized

    def fetch_all_news(self):
        """抓取所有新闻源"""
        print(f"\n{'='*60}")
        print(f"开始抓取财经新闻 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")

        # 抓取各个新闻源
        self.all_news.extend(self.fetch_cailian_news())
        self.all_news.extend(self.fetch_sina_news())

        print(f"\n总计抓取: {len(self.all_news)} 条新闻")

        return self.all_news

    def generate_daily_report(self) -> str:
        """生成日报"""
        if not self.all_news:
            self.fetch_all_news()

        # 分类新闻
        categorized = self.categorize_news(self.all_news)

        # 找出最重要的事件（优先级：重大事件 > 地缘政治 > 中国政策）
        top_event = self._find_top_event(categorized)

        # 生成文件名
        today = datetime.now()
        filename = f"{today.strftime('%m-%d')} [{top_event}].md"

        # 生成内容
        content = self._generate_markdown_content(categorized, top_event, today)

        # 保存文件
        daily_folder = self.output_config['daily_folder']
        os.makedirs(daily_folder, exist_ok=True)
        filepath = os.path.join(daily_folder, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\n{'='*60}")
        print(f"✓ 日报生成成功: {filepath}")
        print(f"{'='*60}\n")

        return filepath

    def _find_top_event(self, categorized: Dict[str, List[NewsItem]]) -> str:
        """找出最重要的事件作为标题"""
        # 优先级：重大事件 > AI科技 > 中国政策 > 企业动态 > 地缘政治
        priority_categories = ['重大事件', 'AI科技', '中国政策', '企业动态', '地缘政治']

        for category in priority_categories:
            if category in categorized and categorized[category]:
                # 取该分类的第一条新闻，提取关键词
                title = categorized[category][0].title
                # 简化标题（取前15个字符）
                return title[:15] + ('...' if len(title) > 15 else '')

        # 如果没有找到，使用默认标题
        return "财经要闻"

    def _generate_markdown_content(self, categorized: Dict[str, List[NewsItem]],
                                   top_event: str, date: datetime) -> str:
        """生成 Markdown 格式的内容"""
        content = []

        # 标题
        content.append(f"# {date.strftime('%m-%d')} {top_event}\n\n")
        content.append(f"> 抓取时间: {date.strftime('%Y-%m-%d %H:%M:%S')}\n")
        content.append(f"> 新闻范围: {(date - timedelta(days=1)).strftime('%m-%d')} 18:00 - {date.strftime('%m-%d')} 08:00\n\n")

        # 各分类内容
        category_order = ['重大事件', 'AI科技', '中国政策', '企业动态', '地缘政治', '其他']
        category_icons = {
            '重大事件': '🔥',
            'AI科技': '🤖',
            '中国政策': '📋',
            '企业动态': '🏢',
            '地缘政治': '🌍',
            '其他': '📰'
        }

        for category in category_order:
            if category in categorized and categorized[category]:
                icon = category_icons.get(category, '📌')
                content.append(f"## {icon} {category}\n\n")

                # 限制每个分类的条目数量
                max_items = self.output_config['max_items_per_category']
                if category == '其他':
                    max_items = self.output_config['max_others']

                news_items = categorized[category][:max_items]

                for news in news_items:
                    # 新格式：标题 + 摘要（如有） + 链接
                    content.append(f"### {news.title}\n\n")

                    # 如果有摘要且不等于标题，显示摘要
                    if hasattr(news, 'summary') and news.summary and news.summary != news.title:
                        # 移除标题部分，只保留核心内容
                        summary = news.summary
                        if news.title in news.summary:
                            summary = news.summary.replace(news.title, '').strip()
                        # 限制摘要长度
                        if len(summary) > 200:
                            summary = summary[:200] + "..."
                        if summary:
                            content.append(f"{summary}\n\n")

                    content.append(f"- **时间**: {news.time}\n")
                    content.append(f"- **来源**: {news.source}\n")
                    content.append(f"- **链接**: [{news.link}]({news.link})\n\n")
                    content.append("---\n\n")

        # 统计信息
        content.append("## 📊 统计信息\n\n")
        for category in category_order:
            if category in categorized:
                count = len(categorized[category])
                content.append(f"- {category}: {count} 条\n")
        content.append(f"\n**总计**: {len(self.all_news)} 条新闻\n")

        return ''.join(content)

def main():
    """主函数"""
    try:
        fetcher = FinancialNewsFetcher()
        report_path = fetcher.generate_daily_report()
        print(f"日报已保存至: {report_path}")
        return 0
    except Exception as e:
        print(f"错误: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit(main())
