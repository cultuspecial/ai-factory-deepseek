import json
import argparse
import sys

def crawl_rss_or_api(topic):
    # 模拟真实稳定的数据源接口
    # 在 L4 中，我们会在这里增加对返回状态码的详细记录
    print(f"🔍 Task: {topic}")
    return [
        {"title": f"Industry Insight: {topic}", "link": "https://example.com/1"},
        {"title": f"Market Analysis: {topic}", "link": "https://example.com/2"}
    ]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", default="AI Trends")
    args = parser.parse_args()
    
    data = crawl_rss_or_api(args.topic)
    
    if not data:
        print("Empty data from source.")
        # 注意：此处不 exit(1)，而是允许下游进入“空数据”模式
    
    with open("raw_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
