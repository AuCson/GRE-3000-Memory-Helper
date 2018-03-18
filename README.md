# GRE-3000-Memory-Helper
将《GRE再要你命3000词》中的例句按照规则提取改编，辅助单词记忆。

usage：
> python manage.py runserver 0.0.0.0:8000

即从所有本机IP进入服务器，默认url为

请通过[host]/verbal?lid=[list ID]&uid=[unit ID] 访问。不指定[list ID]会响应404.


Tech:
1. static/data.json 原始数据为知名论坛bbs.zhan.com下载的《再要你命3000》。通过在线PDF转TXT解析并通过简单的规则结构化。按照源文件的说明，请不要用于商业用途。
2. templates 几乎摘抄至bootstrap官方样例

> 没有什么软件是CS的同学找不到的；如果有，就自己写一个
