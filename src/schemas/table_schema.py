from config import ma, db


class TableSchema(ma.Schema):
    class Meta:
        fields = ('id', 'number')
        ordered = True