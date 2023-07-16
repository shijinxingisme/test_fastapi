from tortoise import Model, fields


class Study(Model):
    """数据库中的表 todo """
    id = fields.IntField(pk=True)
    content = fields.CharField(max_length=500)
    created_at = fields.DatetimeField(auto_now_add=True)  # auto_now_add 创建的时候更新
    updated_at = fields.DatetimeField(auto_now=True)  # auto_now 每次修改更新
