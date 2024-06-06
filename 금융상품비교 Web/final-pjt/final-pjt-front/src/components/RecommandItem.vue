<template>
  <div class="row">
    <div class="col">
      <p class="fs-4">{{ product.finPrdtNm }}</p>
      <p class="fs-4">{{ product.prdtCategory === 'deposit' ? '정기예금' : '적금' }}</p>
      <p class="fs-4">가입 방식 : {{ product.joinWay }}</p>
      <p class="fs-4">최고 금리 : {{ product.maxTrm }}개월 - {{ product.maxRate }}%</p>
    </div>
    <div class="col-3 p-5">
      <button @click="goDetail(product.finPrdtCd)" class="btn btn-primary">Detail</button>
    </div>
    <hr>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

defineProps({
  product: Object,
})

const router = useRouter()

const goDetail = function (finPrdtCd) {
  router.push({ name: 'compareDetail', params: { 'fin_prdt_cd': finPrdtCd } })
}
</script>

<style scoped>
button {
  width: 100%;
  height: 90%;
}
</style>