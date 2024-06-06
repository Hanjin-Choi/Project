<template>
  <div>
    <nav class="navbar navbar-expand-lg custom-navbar">
      <div class="container-fluid">
        <RouterLink class="navbar-brand" :to="{ name: 'mainpage' }">
          <img src="@/assets/logo.png" alt="Shin-Han 돈은 다다익선" class="navbar-logo">
        </RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item" v-if="userStore.isAuthenticated">
              <RouterLink class="nav-link" :to="{ name: 'compare' }">예금비교</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'calculate' }">환율계산기</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'map' }">은행지도</RouterLink>
            </li>
            <li class="nav-item" v-if="userStore.isAuthenticated">
              <RouterLink class="nav-link" :to="{ name: 'community-home' }">게시판</RouterLink>
            </li>
            <li v-if="userStore.user !== null && userStore.user.user.is_superuser" class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'category' }">카테고리 생성</RouterLink>
            </li>
          </ul>
          <span v-if="!userStore.isAuthenticated" class="auth-links">
            <RouterLink :to="{ name: 'login' }" class="auth-link">로그인</RouterLink>
            <span class="separator">|</span>
            <RouterLink :to="{ name: 'signup' }" class="auth-link">회원가입</RouterLink>
          </span>
          <span v-else class="auth-links">
            <a @click="logout" class="auth-link">로그아웃</a>
            <span class="separator">|</span>
            <RouterLink :to="{ name: 'profile' }" class="auth-link">마이페이지</RouterLink>
          </span>
        </div>
      </div>
    </nav>
  </div>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/auth'

const userStore = useUserStore()
const router = useRouter()

const logout = function () {
  userStore.logOut()
  setTimeout(() => {
    router.push({ name: 'mainpage' })
  }, 500)
}
</script>

<style scoped>
.custom-navbar {
  background-color: #2c3e50; /* 어두운 블루 그레이 색상 */
  border-bottom: 2px solid #34495e; /* 로고 색상과 어울리는 하단 경계선 */
  padding: 10px 20px;
}

.navbar-logo {
  height: 40px;
}

.nav-link {
  color: #ecf0f1; /* 밝은 회색 텍스트 색상 */
  font-weight: bold;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #bdc3c7; /* 호버 시 더 밝은 회색 */
}

.auth-links {
  display: flex;
  align-items: center;
}

.auth-link {
  color: #ecf0f1; /* 밝은 회색 텍스트 색상 */
  font-weight: bold;
  transition: color 0.3s ease;
  cursor: pointer;
}

.auth-link:hover {
  color: #bdc3c7; /* 호버 시 더 밝은 회색 */
}

.separator {
  color: #ecf0f1; /* 밝은 회색 구분선 */
  margin: 0 10px;
}

a {
  text-decoration: none;
}

.navbar-toggler {
  border-color: rgba(255, 255, 255, 0.1); /* 토글 버튼 경계선 색상 */
}

.navbar-toggler-icon {
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(236, 240, 241, 0.7)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E"); /* 토글 아이콘 색상 */
}

</style>