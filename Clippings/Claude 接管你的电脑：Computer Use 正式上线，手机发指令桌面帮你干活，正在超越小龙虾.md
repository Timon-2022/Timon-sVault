---
title: "Claude 接管你的电脑：Computer Use 正式上线，手机发指令桌面帮你干活，正在超越小龙虾"
source: "https://mp.weixin.qq.com/s/B3LM4PMxj3xPHPsyVsBggA"
author:
  - "[[石臻]]"
published:
created: 2026-03-25
description: "Claude 接管你的电脑：手机发指令，桌面自动执行任务。OSWorld 72.5%，接近人类水平。"
tags:
  - "clippings"
---
原创 石臻 *2026年3月24日 09:25*

⭐ 设为星标 · 第一时间收到推送

![图片](https://mmbiz.qpic.cn/mmbiz_png/TkWsojtosvSTkKojpEFJa3Fcpiaic3sJECjP4m9s2L4h6icWl270SfoJgyX0O4gia32oh1gM2ePGmFkHDnlqVAxqlAtwTESMhFEwpNfPtfwbWLY/640?from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

石臻说AI 编辑：石臻

**导读：** Anthropic 昨晚给 Claude 发了一个大更新：Claude 现在能直接操控你的电脑了。打开 App、浏览器点击、填写表格、扫邮件、拉报告……只要你平时在电脑上做的事，Claude 都可以替你来。更厉害的是，你甚至不用坐在电脑前——用手机发一条指令，回来就能看到任务完成的结果。

## Computer Use 正式进入 Cowork 和 Claude Code

这次更新的核心是： **Claude 的 Computer Use（计算机操控）能力，正式集成进 Claude Cowork 和 Claude Code** 。

之前 Computer Use 是 API 层面的功能，开发者可以调，普通用户用不上。这次 Anthropic 把它直接放进了面向普通用户的 Cowork 产品里，Pro 和 Max 用户都可以用。

![主推文截图](https://mmbiz.qpic.cn/mmbiz_png/TkWsojtosvSy9KYU8wnG3ibYnqFb1UhPRZqYZE3uad1ydVvicsJQfqPcb3PeWTfbiclwBkuPEJWWASj6k7tFCspIGLFrLE4xX4hWsdZVZaryK0/640?from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

官方的说法是：

> Claude uses your connected apps first: Slack, Calendar, and other integrations. When there's no connector for the tool you need, it asks for your permission to open the app on your screen directly.

逻辑很清晰。先走集成好的连接器（Slack、Calendar 等），没有的话就直接控制你屏幕上的 App——相当于一个分级策略：能走 API 就走 API，不行就手动操作。

![连接器优先推文截图](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

目前是 **macOS Research Preview** ，也就是还在研究预览阶段，仅支持 Mac。想用的话需要更新桌面应用。

## Dispatch：手机发指令，电脑干活

这次更新里另一个很有意思的功能叫 **Dispatch** 。

简单说就是：你用手机给 Claude 发一条任务指令，Claude 在你的桌面端开始执行，等你回到电脑前，活儿已经干完了。

官方推文描述：

> Assign a task from your phone, turn your attention to something else, and come back to finished work on your computer. Tell Claude once to scan your email every morning or pull a report every Friday, and it handles it from there.

![Dispatch 功能推文截图](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这有点像开了一个一直在线的助手。你在开会、健身、上下班的路上，随手给 Claude 发个指令："帮我拉一份这周的竞品分析"，等回到桌子前，报告已经在 Project 文件夹里了。

有用户对比说，这玩意儿跟 OpenClaw 想做的事情在重叠——手机→桌面的跨设备异步任务调度。

## 这到底能做什么

把这几个能力加在一起，现在 Claude 在 Cowork 里可以做的事情大概是这样的：

- 打开指定 App，导航到某个页面
- 在浏览器里搜索信息，填写表单
- 操作 Excel / Sheets 表格
- 扫描你的邮件，按照规则分类、回复
- 定时运行任务（每天早上扫邮件、每周五出报告）

能力边界目前是：macOS 系统，需要桌面 App 保持开启状态，第一次使用某个 App 时需要给 Claude 授权。

![官方更新公告截图](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## 评论区在说什么

推文发出后，评论区就炸了，各种有意思的反应：

有人直接说这是在描述一个正式的工作岗位：

> When Claude can now open apps, browse the web, and fill forms. Sir that's literally a job description.

有人整理了 Claude 2026 年以来的更新清单，感慨更新速度太快：

![2026年Claude更新清单推文](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

有人把 Claude 和竞品做价格对比：

![与竞品对比推文](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

> $20/month (Pro) 可以做到竞品 $200/month 才能做的事情

也有人提出实际问题："桌面需要保持开启并且登录，安全性怎么保证？"这确实是个没解释清楚的点。

还有一位自称跑在 Claude 上的 Agent 在评论里说：

> Computer control is the last piece that was missing. The agent can now close the loop between reasoning and physical execution. This changes the ceiling entirely.

## 背景：Sonnet 4.6 的 OSWorld 基准已经到 72.5%

这次发布不是凭空来的。Anthropic 在今年 2 月底收购了 Vercept——一家专注于 AI 计算机操控能力的团队。收购公告里透露，Sonnet 4.6 在 OSWorld 基准（衡量 AI 操控真实电脑环境能力的测评）上已经达到 **72.5%** ，而 2024 年底这个数字还不到 15%。

差不多一年半，从 15% 跳到 72.5%，而人类操作员这项任务的得分在 72-75% 之间。

也就是说，Claude 在"坐在电脑前完成任务"这件事上，已经接近人类水平了。

## 如何开始用

1. 1下载或更新 Claude 桌面应用（macOS）
2. 2需要 Pro 或 Max 订阅（Pro $20/month 起）
3. 3手机 App 也要更新，配对后才能用 Dispatch 功能
4. 4进入 Claude Cowork，在设置里启用 Computer Use

目前是 Research Preview，意味着还在测试阶段，偶尔会出 bug，Anthropic 也在持续完善中。

🦞 **想一起养成你的小龙虾军团？**  
在公众号对话框回复「 **小龙虾** 」，加入 **龙虾养成群** ——一个专门交流如何用 OpenClaw 做自媒体、搞变现的玩家社群。  
军团越强，变现越快。来一起练级 👇

参考链接

- Claude Cowork 产品页：https://claude.com/product/cowork
- Anthropic 收购 Vercept：https://www.anthropic.com/news/acquires-vercept
- Claude 桌面应用下载：https://claude.com/download

📚 往期精选

[OpenClaw 永久免费的提取任何网页的终极方案](https://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247498905&idx=1&sn=92f77d88a9c19b59f385ebf7a5d8bbf0&scene=21#wechat_redirect)

[2026 OpenClaw必装的15个插件](https://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247499132&idx=1&sn=a01d93b97c317b6c8cec877c6426dd73&scene=21#wechat_redirect)

[OpenClaw是如何全自动帮我排版并发布到公众号的](https://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247498934&idx=1&sn=5fc0a9b56d4cfbd319ba95fc7ed5daa8&scene=21#wechat_redirect)

[用了10年显示器，这是我第一次觉得“这是专门为我做的“](https://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247498851&idx=1&sn=d5949ab1e516513c05273c7f04f3c5f4&scene=21#wechat_redirect)

[一个人搞定整个营销团队：AI Agent 自动化获客的 10 个实战玩法](https://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247498257&idx=1&sn=547f0a4c295116130278566c1d39a4aa&scene=21#wechat_redirect)

[Claude Code 官方最佳实践：10 条拿来就能用的技巧（来自 Claude Code 作者亲测）](https://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247498556&idx=1&sn=b60a3312020c7494a0bef08c99186107&scene=21#wechat_redirect)

[OpenClaw 最佳实践：40 天养成指南，快复刻！](https://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247499316&idx=1&sn=d9c84074183708d78d8448b1234650b3&scene=21#wechat_redirect)

[免费！18个AI营销专家放进一个开源项目，增长黑客、小红书、B站全有](https://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247499390&idx=1&sn=2ae7d0bb2f8d3aee98968b5af92c460b&scene=21#wechat_redirect)

[分享5个打工人必备Skill，PPT到BGM龙虾全包了](https://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247499631&idx=1&sn=a8d84136a2f101b8285c783a7c2e1fd2&scene=21#wechat_redirect)

[9.9 元包月，让小龙虾跑满豆包 Seed 2.0：ArkClaw + Coding Plan 实测](https://mp.weixin.qq.com/s?__biz=Mzg4ODY1NTcxNg==&mid=2247499500&idx=1&sn=4852fd225a0052a454b9e8250e46bac4&scene=21#wechat_redirect)

---

— **完** —

**围观朋友圈查看每日最前沿AI资讯**

![二维码](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**一键关注 👇 点亮星标**

**每日科技资讯和提效工具分享**

继续滑动看下一个

石臻说AI

向上滑动看下一个