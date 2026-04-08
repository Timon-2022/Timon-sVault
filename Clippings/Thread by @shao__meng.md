---
title: "Thread by @shao__meng"
source: "https://x.com/shao__meng/status/2034562818046103665"
author:
  - "@shao__meng"
published: 2026-03-19
created: 2026-03-22
description:
tags:
  - "clippings"
---
**meng shao** @shao\_\_meng [2026-03-19](https://x.com/shao__meng/status/2034562818046103665)

重读 OpenAI Codex、Anthropic Claude 官方对 Agent Skills 测试评估和提升的文章，以及 @mgechev @itsolelehmann 两位作者的 Skills 测试提升的开源项目，整体重新梳理一下「怎么才能让 Agent Skills 更有效？」  
  
开始前先把参考的四篇文章和开源项目贴在这，感兴趣的朋友可以深入去了解：

1\. Testing Agent Skills Systematically with Evals

https://developers.openai.com/blog/eval-skills…

2\. Improving skill-creator: Test, measure, and refine Agent Skills

https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills…

3\. "Unit tests" for your agent skills

https://github.com/mgechev/skillgrade…

4\. autoresearch-skill

https://github.com/olelehmann100kMRR/autoresearch-skill…  
开始前先把参考的四篇文章和开源项目贴在这，感兴趣的朋友可以深入去了解：

1\. 使用评估系统化测试智能体技能

https://developers.openai.com/blog/eval-skills…

2\. 改进技能创建器：测试、衡量与优化智能体技能

https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills…

3\. 为你的智能体技能设置"单元测试"

https://github.com/mgechev/skillgrade…

4\. 自动研究技能

https://github.com/olelehmann100kMRR/autoresearch-skill…  
  
\-- 实操建议太长不读版本 --  
  
· 为常用的 Skill 写 3-5 条 yes/no 评分标准，这是投入产出比最高的第一步

· 在 eval 集中加入至少一条不应触发的反例，防止 Skill 被过度匹配

· 用确定性检查覆盖硬性要求，用 LLM rubric 覆盖风格要求，分层评估比单一评分更可靠

· 记录每次迭代的变更和结果，这份日志的长期价值超过 Skill 本身  
  
\-- 梳理开始 --  
  
\- 三条核心方法论 -  
  
1\. 先定义 "好"，再写 Skill

OpenAI 的 eval 指南将成功标准分为四类：

· 结果目标：任务是否完成，比如 app 能否运行

· 过程目标：是否按预期路径执行，比如是否调用了正确的 skill

· 风格目标：输出是否符合约定，比如是否用 Tailwind 而非 CSS modules

· 效率目标：是否存在浪费，比如不必要的重复命令、token 消耗过高  
  
Anthropic 进一步区分了两类 Skill：能力增强型（模型本身做不好的事）和偏好编码型（模型能做但需按特定流程执行）。前者随模型进步可能失效，后者更持久但需持续验证保真度。这意味着评估不仅是质量检查，也是判断一个 Skill 是否仍有存在必要的手段。  
  
2\. 确定性检查 + LLM 评分的双层评估

三套工具采用了相同的分层结构：

· 第一层：确定性检查 — 文件是否存在、命令是否执行、输出格式是否正确。速度快、可解释、可复现。Skillgrade 直接输出 JSON 格式的 score + checks，OpenAI 通过解析 JSONL trace 中的 command\_execution 事件实现。  
  
· 第二层：LLM Rubric 评分 — 对风格、流程合规性等定性维度用模型打分。OpenAI 使用 --output-schema 约束输出为可比较的结构化 JSON；Skillgrade 用加权方式将两层分数合并为最终得分（如确定性 70% + LLM rubric 30%）。  
  
关键原则：先用快速的硬性检查定位明确的失败，再用模型评分覆盖模糊的质量维度。  
  
3\. 自动化迭代循环（Autoresearch）

Ole Lehmann 将 Karpathy 的 autoresearch 思路应用到 Skill 优化上，形成了一个闭环：

测试当前 Skill → 评分 → 分析失败点 → 做一个小改动 → 重新测试 → 得分提升则保留，否则回滚 → 重复  
  
这里最有价值的设计决策：

· 评分标准用 yes/no 清单，而非模糊的 1-10 打分，保证一致性（如"标题是否包含具体数字"而非"标题质量如何"）

· 每次只改一个变量，确保归因清晰

· 保留完整变更日志，记录每次尝试的改动、原因和结果，这份日志本身就是可复用的优化知识  
  
Ole Lehmann 的案例：一个 landing page 文案 Skill 从 56% 通过率提升到 92%，4 轮改动中 3 次保留、1 次回滚，全程无人工干预。  
  
\- 最值得关注的方向 -  
  
1\. Skill 触发精度是被严重低估的问题

· Anthropic 和 OpenAI 都强调：SKILL.md 中的 name 和 description 直接决定 Skill 是否被正确调用。

· OpenAI 建议在 eval 集中同时包含正例和反例（should\_trigger=true/false），用来捕捉误触发。

· Anthropic 的 skill-creator 新增了触发描述优化功能，在 6 个公开 Skill 中改善了 5 个的触发准确率。  
  
2\. 评估数据集不需要大，但需要有针对性

· OpenAI 明确建议：10-20 条测试 prompt 足够，关键是覆盖显式调用、隐式调用、带噪声的上下文调用和反例。随着真实失败案例的积累逐步扩展。

· Skillgrade 也推荐"3-5 个精心设计的 task 胜过 50 个粗糙的"。  
  
3\. 评估基础设施正在标准化

· codex exec --json：原生 trace 捕获 + 结构化输出

· Skillgrade：通用评估框架，含 Docker 沙箱

· skill-creator ：Claude 内置 eval 生成 + benchmark + A/B 对比  
  
Skillgrade 的 eval.yaml 格式值得关注：它将 workspace 文件准备、grader 定义、权重分配和 CI 集成统一到一个声明式配置中，降低了门槛。  
  
4\. Skill 可能会演化为纯规格说明

Anthropic 在文章末尾提出了一个方向性判断：随着模型能力提升，SKILL.md 可能从"详细的操作指令"演变为"描述期望结果的规格说明"，由模型自行决定实现路径。而 eval 框架恰好已经在描述"什么是好的结果"——未来 eval 本身可能就是 Skill。

![图像](https://pbs.twimg.com/media/HDw4C8faIAA0vyw?format=jpg&name=large)