from tortoise import fields, models


class File(models.Model):
    uuid = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=250, null=True)
    path = fields.CharField(max_length=250, null=True)
    type = fields.CharField(max_length=15, null=True)

    def __str__(self):
        return f'{self.uuid}'
