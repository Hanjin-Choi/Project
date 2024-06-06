<template>
    <div class="signUp">
        <div class="signUpWindow row position-relative">
            <div class="logInPage col-6 position-absolute top-0 start-0">
                <h1>Welcome Back!</h1>
                <br>
                <p>Enter your personal account to enter the website apps</p>
                <br>
                <button @click="buttonClick" class="btn btn-primary">SIGN IN</button>
            </div>
            <div class="signUpPage col-6 position-absolute top-0">
                <h1>Create Account</h1>
                <br>
                <form @submit.prevent="signUp">
                    <div class="name">
                        <input class="form-control mx-auto" type="text" v-model="username" id="name" placeholder="Name">
                    </div>
                    <br>
                    <div class="Email">
                        <input class="form-control mx-auto" type="text" v-model="email" id="email" placeholder="Email">
                    </div>
                    <br>
                    <div class="Email">
                        <input class="form-control mx-auto" type="password" v-model="password1" id="password1" placeholder="Password">
                    </div>
                    <br>
                    <div class="password2">
                        <input class="form-control mx-auto" type="password" v-model="password2" id="password" placeholder="Password Confirm">
                    </div>
                    <br>
                    <div>
                        <button type="submit" class="btn btn-dark">SIGN UP</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { useUserStore } from '@/stores/auth';

const router = useRouter()
const buttonClick = function(){
    router.push({name:'login'})
}

const username=ref(null)
const email=ref(null)
const password1=ref(null)
const password2=ref(null)
const store = useUserStore()
const signUp = function(){
    const payload = {
        username : username.value,
        email : email.value,
        password1 : password1.value,
        password2 : password2.value,
    }
    store.signUp(payload)
    setTimeout(() => {router.push({ name: 'portfolio', params: { userName: username.value } })}, 500)
}
</script>

<style scoped>
.signUp {
    background : linear-gradient(to right,skyblue,white);
    align-content: center;
    height: 100vh;
    text-align: center;
}
.signUpWindow{
    display :inline-block;
    height: 50%;
    width : 40%;
    background-color: white;
    border-radius: 10px;
    overflow: hidden;
    margin:0;
}

.signUpPage{
    display : inline-block;
    height: 100%;
    align-content: center;
}

.logInPage{
    display: inline-block;
    background-color: #20639B;
    color:white;
    height:100%;
    align-content: center;
    border-top-right-radius: 30%;
    border-bottom-right-radius: 30%;
}

input{
    width: 70%
}
button{
    width : 40%
}
</style>