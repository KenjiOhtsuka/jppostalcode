from model import ZipCodeRecord

class ZipCodeRepository:
    def __init__(self):
        self.data: dict[str, list[ZipCodeRecord]] = {}

    def add(self, record: ZipCodeRecord):
        if record.zipcode not in self.data:
            self.data[record.zipcode] = []
        self.data[record.zipcode].append(record)

    def find(self, zipcode: str):
        return self.data.get(zipcode, [])
