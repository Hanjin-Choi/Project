<template>
    <div class="container">
        <h2>비밀번호 변경</h2>
        <input placeholder="Password" type="password" v-model="password1" class="form-control mt-3">

        <input placeholder="Password Confirmation" type="password" v-model="password2" class="form-control mt-3">

        <button class="btn btn-dark mt-3" @click="buttonClick">UPDATE</button>

    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
const store = useUserStore()
const password1=ref(null)
const password2=ref(null)
const router = useRouter()
const buttonClick = function() {
    const payload={
        new_password1:password1.value,
        new_password2:password2.value,
    }
    store.passwordChange(payload)
    setTimeout(()=>{
        router.push({name:'profile'})
    },100)
}

</script>

<style scoped>
</style>