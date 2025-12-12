import argparse
from analyzer.telegram_scraper import get_posts
from analyzer.metrics import compute_metrics
from analyzer.visualization import plot_views_over_time
from analyzer.report import generate_pdf_report

def main():
    parser = argparse.ArgumentParser(description="Offline Telegram Analyzer")
    parser.add_argument("--channel", required=True, help="Telegram channel username or link")
    parser.add_argument("--limit", type=int, default=50, help="Number of posts to fetch")
    args = parser.parse_args()

    print(f"Fetching posts from {args.channel} (limit={args.limit})...")
    df = get_posts(args.channel, limit=args.limit)

    print("Computing metrics...")
    metrics = compute_metrics(df)
    print(metrics)

    print("Generating charts...")
    plot_views_over_time(df)

    print("Generating PDF report...")
    generate_pdf_report(metrics)

    print("Done! Report saved as report.pdf")

if __name__ == "__main__":
    main()
