<template>
  <div class="container community-container mt-4">
    <h1 class="community-title">게시판</h1>
    <div class="community-categories mt-3">
      <ul class="list-group list-group-horizontal">
        <li class="list-group-item">
          <RouterLink :to="{ name: 'community-home' }" class="category-link">전체 게시글</RouterLink>
          <span class="category-separator">|</span>
        </li>
        <li class="list-group-item" v-for="(category, index) in store.categoryList" :key="category.id">
          <RouterLink :to="{ name: 'eachCategory', params: { categoryName: category.name } }" class="category-link">
            {{ category.name }}
          </RouterLink>
          <span v-if="index < store.categoryList.length - 1" class="category-separator">|</span>
        </li>
      </ul>
    </div>
    <div class="text-end mt-3">
      <RouterLink class="btn btn-primary" :to="{ name: 'createPost' }">글쓰기</RouterLink>
    </div>
    <div class="router-view-container mt-4">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { usePostStore } from '@/stores/postStore'

const store = usePostStore()
onMounted(() => {
  store.getCategory()
  store.getPost()
})
</script>

<style scoped>
.community-container {
  background-color: #f5f5f5; /* 밝은 배경색 */
  padding: 20px;
  border-radius: 10px;
}

.community-title {
  color: #2c3e50; /* 텍스트 색상 */
}

.community-categories {
  margin-top: 20px;
}

.list-group-item {
  background-color: transparent;
  border: none;
  padding: 10px 5px; /* 간격 조정 */
}

.category-link {
  color: #2c3e50; /* 기본 링크 색상 */
  font-weight: bold;
  text-decoration: none;
  transition: color 0.3s ease;
}

.category-link:hover {
  color: #3498db; /* 호버 시 파란색 */
}

.category-separator {
  margin: 0 10px; /* 구분자 좌우 간격 조정 */
  color: #2c3e50; /* 구분자 색상 */
}

.router-view-container {
  background-color: #ffffff; /* 흰색 배경 */
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* 그림자 추가 */
  border: 1px solid #dddddd; /* 경계선 추가 */
}

.btn-primary {
  background-color: #3498db; /* 파란색 버튼 */
  border-color: #3498db;
  color: white;
}

.btn-primary:hover {
  background-color: #2980b9;
  border-color: #2980b9;
}
</style>
