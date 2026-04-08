#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试新闻抓取"""

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

print("=" * 60)
print("测试财联社")
print("=" * 60)
try:
    url = "https://www.cls.cn/telegraph"
    response = requests.get(url, headers=headers, timeout=10)
    response.encoding = 'utf-8'
    print(f"状态码: {response.status_code}")
    print(f"内容长度: {len(response.text)}")

    soup = BeautifulSoup(response.text, 'lxml')

    # 尝试不同的选择器
    selectors = [
        ('div.telegraph-item', 'telegraph-item'),
        ('div[class*="telegraph"]', 'class包含telegraph'),
        ('div.item', 'item'),
        ('li', 'li标签'),
    ]

    for selector, desc in selectors:
        items = soup.select(selector)
        print(f"\n{desc} ({selector}): 找到 {len(items)} 个")
        if items:
            print(f"  第一个元素: {str(items[0])[:200]}...")
            break

    # 保存HTML用于调试
    with open('debug_cailian.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("\n✓ HTML已保存到 debug_cailian.html")

except Exception as e:
    print(f"✗ 错误: {e}")

print("\n" + "=" * 60)
print("测试同花顺")
print("=" * 60)
try:
    url = "https://news.10jqka.com.cn/realtimenews/"
    response = requests.get(url, headers=headers, timeout=10)
    response.encoding = 'gbk'
    print(f"状态码: {response.status_code}")
    print(f"内容长度: {len(response.text)}")

    soup = BeautifulSoup(response.text, 'lxml')

    selectors = [
        ('div.item', 'item'),
        ('div[class*="news"]', 'class包含news'),
        ('ul.news_list li', 'news_list li'),
        ('li', 'li标签'),
    ]

    for selector, desc in selectors:
        items = soup.select(selector)
        print(f"\n{desc} ({selector}): 找到 {len(items)} 个")
        if items:
            print(f"  第一个元素: {str(items[0])[:200]}...")
            break

    with open('debug_tonghuashun.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("\n✓ HTML已保存到 debug_tonghuashun.html")

except Exception as e:
    print(f"✗ 错误: {e}")

print("\n" + "=" * 60)
print("请查看 debug_*.html 文件了解网页结构")
print("=" * 60)
