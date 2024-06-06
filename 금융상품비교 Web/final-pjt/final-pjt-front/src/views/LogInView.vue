<template>
    <div class="login">
        <div class="loginWindow row position-relative">
            <div class="loginPage col-6 position-absolute start-0">
                <h1>Sign In</h1>
                <br>
                <form @submit.prevent="login">
                    <div class="username">
                        <input class="form-control mx-auto" type="text" v-model="username" id="username" placeholder="Username">
                    </div>
                    <br>
                    <div class="password">
                        <input class="form-control mx-auto" type="password" v-model="password" id="password" placeholder="Password">
                    </div>
                    <br>
                    <div>
                        <button type="submit" class="btn btn-dark">SIGN IN</button>
                    </div>
                </form>
            </div>
            <div class="signUpPage col-6 position-absolute top-0">
                <h1>Hello, Customer!</h1>
                <br>
                <p>Register with your personal account to use this apps</p>
                <br>
                <button @click="buttonClick" class="btn btn-primary">SIGN UP</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
const store=useUserStore()
const router = useRouter()
const buttonClick = function() {
    router.push({name:'signup'})
}
const username = ref(null)
const password = ref(null)

const login = function(){
    const payload ={
    username: username.value ,
    password : password.value,
    }
    store.logIn(payload)
    setTimeout(() => {
        if (store.isAuthenticated) {
            store.getPortfolio(username.value)
        } else {
            window.alert('잘못된 정보입니다. 다시 한 번 확인해주세요.')
        }
    }, 1000)
}

</script>

<style scoped>
.login {
    background : linear-gradient(to right,white,skyblue);
    align-content: center;
    height: 100vh;
    text-align: center;
}
.loginWindow{
    display :inline-block;
    height: 50%;
    width : 40%;
    background-color: white;
    border-radius: 10px;
    overflow: hidden;
    margin:0;
}

.loginPage{
    display : inline-block;
    height: 100%;
    align-content: center;
}

.signUpPage{
    display: inline-block;
    background-color: #20639B;
    color:white;
    height:100%;
    align-content: center;
    border-top-left-radius: 30%;
    border-bottom-left-radius: 30%;
}
input {  
    width: 70%;
}
button{
    width : 40%
}
</style>