<template>
  <div class="container mt-4">
    <nav class="mb-3">
      <span @click="() => curr='deposit'" class="fs-3 navitem" :class="{ 'text-success': curr==='deposit', 'text-black-50': !(curr==='deposit') }">정기예금</span>&nbsp;
      <span @click="() => curr='saving'" class="fs-3 navitem" :class="{ 'text-success': curr==='saving', 'text-black-50': !(curr==='saving') }">적금</span>
    </nav>
    <div class="row">
      <div class="col-2">
        <h3>검색하기</h3>
        <p>검색 조건을 입력하세요</p>
        <hr>
        <div class="mb-3">
          <label for="bank" class="form-label">은행을 선택하세요</label>
          <select name="bank" id="bank" class="form-select" v-model="selectedBank">
            <option value="entireBank">전체 은행</option>
            <option v-for="bank in store.bankList" :value="bank">{{ bank }}</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="period" class="form-label">예치 기간</label>
          <select name="period" id="period" class="form-select" v-model="selectedPeriod">
            <option value="0">전체 기간</option>
            <option v-for="period in periodList" :value="String(period)">{{ period }}개월</option>
          </select>
        </div>
      </div>
      <Deposit v-if="store.financeProductList && (curr==='deposit')" :selectedBank="selectedBank" :selectedPeriod="selectedPeriod"/>
      <Saving v-if="store.financeProductList && (curr==='saving')" :selectedBank="selectedBank" :selectedPeriod="selectedPeriod"/>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useFinanceStore } from '@/stores/financeStore'
import Deposit from '@/components/Deposit.vue'
import Saving from '@/components/Saving.vue'

const curr = ref('deposit')
const store = useFinanceStore()

const periodList = [6, 12, 24, 36]

const selectedBank = ref('entireBank')
const selectedPeriod = ref('0')

onMounted(() => {
  store.getFinanceInfo()
  setTimeout(() => {
    store.getBankInfo()
  }, 200)
})
</script>

<style scoped>
a {
  text-decoration-line: none;
}
.navitem {
  cursor: pointer;
}
</style>