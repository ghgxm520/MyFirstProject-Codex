from fastapi import APIRouter, HTTPException, Request

from app.schemas.payment import PaymentCreate, PaymentRead
from app.services.payment_service import PaymentService

router = APIRouter()


@router.post("/orders", response_model=PaymentRead)
async def create_payment_order(payload: PaymentCreate) -> PaymentRead:
    """创建支付订单，支持打赏、单篇购买、会员办理。"""
    return await PaymentService().create_order(payload)


@router.post("/callback/{channel}")
async def payment_callback(channel: str, request: Request) -> dict:
    """处理支付回调：签名校验 + 订单状态更新 + 权限激活。"""
    callback_data = await request.json()
    verified = PaymentService().verify_callback_signature(channel=channel, data=callback_data)
    if not verified:
        raise HTTPException(status_code=400, detail="支付回调签名校验失败")

    await PaymentService().activate_permission(callback_data)
    return {"status": "success"}
