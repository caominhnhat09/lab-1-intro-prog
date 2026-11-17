
import csv
from pathlib import Path
from collections import Counter

import matplotlib.pyplot as plt


PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = PROJECT_DIR / "parser" / "data" / "cleaned_data.csv"

OUTPUT_DIR = PROJECT_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_data():
    with open(DATA_FILE, encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def plot_complaints(records):
    counts = Counter(
        row["complaint_type"]
        for row in records
        if row["complaint_type"]
    )

    top = counts.most_common(10)

    labels = [item[0] for item in top]
    values = [item[1] for item in top]

    plt.figure(figsize=(12, 6))
    plt.bar(labels, values)

    plt.title("Top 10 Complaint Types")
    plt.xlabel("Complaint Type")
    plt.ylabel("Number of Requests")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "complaint_types.png")
    plt.close()


def plot_agencies(records):
    counts = Counter(
        row["agency"]
        for row in records
        if row["agency"]
    )

    top = counts.most_common(10)

    labels = [item[0] for item in top]
    values = [item[1] for item in top]

    plt.figure(figsize=(10, 6))
    plt.barh(labels, values)

    plt.title("Top 10 Agencies")
    plt.xlabel("Number of Requests")
    plt.ylabel("Agency")

    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "agencies.png")
    plt.close()


def plot_status(records):
    counts = Counter(
        row["status"]
        for row in records
        if row["status"]
    )

    plt.figure(figsize=(8, 6))

    plt.pie(
        counts.values(),
        labels=counts.keys(),
        autopct="%1.1f%%"
    )

    plt.title("Request Status Distribution")

    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "status_distribution.png")
    plt.close()


def plot_daily_requests(records):
    counts = Counter()

    for row in records:
        date = row["created_date"]

        if date:
            day = date[:10]
            counts[day] += 1

    dates = sorted(counts.keys())
    values = [counts[date] for date in dates]

    plt.figure(figsize=(12, 6))

    plt.plot(dates, values, marker="o")

    plt.title("Daily Requests")
    plt.xlabel("Date")
    plt.ylabel("Number of Requests")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "daily_requests.png")
    plt.close()


def main():
    records = load_data()

    plot_complaints(records)
    plot_agencies(records)
    plot_status(records)
    plot_daily_requests(records)

    print("4 charts created successfully!")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
