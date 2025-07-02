# backend/db/insert_data.py

from nifty_vix_scraper.backend.db.database import engine, SessionLocal
from nifty_vix_scraper.backend.db.models import OptionData, Base

# Step 1: Create tables (only runs if not already created)
Base.metadata.create_all(bind=engine)

# Step 2: Insert a test row
def insert_sample():
    session = SessionLocal()
    try:
        new_data = OptionData(
            symbol="NIFTY",
            strike_price=25600,
            option_type="CE",
            ltp=170.7
        )
        session.add(new_data)
        session.commit()
        print("✅ Data inserted successfully")
    except Exception as e:
        print(f"❌ Error: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    insert_sample()
