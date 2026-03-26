<template>
  <el-container>
    <el-header>
      <h2>个人知识站点</h2>
    </el-header>
    <el-main>
      <MasonryGrid :contents="mockContents" />
    </el-main>
  </el-container>
</template>

<script setup>
import MasonryGrid from '../../components/MasonryGrid.vue'

// 模拟首页内容数据，后续可替换为真实 API 请求
const mockContents = [
  { id: 1, title: 'FastAPI 支付回调实践', summary: '解析异步支付回调验签流程。', content_type: '技术资源', tags: ['FastAPI', '支付'] },
  { id: 2, title: 'Vue 3 项目架构心得', summary: '从组件分层到可维护性演进。', content_type: '个人心得', tags: ['Vue3', '架构'] },
  { id: 3, title: '开源课程：全栈实战', summary: '手把手实现知识付费平台。', content_type: '开源课程', tags: ['课程', '全栈'] }
]
</script>
