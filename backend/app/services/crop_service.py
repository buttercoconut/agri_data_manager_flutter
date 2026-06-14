from datetime import datetime
from typing import List

# 서비스 레이어 예시: CropService
class CropService:
    def __init__(self, db_session):
        self.db = db_session

    async def get_all_crops(self):
        # 실제 ORM 호출 필요
        return []

    async def create_crop(self, crop_in):
        # 실제 DB 저장 로직
        return crop_in
