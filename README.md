# AI 学习助手

一个基于 FastAPI 和 SiliconFlow API 的简单 AI 学习助手。

## 功能

- 生成学习计划
- 拆分任务
- 提供鼓励建议
- 提供简单前端页面交互（ai写的）

## 技术栈

- Python
- FastAPI
- OpenAI 兼容 SDK
- SiliconFlow API
- HTML / CSS / JavaScript

## 运行方式

安装依赖：

```bash
pip install fastapi uvicorn openai python-dotenv

创建.env文件：
```bash
SILICONFLOW_API_KEY=你的key

启动后端：
```bash
uvicorn talk_fastapi_ver2_with_ai_front:app --reload

然后直接用浏览器打开 front2.html。

接口
* /health
* /plan
* /split_task
* /encourage
