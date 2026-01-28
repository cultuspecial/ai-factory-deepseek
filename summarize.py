import datetime
import json
import random

def record_meta(topic, success, fallback, retries, content, tokens=0):
    """
    将运行元数据写入 JSONL 文件，供 GitHub Actions 看板分析
    """
    meta = {
        "timestamp": datetime.datetime.now().isoformat(),
        "topic": topic,
        "llm_success": success,
        "fallback_used": fallback,
        "retry_count": retries,
        "content_length": len(content),
        "total_tokens": tokens, 
        "status": "HEALTHY" if success and not fallback else "DEGRADED"
    }
    
    # 追加模式写入 run_history.jsonl
    with open("run_history.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(meta, ensure_ascii=False) + "\n")

def generate_report():
    """
    你的核心业务逻辑（目前为模拟数据，后续可接入 API）
    """
    topic = "AI Trends"
    content = "这是一份自动生成的 AI 趋势报告。"
    is_success = True
    is_fallback = False
    retries = 0
    
    # 模拟 Token 消耗（实际对接时请改为 API 的 usage.total_tokens）
    actual_tokens = random.randint(500, 2000) 
    
    # 记录到 JSONL 供看板读取
    record_meta(topic, is_success, is_fallback, retries, content, tokens=actual_tokens)
    print(f"✅ 成功记录: {topic}, Tokens: {actual_tokens}")

# --- 必须有下面这两行，Actions 运行 Python 时才会真正干活 ---
if __name__ == "__main__":
    generate_report()
