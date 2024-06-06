<template>
  <div class="mt-4">
    <h4 class="text-center">{{ product.fin_prdt_nm }}</h4>
    <BarChart :optionList="optionList"/>
  </div>
</template>

<script setup>
import { useFinanceStore } from '@/stores/financeStore'
import { computed, ref } from 'vue'
import BarChart from '@/components/BarChart.vue'

const props = defineProps({
  product: Object,
})

const store = useFinanceStore()

const optionList = computed(() => props.product.option_set)
</script>

<style scoped>

</style>