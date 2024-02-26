class MixingLog:
    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'создан объект{self.__class__.__name__} {k}: {v},'
        return object_attributes
