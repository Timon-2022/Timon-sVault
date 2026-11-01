#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试语鲸网站访问"""

from credentials import load_config

try:
    from playwright.sync_api import sync_playwright

    # 读取配置
    config = load_config('config.json')

    username = config['rss']['lingowhale_username']
    password = config['rss']['lingowhale_password']

    print("启动浏览器...")
    with sync_playwright() as p:
        # 使用无头模式
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )
        page = context.new_page()

        print(f"访问语鲸网站...")
        page.goto('https://lingowhale.com', timeout=30000)
        page.wait_for_load_state('networkidle')

        print(f"当前URL: {page.url}")
        print(f"页面标题: {page.title()}")

        # 查找登录入口
        print("\n查找登录相关元素...")

        # 检查是否有登录按钮
        login_buttons = page.locator('button, a').all()
        login_found = False
        for btn in login_buttons[:20]:
            try:
                text = btn.inner_text().lower()
                if '登录' in text or 'login' in text or '登入' in text:
                    print(f"  找到登录按钮: {text}")
                    login_found = True
                    break
            except:
                pass

        if not login_found:
            print("  未找到明显的登录按钮")

        # 访问 channels 页面
        print("\n访问 channels 页面...")
        page.goto('https://lingowhale.com/channels', timeout=30000)
        page.wait_for_load_state('networkidle')
        print(f"当前URL: {page.url}")

        # 检查是否被重定向到登录页
        if 'login' in page.url.lower() or 'signin' in page.url.lower():
            print("⚠️  需要登录才能访问订阅页面")

        # 查看页面结构
        print("\n页面结构分析...")
        # 保存HTML
        html = page.content()
        with open('debug_lingowhale_full.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"页面HTML已保存到: debug_lingowhale_full.html")

        # 检查是否有RSS相关内容
        if 'rss' in html.lower() or 'feed' in html.lower():
            print("✓ 页面中包含 RSS/Feed 相关内容")
        else:
            print("✗ 页面中未发现 RSS/Feed")

        browser.close()
        print("\n测试完成")

except ImportError:
    print("错误: playwright 未正确安装")
    print("请运行: playwright install")
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
