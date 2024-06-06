<template>
  <div class="container mt-4 detail-container">
    <h1 style="color:#2c3e50;">정기예금 상세</h1>
    <div class="container p-5 detail-content">
      <div class="row detail-row">
        <div class="col-2 p-2">
          <strong>공시 제출일</strong>
        </div>
        <div class="col p-2">
          <p>{{ product.dcls_month }}</p>
        </div>
      </div>
      <div class="row detail-row">
        <div class="col-2 p-2">
          <strong>금융회사명</strong>
        </div>
        <div class="col p-2">
          <p>{{ product.kor_co_nm }}</p>
        </div>
      </div>
      <div class="row detail-row">
        <div class="col-2 p-2">
          <strong>상품명</strong>
        </div>
        <div class="col p-2">
          <p>{{ product.fin_prdt_nm }}</p>
        </div>
      </div>
      <div class="row detail-row">
        <div class="col-2 p-2">
          <strong>가입 제한</strong>
        </div>
        <div class="col p-2">
          <p>{{ product.join_deny }}</p>
        </div>
      </div>
      <div class="row detail-row">
        <div class="col-2 p-2">
          <strong>가입 방법</strong>
        </div>
        <div class="col p-2">
          <p>{{ product.join_way }}</p>
        </div>
      </div>
      <div class="row detail-row">
        <div class="col-2 p-2">
          <strong>우대 조건</strong>
        </div>
        <div class="col p-2">
          <p>{{ product.spcl_cnd }}</p>
        </div>
      </div>
      <span v-if="userStore.user !== null">
        <button v-if="!prdt_list.includes(String(product.id) + ',')" class="btn btn-primary mt-3" @click="addProduct">가입하기</button>
        <button v-if="prdt_list.includes(String(product.id) + ',')" class="btn btn-secondary mt-3" @click="deleteProduct">가입 취소</button>
      </span>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useFinanceStore } from '@/stores/financeStore'
import { useUserStore } from '@/stores/auth'

const route = useRoute()
const store = useFinanceStore()
const userStore = useUserStore()

const product = ref(store.financeProductList.find(element => {return element.fin_prdt_cd === route.params.fin_prdt_cd}))

const prdt_list = computed(() => {
  if (userStore.user !== null) {return userStore.user.prdt_list} else {return null}
})
const userName = userStore.user ? userStore.user.user.username : null

const addProduct = function () {
  if (window.confirm('가입하시겠습니까?')) {
    userStore.updatePortfolio(userName, {
      prdt_list: prdt_list.value + String(product.value.id) + ','
    })
    setTimeout(() => {userStore.getPortfolio(userName)}, 500)
  }
}
const deleteProduct = function () {
  if (window.confirm('가입을 취소합니다.')) {
    userStore.updatePortfolio(userName, {
      prdt_list: prdt_list.value.replace(String(product.value.id) + ',', '')
    })
    setTimeout(() => {userStore.getPortfolio(userName)}, 500)
  }
}
</script>

<style scoped>
.detail-container {
  background-color: #f5f5f5; /* 밝은 배경색 */
  padding: 20px;
  border-radius: 10px;
}

.detail-content {
  background-color: #ffffff; /* 흰색 배경 */
  border-radius: 10px;
  padding: 20px;
  color: #34495e; /* 텍스트 색상 */
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.detail-row {
  border-bottom: 1px solid #dddddd; /* 연한 회색 라인 */
  padding: 10px 0;
}

.detail-row:last-child {
  border-bottom: none;
}

strong {
  color: #34495e; /* 텍스트 색상 */
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

.btn-secondary {
  background-color: #95a5a6; /* 회색 버튼 */
  border-color: #95a5a6;
  color: white;
}

.btn-secondary:hover {
  background-color: #7f8c8d;
  border-color: #7f8c8d;
}
</style>
