<template>
  <div>
    <h1>전체 게시글</h1>
    <hr>
    <PostItem v-for="post in postList" :post="post" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { usePostStore } from '@/stores/postStore';
import PostItem from './PostItem.vue';
const store=usePostStore()
const postList = computed(() => store.postList)
</script>

<style scoped>

</style>