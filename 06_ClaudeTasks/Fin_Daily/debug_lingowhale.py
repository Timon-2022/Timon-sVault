#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LingoWhale 页面结构调试脚本
"""

try:
    from playwright.sync_api import sync_playwright
    import time

    with sync_playwright() as p:
        print("启动浏览器...")
        browser = p.chromium.launch(headless=False)  # 非无头模式，可以看到浏览器
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )
        page = context.new_page()

        # 访问主页
        print("\n1. 访问主页...")
        page.goto('https://lingowhale.com')
        page.wait_for_load_state('networkidle')
        print(f"当前 URL: {page.url}")
        print(f"页面标题: {page.title()}")

        # 保存截图
        page.screenshot(path="screenshots/01_homepage.png")
        print("截图已保存: screenshots/01_homepage.png")

        # 尝试访问 channels
        print("\n2. 访问 channels 页面...")
        page.goto('https://lingowhale.com/channels')
        page.wait_for_load_state('networkidle')
        time.sleep(2)
        print(f"当前 URL: {page.url}")
        print(f"页面标题: {page.title()}")

        # 查找登录相关元素
        print("\n3. 查找登录相关元素...")

        # 检查是否有登录表单
        login_form = page.locator('form').count()
        print(f"表单数量: {login_form}")

        # 检查输入框
        inputs = page.locator('input').all()
        print(f"\n找到 {len(inputs)} 个输入框:")
        for i, inp in enumerate(inputs[:10]):  # 只显示前10个
            input_type = inp.get_attribute('type') or 'text'
            input_name = inp.get_attribute('name') or ''
            input_id = inp.get_attribute('id') or ''
            input_placeholder = inp.get_attribute('placeholder') or ''
            print(f"  [{i+1}] type={input_type}, name={input_name}, id={input_id}, placeholder={input_placeholder}")

        # 检查按钮
        buttons = page.locator('button').all()
        print(f"\n找到 {len(buttons)} 个按钮:")
        for i, btn in enumerate(buttons[:10]):
            btn_text = btn.inner_text()
            btn_type = btn.get_attribute('type') or ''
            print(f"  [{i+1}] text={btn_text}, type={btn_type}")

        # 检查链接
        links = page.locator('a').all()
        print(f"\n找到 {len(links)} 个链接:")
        for i, link in enumerate(links[:10]):
            href = link.get_attribute('href') or ''
            text = link.inner_text()
            if '登录' in text or '注册' in text or 'login' in href.lower() or 'signin' in href.lower():
                print(f"  [{i+1}] text={text}, href={href}")

        # 保存截图
        page.screenshot(path="screenshots/02_channels.png")
        print("\n截图已保存: screenshots/02_channels.png")

        # 获取页面 HTML
        html = page.content()
        with open('screenshots/page_source.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("页面源码已保存: screenshots/page_source.html")

        print("\n等待 10 秒，您可以手动查看浏览器...")
        time.sleep(10)

        browser.close()
        print("\n完成！")

except ImportError:
    print("错误: 需要安装 playwright")
    print("运行: pip install playwright && playwright install")
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
