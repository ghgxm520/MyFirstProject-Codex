<template>
  <el-container>
    <el-header><h2>运营驾驶舱</h2></el-header>
    <el-main>
      <el-row :gutter="16">
        <el-col :span="6"><el-statistic title="日活用户" :value="metrics.dau" /></el-col>
        <el-col :span="6"><el-statistic title="内容热度" :value="metrics.contentHeat" /></el-col>
        <el-col :span="6"><el-statistic title="订阅转化" :value="metrics.conversion" suffix="%" /></el-col>
        <el-col :span="6"><el-statistic title="财务收入(元)" :value="metrics.revenue" /></el-col>
      </el-row>

      <el-table :data="tableData" style="margin-top: 24px">
        <el-table-column prop="title" label="内容标题" />
        <el-table-column prop="status" label="发布状态" />
        <el-table-column prop="updatedAt" label="更新时间" />
      </el-table>
    </el-main>
  </el-container>
</template>

<script setup>
// 驾驶舱核心指标，可通过后端 dashboard API 实时刷新
const metrics = {
  dau: 1280,
  contentHeat: 872,
  conversion: 13.7,
  revenue: 5099
}

const tableData = [
  { title: 'FastAPI 支付回调实践', status: '已发布', updatedAt: '2026-03-26 08:00' },
  { title: 'Vue 3 项目架构心得', status: '草稿', updatedAt: '2026-03-25 22:15' }
]
</script>
