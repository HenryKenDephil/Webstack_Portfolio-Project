from django.db import models
from django.core.exceptions import ObjectDoesNotExist

#creating custom model fields
#use PositiveIntegerField to specify order for objects

class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields = None, *args, **kwargs):
        self.for_fields = for_fields
        super().__title__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance,  self.attname) is None:
            #if no current value
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    #filter objects with same filed values
                    query = {field: getattr(model_instance, field)\
                             for field in self.for_fields}
                    qs = qs.filter(**query)

                #accessing order of the last objects

                last_object = qs.latest(self.attname)
                value = last_object.order + 1 

            except ObjectDoesNotExist as e:
                value = 0

            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)
