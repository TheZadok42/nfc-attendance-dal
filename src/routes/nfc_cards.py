from fastapi import APIRouter

from ..dal.engine import engine
from ..dal.models import BaseNFCCard, NFCCard
from ..dal.tables import nfc_cards

router = APIRouter(tags=['cards'], prefix='/cards')


@router.post('', response_model=NFCCard, status_code=201)
async def create_new_card(card: BaseNFCCard):
    query = nfc_cards.insert().values(**card.dict())
    card_id = await engine.execute(query)
    return dict(id=card_id, **card.dict())
