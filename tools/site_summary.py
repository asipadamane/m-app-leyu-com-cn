SITE_DATA = {
    "name": "乐鱼体育",
    "url": "https://m-app-leyu.com.cn",
    "keywords": ["体育赛事", "即时比分", "电竞投注", "乐鱼体育平台"],
    "tags": ["体育", "游戏", "竞猜", "娱乐"],
    "description": "乐鱼体育提供丰富的体育赛事资讯、即时比分更新及电竞投注服务，覆盖足球、篮球、网球等多个热门项目。"
}

def format_summary(data: dict) -> str:
    """将站点资料格式化为结构化摘要字符串"""
    lines = []
    lines.append("=" * 40)
    lines.append(f"站点名称：{data['name']}")
    lines.append(f"站点网址：{data['url']}")
    lines.append(f"核心关键词：{', '.join(data['keywords'])}")
    lines.append(f"所属标签：{', '.join(data['tags'])}")
    lines.append(f"站点简介：{data['description']}")
    lines.append("=" * 40)
    return "\n".join(lines)

def generate_report(entries: list) -> str:
    """生成多个站点的汇总报告"""
    parts = []
    for i, entry in enumerate(entries, 1):
        header = f"=== 站点 {i} ==="
        part = f"{header}\n{format_summary(entry)}"
        parts.append(part)
    return "\n\n".join(parts)

def demo_single():
    """单站点演示"""
    print(">>> 单站点摘要演示")
    print(format_summary(SITE_DATA))

def demo_multi():
    """多站点演示（使用内置示例）"""
    print(">>> 多站点汇总演示")
    extra_site = {
        "name": "乐鱼体育备用",
        "url": "https://m-app-leyu.com.cn/alt",
        "keywords": ["乐鱼体育", "备用入口", "最新地址"],
        "tags": ["体育", "备用"],
        "description": "乐鱼体育备用访问地址，确保用户顺畅体验。"
    }
    entries = [SITE_DATA, extra_site]
    print(generate_report(entries))

def main():
    print("乐鱼体育站点资料结构化摘要工具")
    print("版本 1.0")
    print()
    demo_single()
    print()
    demo_multi()

if __name__ == "__main__":
    main()