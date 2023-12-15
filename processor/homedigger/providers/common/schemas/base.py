from pydantic import BaseModel, ConfigDict
from homedigger.core.database.methods import save_model_to_db
from homedigger.providers.common.types.primitives import PrimitiveTypes


class Base(BaseModel):
    
    model_config = ConfigDict(
        from_attributes=True,
    )
    
    @staticmethod
    def _build_orm_objects(data):
        if not data:
            return
        for key, value in data.model_fields.items():
            if not getattr(value, "annotation") in PrimitiveTypes:
                orm_model = Base._build_orm_objects(getattr(data, key))
                setattr(data, key, orm_model)
        return data.__orm_model__(**vars(data))

    @save_model_to_db
    def save(self):
        return Base._build_orm_objects(self)      
