# 慕课网风格个人站点（Vue3 + Element Plus + FastAPI）

## 阶段 1：架构与数据模型设计
### 逻辑思路
1. **用户与权限**：仅保留普通用户 / 永久会员两级，避免权限系统过重。
2. **内容域拆分**：统一 `contents` 表 + `content_type` 枚举覆盖个人心得、技术资源、开源课程。
3. **支付域**：通过 `orders` 记录支付流水，回调时做签名校验并触发权限激活。
4. **数据分析域**：用聚合服务输出驾驶舱指标，后续可替换为实时流式计算。

### 核心代码入口
- FastAPI 应用入口：`backend/app/main.py`
- SQLAlchemy 数据模型：`backend/app/models/entities.py`
- Dashboard 聚合服务：`backend/app/services/dashboard_service.py`

## 阶段 2：后端 API 设计（异步）
### 逻辑思路
1. **内容引擎 API**：列表、创建，支持分类与标签过滤。
2. **支付 API**：订单创建 + 回调接口；回调流程强制验签。
3. **管理 API**：驾驶舱指标输出。

### 核心代码入口
- 内容 API：`backend/app/api/v1/routes_content.py`
- 支付 API：`backend/app/api/v1/routes_payment.py`
- 管理 API：`backend/app/api/v1/routes_admin.py`

## 阶段 3：前端页面与组件（Vue3 + Element Plus）
### 逻辑思路
1. **首页**：`Row/Col + Card` 实现瀑布流卡片感布局（不引入 Tailwind）。
2. **后台驾驶舱**：`Statistic + Table` 展示核心运营数据。
3. **SEO 基础**：`index.html` 补充 description。

### 核心代码入口
- 首页视图：`frontend/src/views/home/HomeView.vue`
- 瀑布流组件：`frontend/src/components/MasonryGrid.vue`
- 管理驾驶舱：`frontend/src/views/admin/AdminDashboard.vue`

## 安全与鲁棒性策略（当前实现 + 下一步）
- 已实现：支付回调签名字段检查示例逻辑。
- 下一步：接入微信/支付宝官方 SDK 公钥验签、幂等更新订单、回调重放防护。
- 下载防护：建议资源下载改为签名短链 + 一次性 token。
- 数据库：推荐 PostgreSQL，后续为 `orders(user_id,status,created_at)` 增加联合索引。

## 本地启动
```bash
# backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# frontend
cd frontend
npm install
npm run dev
```
