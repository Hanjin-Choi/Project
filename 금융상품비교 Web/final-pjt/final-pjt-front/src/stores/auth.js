import { ref, computed } from "vue"
import { defineStore } from "pinia"
import axios from "axios"
import { useRouter } from "vue-router"

export const useUserStore = defineStore('user', () => {
  const router = useRouter()

  const USER_URL = 'http://127.0.0.1:8000/accounts'

  const token = ref(null)
  const isAuthenticated = ref(false)
  const user = ref(null)

  const signUp = function (payload) {
    axios({
      method: 'post',
      url: `${USER_URL}/signup/`,
      data: payload,
    })
    .then(res => {
      console.log(res)
      logIn({
        username: payload.username,
        password: payload.password1,
      })
      if (!alert('회원가입 후 포트폴리오 작성이 필요합니다.')) {
        router.push({name:'portfolio'})
      }
    })
    .catch(err => console.log(err))
  }

  const logIn = function (payload) {
    axios({
      method: 'post',
      url: `${USER_URL}/login/`,
      data: payload,
    })
    .then(res => {
      console.log(res)
      token.value = res.data.key
      isAuthenticated.value = true
      router.push({name:'mainpage'})
    })
    .catch(err => console.log(err))
  }

  const createPortfolio = function (userName, userData) {
    axios({
      method: 'post',
      url: `${USER_URL}/${userName}/portfolio/`,
      data: userData,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      console.log(res)
      getPortfolio(userName)
    })
    .catch(err => console.log(err))
  }

  const updatePortfolio = function (userName, userData) {
    axios({
      method: 'put',
      url: `${USER_URL}/${userName}/portfolio/`,
      data: userData,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      console.log(res)
      getPortfolio(userName)
    })
    .catch(err => console.log(err))
  }

  const getPortfolio = function (userName) {
    axios({
      method: 'get',
      url: `${USER_URL}/user/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      console.log(res)
      user.value = res.data
    })
    .catch(err => {
      console.log(err)
      if (user.value === null) {
        alert('포트폴리오 작성이 필요합니다.')
        router.push({ name: 'portfolio', params: { 'userName': userName } })
      }
    })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${USER_URL}/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => {
      console.log(res)
      token.value = null
      isAuthenticated.value = false
      user.value = null
    })
    .catch(err => console.log(err))
  }

  const passwordChange = function(payload){
    axios({
      method:'post',
      url:`${USER_URL}/password/change/`,
      headers : {
        Authorization : `Token ${token.value}`
      },
      data : payload,
    })
    .then(res=>{
      console.log(res)
    }
    )
    .catch(err=>console.log(err))
  }

  return {
    token,
    isAuthenticated,
    user,
    signUp,
    logIn,
    createPortfolio,
    updatePortfolio,
    getPortfolio,
    logOut,
    passwordChange,
  }
}, { persist: true })