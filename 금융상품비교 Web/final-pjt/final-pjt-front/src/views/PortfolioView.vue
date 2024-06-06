<template>
    <div class="portfolio">
        <div class="portfolioWindow shadow p-3 mb-5 bg-body-tertiary rounded">
            <h1>Portfolio</h1>
            <br>
            <div class="portfolioPage row">
                <div class="side mb-2 col-6">
                    <input class="form-control mx-auto" type="text" v-model="age" id="age" placeholder="나이">
                    <br>
                    <input class="form-control mx-auto" type="text" v-model="asset" id="asset" placeholder="자산">
                    <br>
                    <input class="form-control mx-auto" type="text" v-model="salary" id="salary" placeholder="연봉">
                </div>
                <div class="side mb-2 col-6">
                    <select class="form-select" v-model="favorite" id="favorite">
                        <option disabled value="">--최애은행--</option>
                        <option v-for="bank in bankList">{{ bank }}</option>
                    </select>
                    <br>
                    <select class="form-select" v-model="ivst_taste" id="ivst_taste">
                        <option disabled value="">--투자성향--</option>
                        <option>공격투자</option>
                        <option>적극투자</option>
                        <option>위험중립</option>
                        <option>안정추구</option>
                        <option>안정</option>
                    </select>
                    <br>
                </div>
                <button @click="register" class="btn btn-dark">REGISTER</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/auth';
import { useRoute,useRouter } from 'vue-router';
const route=useRoute()
const router=useRouter()
const username = ref(route.params.userName)
const ivst_taste=ref('')
const prdt_list=ref(',')
const age=ref(null)
const asset=ref(null)
const salary=ref(null)
const favorite=ref("")
const bankList = ref(['국민은행','하나은행','한국스탠다드차타드은행',
    '신한은행','외환은행','우리은행','한국시티은행',
    '경남은행','광주은행','대구은행','부산은행','전북은행','제주은행',
    '중소기업은행','농협은행주식회사','수협은행','한국산업은행','한국수출입은행',
    '주식회사 케이뱅크', '주식회사 카카오뱅크','토스뱅크 주식회사',
])

const store = useUserStore()

const register = function(){
    const payload ={
        age:age.value,
        prdt_list:prdt_list.value,
        asset:asset.value,
        ivst_taste:ivst_taste.value,
        salary:salary.value,
        favorite:favorite.value,
    }
    if (window.confirm('입력하신 내용이 확실합니까?')) {
        if (store.user === null) {
            store.createPortfolio(username.value,payload)
        } else {
            store.updatePortfolio(username.value,payload)
        }
        
        setTimeout(() => {
            router.push({name:'profile'})
        }, 500)
    }
}

onMounted(() => {
    if (store.user !== null) {
        age.value = store.user.age
        asset.value = store.user.asset
        salary.value = store.user.salary
        favorite.value = store.user.favorite
        ivst_taste.value = store.user.ivst_taste
        prdt_list.value = store.user.prdt_list
    }
})
</script>

<style scoped>
.portfolio {
    background-color: white;
    align-content: center;
    height: 100vh;
    text-align: center;
}
.portfolioWindow{
    display :inline-block;
    height: 50%;
    width : 40%;
    align-content: center;
    background-color: white;
    border-radius: 10px;
    overflow: hidden;
    margin:0;
}
.portfolioPage {
    justify-content: center;
    height: 60%;
}

.side{
    display : block;
    height: 100%;
    flex-wrap: wrap;
}

input {  
    width: 80%;
    margin-top: 2rem;
}
select{
    width:80%;
    margin-top: 2rem;
}
button{
    width : 40%;
    bottom: 10;
}
</style>