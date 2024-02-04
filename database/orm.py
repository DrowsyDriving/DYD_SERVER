from sqlalchemy import Column, String, Integer, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()


class AreaInfo(Base):
    __tablename__ = 'areainfo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    area = Column(String(255), nullable=False, unique=True)
    areacode = Column(String(255), nullable=False)

    @classmethod
    def create(cls, area: str, areacode: str) -> "AreaInfo":
        return cls(
            area=area,
            areacode=areacode,
        )


class AlertInfo(Base):
    __tablename__ = 'alertinfo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    car_number = Column(String(15), nullable=False)
    warning_level = Column(Integer, nullable=False)
    latitude = Column(Numeric(precision=16, scale=13), nullable=False)
    longitude = Column(Numeric(precision=16, scale=13), nullable=False)
    occurrence_time = Column(DateTime, default=datetime.now())

    @classmethod
    def create(
        cls, car_number: str, warning_level: int, latitude: float, longitude: float
    ) -> "AlertInfo":
        return cls(
            car_number=car_number,
            warning_level=warning_level,
            latitude=latitude,
            longitude=longitude,
        )


# ALTER TABLE [테이블명] AUTO_INCREMENT=1;
# id 숫자 변경
# SET @COUNT = 0;
# UPDATE areainfo SET id = @COUNT:=@COUNT+1;
