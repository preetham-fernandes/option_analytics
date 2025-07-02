# backend/db/models.py

from sqlalchemy import Column, Integer, Float, String, DateTime
from nifty_vix_scraper.backend.db.database import Base
from datetime import datetime

class OptionData(Base):
    __tablename__ = "option_data"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    symbol = Column(String(20), index=True)
    strike_price = Column(Float)
    option_type = Column(String(2))  # "CE" or "PE"
    ltp = Column(Float)

    # Optional: enforce uniqueness to avoid duplicates
    __table_args__ = (
        {'mysql_charset': 'utf8mb4'},
    )
