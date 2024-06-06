<template>
  <div class="container mt-2">
    <h3 class="mb-4">선호하시는 <span class="text-success">{{ userStore.user.favorite }}</span>의 상품이에요!</h3>
    <RecommendItem v-for="product in orderedList" :key="product.finPrdtCd" :product="product"/>
  </div>
</template>

<script setup>
import RecommendItem from '@/components/RecommandItem.vue'
import { useFinanceStore } from '@/stores/financeStore'
import { useUserStore } from '@/stores/auth'
import { ref, computed } from 'vue'

const userStore = useUserStore()
const store = useFinanceStore()

const prdtList = computed(() => {
  return store.financeProductList.filter(item => {
    return item.kor_co_nm === userStore.user.favorite
  })
})

const orderedList = ref([])

prdtList.value.forEach(element => {
  const maxTrm = ref(0)
  const maxRate = ref(0)

  element.option_set.forEach(option => {
    if (option.intr_rate2 > maxRate.value) {
      maxRate.value = option.intr_rate2
      maxTrm.value = option.save_trm
    }
  })
  orderedList.value.push({
    finPrdtCd: element.fin_prdt_cd,
    finPrdtNm: element.fin_prdt_nm,
    maxRate: maxRate.value,
    maxTrm: maxTrm.value,
    prdtCategory: element.prdt_category,
    joinWay: element.join_way
  })
})
orderedList.value.sort((a, b) => b.maxRate - a.maxRate)
</script>

<style scoped>

</style>