import csv
from dataclasses import dataclass
from typing import List

SALES_DATA_FILE = "sales-data.csv"
REPORT_FILE = "sales-report.txt"

@dataclass
class SaleRecord:
    date: str
    product: str
    quantity: int
    price: float


def load_sales_data(filename: str) -> List[SaleRecord]:
    """Load sales records from a CSV file."""
    records: List[SaleRecord] = []
    with open(filename, mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            record = SaleRecord(
                date=row["date"],
                product=row["product"],
                quantity=int(row["quantity"]),
                price=float(row["price"]),
            )
            records.append(record)
    return records


def summarize_sales(records: List[SaleRecord]) -> dict:
    """Compute summary statistics for sales records."""
    total_quantity = sum(record.quantity for record in records)
    total_sales = sum(record.quantity * record.price for record in records)
    return {
        "total_records": len(records),
        "total_quantity": total_quantity,
        "total_sales": total_sales,
    }


def create_report(summary: dict, filename: str) -> None:
    """Write the sales summary report to a text file."""
    recommendation = (
        "Sales look strong across the product line."
        if summary["total_sales"] >= 300
        else "Consider reviewing low-performing products to improve revenue."
    )

    with open(filename, mode="w", encoding="utf-8") as report_file:
        report_file.write(f"Total records: {summary['total_records']}\n")
        report_file.write(f"Total quantity sold: {summary['total_quantity']}\n")
        report_file.write(f"Total sales: ${summary['total_sales']:.2f}\n")
        report_file.write(f"Recommendation: {recommendation}\n")


def main() -> None:
    records = load_sales_data(SALES_DATA_FILE)
    summary = summarize_sales(records)
    create_report(summary, REPORT_FILE)
    print(f"Processed {summary['total_records']} records.")
    print(f"Report written to {REPORT_FILE}.")


if __name__ == "__main__":
    main()
