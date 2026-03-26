<template>
  <el-row :gutter="16" class="masonry-grid">
    <el-col
      v-for="item in contents"
      :key="item.id"
      :xs="24"
      :sm="12"
      :md="8"
      :lg="6"
      class="masonry-col"
    >
      <el-card shadow="hover" class="content-card">
        <template #header>
          <div class="card-header">
            <span>{{ item.title }}</span>
            <el-tag size="small">{{ item.content_type }}</el-tag>
          </div>
        </template>
        <p>{{ item.summary }}</p>
        <div class="tag-list">
          <el-tag v-for="tag in item.tags" :key="tag" size="small" type="info">{{ tag }}</el-tag>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script setup>
defineProps({
  // 内容卡片数据，供首页瀑布流展示
  contents: {
    type: Array,
    default: () => []
  }
})
</script>

<style scoped>
.masonry-col {
  margin-bottom: 16px;
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.tag-list {
  margin-top: 12px;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}
</style>
