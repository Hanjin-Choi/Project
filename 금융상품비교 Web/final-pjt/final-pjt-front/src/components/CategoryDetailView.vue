<template>
  <div>
    <h1>{{ route.params.categoryName }}</h1>
    <hr>
    <PostItem v-for="post in postList" :post="post" />
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router'
import { usePostStore } from '@/stores/postStore';
import PostItem from './PostItem.vue';
const route = useRoute()
const store=usePostStore()
const postList = computed(() => {
  return store.postList.filter(ele => ele.category.name===route.params.categoryName)
})
</script>

<style scoped>

</style>
