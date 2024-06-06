<template>
  <div class="container mt-4">
    <h1 class="text-center mb-4">환율 계산기</h1>
    <div class="card mx-auto" style="max-width: 600px;">
      <div class="card-body">
        <select class="form-select mb-3" name="country1" id="country1" v-model="currCountry1">
          <option v-for="country in countries" :key="country.curUnit" :value="country.curUnit">
            {{ country.curNm }}
          </option>
        </select>
        <div class="input-group mb-3">
          <input type="text" class="form-control" v-model="price" placeholder="금액을 입력하세요">
          <button class="btn btn-outline-primary" type="button" @click="calc">계산</button>
        </div>
        <select class="form-select mb-3" name="country2" id="country2" v-model="currCountry2">
          <option v-for="country in countries" :key="country.curUnit" :value="country.curUnit">
            {{ country.curNm }}
          </option>
        </select>
        <input type="text" class="form-control mb-5" v-model="result" readonly placeholder="결과">
        <div class="row text-center">
          <div class="col-5">
            <div class="card p-2">
              <img :src="countrySrc1" alt="nation1" class="img-fluid flag">
            </div>
          </div>
          <div class="col-2 d-flex align-items-center justify-content-center">
            <img src="@/assets/arrow.png" alt="arrow" class="img-fluid">
          </div>
          <div class="col-5">
            <div class="card p-2">
              <img :src="countrySrc2" alt="nation2" class="img-fluid flag">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useFinanceStore } from '@/stores/financeStore'

const store = useFinanceStore()

const countries = ref([])
const currCountry1 = ref('KRW')
const currCountry2 = ref('USD')

const countryFlag = {
  AED: 'UAE.png',
  AUD: 'AUS.png',
  BHD: 'Bahrain.png',
  BND: 'Brunei.png',
  CAD: 'Canada.png',
  CHF: 'Switzerland.png',
  CNH: 'China.png',
  DKK: 'Denmark.png',
  EUR: 'Europe.png',
  GBP: 'United_Kingdom.png',
  HKD: 'Hong_Kong.png',
  'IDR(100)': 'Indonesia.png',
  'JPY(100)': 'Japan.png',
  KRW: 'korea.jpg',
  KWD: 'Kuwait.png',
  MYR: 'Malaysia.png',
  NOK: 'Norway.png',
  NZD: 'New_Zealand.png',
  SAR: 'Saudi_Arabia.png',
  SEK: 'Sweden.png',
  SGD: 'Singapore.png',
  THB: 'Thailand.png',
  USD: 'United_States.png',
}

const countrySrc1 = computed(() => '/src/assets/nations/' + countryFlag[currCountry1.value])
const countrySrc2 = computed(() => '/src/assets/nations/' + countryFlag[currCountry2.value])

const price = ref(0.0)
const tmp_price = ref(0.0)
const result = ref(0.0)

const calc = function () {
  const info1 = store.exchangeData.find((element) => {
    return element.cur_unit === currCountry1.value
  })
  const info2 = store.exchangeData.find((element) => {
    return element.cur_unit === currCountry2.value
  })
  if (currCountry1.value === 'KRW') {
    tmp_price.value = price.value
  } else {
    tmp_price.value = price.value * parseFloat(info1.ttb.replace(',', ''))
    if (currCountry1.value === 'JPY(100)' || currCountry1.value === 'IDR(100)') {
      tmp_price.value /= 100
    }
  }
  if (currCountry2.value === 'KRW') {
    result.value = tmp_price.value
  } else {
    result.value = tmp_price.value / parseFloat(info2.tts.replace(',', ''))
    if (currCountry2.value === 'JPY(100)' || currCountry2.value === 'IDR(100)') {
      result.value *= 100
    }
  }
}

onMounted(() => {
  store.getExchangeInfo()
  setTimeout(() => {
    store.exchangeData.forEach(element => {
      countries.value.push({
        curUnit: element.cur_unit,
        curNm: element.cur_nm,
      })
    })
  }, 300)
})
</script>

<style scoped>
.card {
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border: none;
}

.text-primary {
  color: #3498db;
}

.btn-outline-primary {
  border-color: #3498db;
  color: #3498db;
}

.btn-outline-primary:hover {
  background-color: #3498db;
  color: white;
}

.input-group .form-control {
  border-radius: 5px;
  border: 1px solid #ddd;
}

.form-select {
  border-radius: 5px;
  border: 1px solid #ddd;
}

.img-fluid {
  max-width: 100%;
  height: 140px;
}

.flag {
  border: solid #ddd 1px;
}

input[readonly] {
  background-color: #f9f9f9;
  color: #34495e;
  border: 1px solid #ddd;
}
</style>
