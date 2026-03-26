from pydantic import BaseModel, Field


class PaymentCreate(BaseModel):
    """支付订单创建参数。"""

    user_id: int
    scene: str = Field(description="donation / article / membership")
    channel: str = Field(description="wechat / alipay")
    amount_cent: int = Field(gt=0)


class PaymentRead(BaseModel):
    """支付订单返回结构。"""

    order_id: int
    pay_url: str
    status: str
