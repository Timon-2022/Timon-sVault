#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LingoWhale 登录工具 - 保存登录凭据
运行此脚本一次，之后可以免密访问
"""

import json
import os

try:
    from playwright.sync_api import sync_playwright
    import time

    def save_cookies(cookies, filename='lingowhale_cookies.json'):
        """保存 cookies 到文件"""
        descriptor = os.open(filename, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(descriptor, 'w', encoding='utf-8') as f:
            os.fchmod(f.fileno(), 0o600)
            json.dump(cookies, f, indent=2)
        print(f"✓ Cookies 已保存到: {filename}")

    def login_and_save():
        """登录并保存 cookies"""
        with sync_playwright() as p:
            print("启动浏览器...")
            browser = p.chromium.launch(headless=False)  # 可视模式，方便调试
            context = browser.new_context(
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            )
            page = context.new_page()

            try:
                # 访问主页
                print("访问 LingoWhale...")
                page.goto('https://lingowhale.com', timeout=30000)
                page.wait_for_load_state('networkidle')

                print("\n请在打开的浏览器窗口中手动完成登录流程")
                print("\n登录成功后，请等待页面加载完成...")
                print("脚本将在 60 秒后自动保存 cookies\n")

                # 等待用户手动登录
                time.sleep(60)

                # 获取 cookies
                cookies = context.cookies()

                if cookies:
                    save_cookies(cookies)
                    print(f"\n成功保存 {len(cookies)} 个 cookies")
                    print("\n现在可以使用 fetch_weekly_rss.py 自动抓取内容了")
                else:
                    print("\n警告: 未获取到 cookies，可能登录失败")

            except Exception as e:
                print(f"错误: {e}")
                import traceback
                traceback.print_exc()
            finally:
                print("\n3 秒后关闭浏览器...")
                time.sleep(3)
                browser.close()

    if __name__ == "__main__":
        import argparse

        parser = argparse.ArgumentParser(description='LingoWhale 登录工具')


        args = parser.parse_args()

        login_and_save()

except ImportError:
    print("错误: 需要安装 playwright")
    print("运行: pip install playwright && playwright install")
