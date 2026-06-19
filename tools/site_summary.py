import json
from typing import Dict, List, Optional

SITE_DATA = {
    "name": "爱游戏官方网站",
    "url": "https://officialsite-i-game.com.cn",
    "keywords": ["爱游戏", "游戏平台", "游戏资讯"],
    "tags": ["娱乐", "游戏", "官方"],
    "description": "爱游戏官方平台，提供最新游戏资讯、下载与服务。",
    "language": "zh-CN",
    "category": "游戏门户"
}


def build_summary(data: Dict) -> str:
    summary_parts = [
        f"站点名称：{data.get('name', '未知')}",
        f"URL：{data.get('url', '无')}",
        f"关键词：{', '.join(data.get('keywords', []))}",
        f"标签：{', '.join(data.get('tags', []))}",
        f"说明：{data.get('description', '无')}",
        f"语言：{data.get('language', '未知')}",
        f"分类：{data.get('category', '未分类')}",
    ]
    return "\n".join(summary_parts)


def generate_markdown_summary(data: Dict) -> str:
    lines = [
        f"# {data.get('name', '站点摘要')}",
        "",
        f"- **URL**: [{data['url']}]({data['url']})",
        f"- **关键词**: `{'`, `'.join(data.get('keywords', []))}`",
        f"- **标签**: `{'`, `'.join(data.get('tags', []))}`",
        f"- **描述**: {data.get('description', '')}",
        f"- **语言**: {data.get('language', '')}",
        f"- **分类**: {data.get('category', '')}",
    ]
    return "\n".join(lines)


def to_json(data: Dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def print_summary(summary: str) -> None:
    print("=== 站点摘要 ===")
    print(summary)
    print()


def main() -> None:
    text_summary = build_summary(SITE_DATA)
    print_summary(text_summary)

    md_summary = generate_markdown_summary(SITE_DATA)
    print("=== Markdown 格式 ===")
    print(md_summary)
    print()

    json_output = to_json(SITE_DATA)
    print("=== JSON 输出 ===")
    print(json_output)


if __name__ == "__main__":
    main()