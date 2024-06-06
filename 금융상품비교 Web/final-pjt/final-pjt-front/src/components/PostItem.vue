<template>
    <div class="container">
        <div class="row row-cols-auto">
            <div class="col-12 col-sm-2">
                {{ post.category.name }}
            </div>
            <div class="col col-sm-8 text-start">
                <RouterLink :to="{name:'postDetail',params:{'postId':post.id}}">
                    [{{post.category.name}}] {{ post.title }}
                </RouterLink>
            </div>
            <div class="col col-sm-2 text-end">
                작성자 : {{ post.user.username }} 
                <span> | </span>
                {{ post.created_at.slice(0,10) }} {{ post.created_at.slice(11,16) }}
            </div>
        </div>
    </div>
    <hr>
</template>

<script setup>
import { RouterLink } from 'vue-router';

const props=defineProps({
    post:Object,
})
</script>

<style scoped>

</style>