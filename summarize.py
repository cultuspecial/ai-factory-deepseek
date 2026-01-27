import datetime

# ... 在 generate_report 逻辑中 ...

def record_meta(topic, success, fallback, retries, content):
    meta = {
        "timestamp": datetime.datetime.now().isoformat(),
        "topic": topic,
        "llm_success": success,
        "fallback_used": fallback,
        "retry_count": retries,
        "content_length": len(content),
        "status": "HEALTHY" if success and not fallback else "DEGRADED"
    }
    with open("run_meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

# 修改后的调用入口逻辑（伪代码示意）
def generate_report():
    # ... 之前的逻辑 ...
    # content, is_success, is_fallback, retries = call_llm_logic()
    # record_meta(topic, is_success, is_fallback, retries, content)
