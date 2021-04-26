class ModelMixin:
    __exclude_fields = []

    def to_dict(self):
        data = {}
        # 序列化逻辑简单，直接获取实例属性即可
        for field in self._meta.fields:
            field_name = field.name
            if field_name not in self.__exclude_fields:
                data[field_name] = getattr(self, field_name)
        return data
