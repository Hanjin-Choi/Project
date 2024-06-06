<template>

<div class="container mt-4">
    <h1>{{ post.title }}</h1>
    <div class="container p-5">
      <div class="row">
        <div class="col-2 p-2">
          <strong>카테고리</strong>
        </div>
        <div class="col p-2">
          <p>{{ post.category.name }}</p>
        </div>
      </div>
      <div class="row">
        <div class="col-2 p-2">
          <strong>작성자</strong>
        </div>
        <div class="col p-2">
          <p>{{ post.user.username }}</p>
        </div>
      </div>
      <div class="row">
        <div class="col-2 p-2">
          <strong>작성일</strong>
        </div>
        <div class="col p-2">
          <p>{{ post.created_at.slice(0,10) }} {{ post.created_at.slice(11,16) }}</p>
        </div>
      </div>
      <div class="row">
        <div class="col-2 p-2">
          <strong>내용</strong>
        </div>
        <div class="col p-2">
          <p>{{ post.content }}</p>
        </div>
      </div>
      <div class="text-end">
          <button class="btn btn-warning" @click="update">UPDATE</button>&nbsp;
          <button class="btn btn-danger" @click="del">DELETE</button>
      </div>

    </div>
    <hr>
    <Comment :post-Id="postId"/>

</div>
</template>

<script setup>
import { ref } from 'vue';
import { usePostStore } from '@/stores/postStore';
import { useRoute,useRouter } from 'vue-router';
import Comment from '@/components/Comment.vue';
const store = usePostStore()
const route =useRoute()
const router = useRouter()
const postList = store.postList
const postId = route.params.postId
const post = postList.find(ele => ele.id==postId)
const del = function(){
  store.deletePost(postId)
}
const update=function () {
  router.push({name:'postUpdate',params:{'postId':postId}})
}

</script>

<style scoped>

</style>