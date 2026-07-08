from model import ZipCodeRecord

class KenAllAdapter:
    def adapt(self, row):
        return ZipCodeRecord(
            zipcode=row[2],
            prefecture=row[6],
            city=row[7],
            town=row[8],
            address_detail=None,
            # kana_prefecture=row[3],
            # kana_city=row[4],
            # kana_town=row[5],
            type="address"
        )

class JigyosyoAdapter:
    def adapt(self, row):
        return ZipCodeRecord(
            zipcode=row[7],
            prefecture=row[3],
            city=row[4],
            town=row[5],
            address_detail=row[6],
            # kana_prefecture=row[0],
            # kana_city=row[1],
            # kana_town=row[2],
            type="office",
            office_name=row[2],
            # office_kana=row[9]
        )
