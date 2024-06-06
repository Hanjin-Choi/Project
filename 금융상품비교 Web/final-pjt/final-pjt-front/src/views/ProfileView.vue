<template>
    <div class="container profile-container mt-4">
      <h1 class="profile-title">{{ username }}님의 Profile</h1>
      <hr>
      <div class="row mt-4">
        <div class="col-2 profile-menu">
          <ul class="list-group list-group-flush">
            <li class="list-group-item">
              <RouterLink :to="{ name: 'profile' }" class="profile-link">프로필</RouterLink>
            </li>
            <li class="list-group-item">
              <RouterLink :to="{ name: 'profile-edit' }" class="profile-link">비밀번호 변경</RouterLink>
            </li>
            <li class="list-group-item">
              <RouterLink :to="{ name: 'portfolio', params: { 'userName': username } }" class="profile-link">포트폴리오 수정</RouterLink>
            </li>
            <li class="list-group-item">
              <RouterLink :to="{ name: 'profile-recommend' }" class="profile-link">상품 추천</RouterLink>
            </li>
          </ul>
        </div>
        <div class="col-10 profile-content border-start">
          <RouterView />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue'
  import { useUserStore } from '@/stores/auth'
  import { RouterLink, RouterView } from 'vue-router'
  import { useFinanceStore } from '@/stores/financeStore'
  
  const userStore = useUserStore()
  const user = ref(userStore.user)
  const username = ref(user.value.user.username)
  
  const store = useFinanceStore()
  
  onMounted(() => {
    store.getFinanceInfo()
    store.getOptionInfo()
  })
  </script>
  
  <style scoped>
  .profile-container {
    background-color: #f5f5f5; /* 밝은 배경색 */
    padding: 20px;
    border-radius: 10px;
  }
  
  .profile-title {
    color: #2c3e50; /* 텍스트 색상 */
  }
  
  .profile-menu {
    padding: 10;
  }
  
  .list-group-item {
    background-color: transparent;
    border: none;
    padding: 10px 0;
  }
  
  .profile-link {
    color: #2c3e50; /* 기본 링크 색상 */
    font-weight: bold;
    text-decoration: none;
    transition: color 0.3s ease;
  }
  
  .profile-link:hover {
    color: #3498db; /* 호버 시 파란색 */
  }
  
  .profile-content {
    background-color: #ffffff; /* 흰색 배경 */
    border-radius: 10px;
    padding: 20px;
    color: #34495e; /* 텍스트 색상 */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  
  hr {
    border: 0;
    height: 1px;
    background: #dddddd; /* 연한 회색 라인 */
  }
  
  .border-start {
    border-left: 1px solid #dddddd; /* 연한 회색 경계선 */
  }
  </style>
  