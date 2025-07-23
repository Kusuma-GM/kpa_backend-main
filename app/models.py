from sqlalchemy import Column, Integer, String, Date, JSON
from .database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, nullable=False)
    submitted_by = Column(String, nullable=False)
    submitted_date = Column(Date, nullable=False)
    fields = Column(JSON, nullable=False)

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"

    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, nullable=False)
    inspection_by = Column(String, nullable=False)
    inspection_date = Column(Date, nullable=False)
    bogie_details = Column(JSON, nullable=False)
    bogie_checksheet = Column(JSON, nullable=False)
    bmbc_checksheet = Column(JSON, nullable=False)