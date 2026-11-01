# 财经任务的登录配置

`config.json` 仅保存公开设置，不保存账号、密码、Cookie 或 API Key。

语鲸登录使用 `python3 login_lingowhale.py`，在打开的浏览器中手动完成登录。
脚本不会打印账号密码；生成的 `lingowhale_cookies.json` 仅供本机使用，权限为 600，且已被 Git 忽略。

需要由运行环境提供账号密码时，使用 `LINGOWHALE_USERNAME` 和 `LINGOWHALE_PASSWORD`。
`fetch_weekly_rss.py` 只在内存中读取这些值，不写回配置，也不会回退到旧配置中的明文凭据。
优先使用已授权的本机 Cookie；没有 Cookie 或环境配置时，脚本会提示先登录。

密码曾经进入公开提交的情况下，删除当前文件中的值不能使旧密码失效：需要在语鲸更换密码；若在其他服务复用过，也应分别更换。
已经公开的历史提交需要另行安排清理，不能视为已经撤回所有副本。

离线验证（不访问网站、不执行登录）：

```sh
python3 -m unittest -v test_credentials.py
```
