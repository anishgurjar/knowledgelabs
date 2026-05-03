from datetime import datetime, timedelta
from dateutil import parser
from zoneinfo import ZoneInfo


RAW_TRANSACTIONS = [
    {"id": 1, "invoice_date": "04/05/2026", "amount": 100}, 
    {"id": 2, "invoice_date": "2026-04-06", "amount": 200},
    {"id": 3, "invoice_date": "April 7, 2026 3:30 PM", "amount": 150},
]

PROMOTION = {
    "start": "2026-04-05 00:00",
    "end": "2026-04-10 00:00",
    "timezone": "America/New_York"
}


def parse_invoice_date(date_str: str, invoice_tz: str) -> datetime:

    dt = parser.parse(date_str)
    dt = dt.replace(tzinfo=ZoneInfo(invoice_tz))
    return dt


def normalize_to_utc(dt: datetime) -> datetime:
    return dt.astimezone(ZoneInfo("UTC"))


def is_within_promo(invoice_dt: datetime, promo_start: datetime, promo_end: datetime) -> bool:
    return promo_start <= invoice_dt < promo_end


def process():
    promo_tz = PROMOTION["timezone"]
    
    promo_start_timestamp = datetime.strptime(PROMOTION["start"], "%Y-%m-%d %H:%M")
    promo_start_timestamp = promo_start_timestamp.replace(tzinfo=ZoneInfo(promo_tz))

    promo_start = normalize_to_utc(promo_start_timestamp)

    promo_end_timestamp = datetime.strptime(PROMOTION["end"], "%Y-%m-%d %H:%M")
    promo_end_timestamp = promo_end_timestamp.replace(tzinfo=ZoneInfo(promo_tz))

    promo_end = normalize_to_utc(promo_end_timestamp)

    matched = []

    for txn in RAW_TRANSACTIONS:
        dt = parse_invoice_date(txn["invoice_date"], "America/New_York")
        dt_utc = normalize_to_utc(dt)

        if is_within_promo(dt_utc, promo_start, promo_end):
            matched.append(txn["id"])

    return matched


if __name__ == "__main__":
    print(process())