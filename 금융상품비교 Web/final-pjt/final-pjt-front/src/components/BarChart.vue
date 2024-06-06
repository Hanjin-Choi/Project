<template>
  <Bar
    id="my-chart-id"
    :options="chartOptions"
    :data="chartData"
  />
</template>

<script setup>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, elements } from 'chart.js'
import { defineProps } from 'vue'
  
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const props = defineProps({
  optionList: Array,
})

const trmList = [6, 12, 24, 36]
const rates1 = []
const rates2 = []

trmList.forEach(period => {
  rates1.push(props.optionList.find(element => element.save_trm === period) ? props.optionList.find(element => element.save_trm === period).intr_rate : 0)
  rates2.push(props.optionList.find(element => element.save_trm === period) ? props.optionList.find(element => element.save_trm === period).intr_rate2 : 0)
})

const chartData = {
  labels: trmList,
  datasets: [
    {
      label: '저축 금리',
      backgroundColor: '#ccff66',
      data: rates1,
    },
    {
      label: '최고 우대금리',
      backgroundColor: '#336600',
      data: rates2,
    },
  ]
}

const chartOptions = {
  responsive: true
}
</script>
