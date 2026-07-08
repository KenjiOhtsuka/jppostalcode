from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ZipCodeRecord:
    zipcode: str
    prefecture: str
    city: str
    town: str
    address_detail: str | None
    # kana_prefecture: str
    # kana_city: str
    # kana_town: str
    type: str  # "address" or "office"
    office_name: str | None = None
    # office_kana: str | None = None
