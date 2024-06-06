import { ref, computed } from "vue"
import { defineStore } from "pinia"
import axios from "axios"
import { useUserStore } from "./auth"

export const useFinanceStore = defineStore('finance', () => {
    const BASE_URL = 'http://127.0.0.1:8000/finances'
    const userStore = useUserStore()

    const financeProductList = ref([])
    const bankList = ref([])
    const optionList = ref({})
    const exchangeData = ref(null)

    const getFinanceInfo = function () {
        if (financeProductList.value.length ===0 ) {
            axios({
                method: 'get',
                url: `${BASE_URL}/run/`,
                headers: {
                    Authorization: `Token ${userStore.token}`
                }
            })
            .then(res => console.log(res))
            .catch(err => console.log(err))
            axios({
                method: 'get',
                url: `${BASE_URL}/products/`,
                headers: {
                    Authorization: `Token ${userStore.token}`
                }
            })
            .then(res => {
                console.log(res)
                financeProductList.value = res.data
            })
            .catch(err => console.log(err))
        }
    }

    const getBankInfo = function () {
        if (financeProductList.value && (bankList.value.length === 0)) {
            financeProductList.value.forEach((element) => {
                if (bankList.value.indexOf(element.kor_co_nm) === -1) {
                    bankList.value.push(element.kor_co_nm)
                }
            })
        }
    }

    const getOptionInfo = function () {
        if (Object.keys(optionList.value).length === 0) {
            axios({
                method: 'get',
                url: `${BASE_URL}/options/`,
                headers: {
                    Authorization: `Token ${userStore.token}`
                }
            })
            .then(res => {
                console.log(res)
                optionList.value = {}
                res.data.forEach((element) => {
                    if (element.fin_prdt_cd in optionList.value) {
                        optionList.value[element.fin_prdt_cd].push(element)
                    } else {
                        optionList.value[element.fin_prdt_cd] = [element]
                    }
                })
            })
            .catch(err => console.log(err))
        }
    }

    const getExchangeInfo = function () {
        if (!exchangeData.value) {
            axios({
                method: 'get',
                url: `${BASE_URL}/exchange/`
            })
            .then(res => {
                console.log(res.data.response)
                exchangeData.value = res.data.response
            })
            .catch(err => console.log(err))
        }
    }

    return {
        BASE_URL,
        financeProductList,
        bankList,
        optionList,
        exchangeData,
        getFinanceInfo,
        getBankInfo,
        getOptionInfo,
        getExchangeInfo,
    }
}, { persist:true })