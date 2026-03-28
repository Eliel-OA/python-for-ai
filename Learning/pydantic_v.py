# from pydantic import BaseModel, ValidationError, Field, ConfigDict, field_serializer
# from typing import Union
# from datetime import datetime, timezone

# class Person(BaseModel):
#     model_config = ConfigDict(populate_by_name=True)
#     first_name: str | None = Field(alias="firstName", default=None)
#     last_name: str = Field(alias="lastName")
    

# # class Model(BaseModel):
# #     numbers: list[int] = []
    
# # m1 = Model()
# # m2 = Model()


# class Log(BaseModel):
#     dt: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))
#     message: str

# log1 = Log(message="Baddie Betty Boop")
# log2 = Log(message="Baddie Betty Boop - v2")

# class Model(BaseModel):
#     number: float
    
#     @field_serializer("number")
#     def serialize_float(self, value):
#         return round(value,2)
    
# m = Model(number=1/3)
# print(m.model_dump())
# print(m.model_dump_json())
        
print(2722/5)