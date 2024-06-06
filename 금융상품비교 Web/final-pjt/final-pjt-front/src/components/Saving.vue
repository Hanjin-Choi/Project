<template>
  <div class="col">
    <h1 @click="sortOrder=0">적금 상품 목록</h1>
    <table class="table">
      <thead>
        <tr>
          <th>공시 제출일</th>
          <th>금융회사명</th>
          <th>상품명</th>
          <th @click="sortOrder=6">6개월</th>
          <th @click="sortOrder=12">12개월</th>
          <th @click="sortOrder=24">24개월</th>
          <th @click="sortOrder=36">36개월</th>
        </tr>
      </thead>
      <tbody>
        <tr @click="goDetail(product.fin_prdt_cd)" v-for="product in orderedList" :key="product.fin_prdt_cd" :class="{ 'table-success': prdt_list.includes(String(product.id) + ',') }" v-show="selectedPeriod === '0' ? true : (store.optionList[product.fin_prdt_cd].findIndex(element => String(element.save_trm) === selectedPeriod) >= 0)">
          <td>{{ product.dcls_month }}</td>
          <td>{{ product.kor_co_nm }}</td>
          <td>{{ product.fin_prdt_nm }}</td>
          <td v-for="period in [6, 12, 24, 36]">{{ product.option_set.find(element => element.save_trm === period) ? product.option_set.find(element => element.save_trm === period).intr_rate : '-' }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useFinanceStore } from '@/stores/financeStore'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/auth'

const props = defineProps({
  selectedBank: String,
  selectedPeriod: String,
})

const router = useRouter()

const store = useFinanceStore()
const userStore = useUserStore()

const prdt_list = computed(() => {
  if (userStore.user !== null) {return userStore.user.prdt_list} else {return null}
})

const goDetail = function (fin_prdt_cd) {
  router.push({ name: 'compareDetail', params: { fin_prdt_cd: fin_prdt_cd } })
}

const savingList = computed(() => {
  return store.financeProductList.filter((element) => {
    return ((element.prdt_category === 'saving') && (props.selectedBank === 'entireBank' ? true : element.kor_co_nm === props.selectedBank))
  })
})

const sortOrder = ref(0)
const orderedList = ref(savingList.value)

const sorting = () => {
  if (sortOrder.value === 0) {
    orderedList.value = savingList.value
  } else {
    orderedList.value = savingList.value.toSorted((a, b) => {
      const aNum = a.option_set.find(element => element.save_trm === sortOrder.value) ? a.option_set.find(element => element.save_trm === sortOrder.value).intr_rate : 0
      const bNum = b.option_set.find(element => element.save_trm === sortOrder.value) ? b.option_set.find(element => element.save_trm === sortOrder.value).intr_rate : 0
      return bNum - aNum
    })
  }
}

watch(sortOrder, sorting)
watch(savingList, sorting)
</script>

<style scoped>
tr {
  cursor: pointer;
}
</style>