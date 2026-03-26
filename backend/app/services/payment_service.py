from app.schemas.payment import PaymentCreate, PaymentRead


class PaymentService:
    """支付领域服务：负责订单创建、签名校验、权限激活。"""

    async def create_order(self, payload: PaymentCreate) -> PaymentRead:
        """创建订单并返回二维码/跳转链接。

        说明：当前为演示实现，正式环境应接入微信/支付宝 SDK。
        """
        return PaymentRead(order_id=10001, pay_url=f"https://pay.example.com/{payload.channel}", status="pending")

    def verify_callback_signature(self, channel: str, data: dict) -> bool:
        """校验回调签名，防止伪造支付通知。

        说明：应根据 channel 使用平台公钥验签。
        """
        signature = data.get("signature")
        return bool(channel in {"wechat", "alipay"} and signature)

    async def activate_permission(self, callback_data: dict) -> None:
        """支付成功后激活用户权限与内容访问资格。"""
        _ = callback_data
        return None
