<template>
    <div class="container">
        <div class="row">
          <div class="col-8">
            <input v-model="userComment" class="form-control" name="" id="">
          </div>
          <div class="col">
            <button class="btn btn-dark" @click="create">댓글작성</button>
          </div>
        </div>
    </div>
    <hr>
    <div class="container">
      <div v-if="commentList.length !=0">
          <div class="row d-flex justify-content-between" v-for="comment in commentList">
            <div class="col-10 d-flex justify-content-between">
              <p class="my-auto">{{ comment.content }}</p>
              <p class="my-auto">{{ comment.user.username }}</p>
            </div>
            <div class="col-auto" v-if="comment.user.username==userStore.user.user.username">
              <button class="btn btn-secondary" @click="del(comment.id)">삭제</button>
            </div>
            <hr class="my-3">
          </div>
      </div>
      <div v-else>
        <p>첫 댓글의 영광을 가져가세요</p>
      </div>
    </div>

  </template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue';
  import { useRoute } from 'vue-router'
  import { usePostStore } from '@/stores/postStore';
  import { useUserStore } from '@/stores/auth';
  const commentStore = usePostStore()
  const userStore =useUserStore()
  const route=useRoute()
  const commentList=computed(() => {
    return commentStore.commentList.filter(ele => ele.post ==route.params.postId)
  })
  const userComment=ref(null)
  const props=defineProps({
    postId:String,
  })
  const postId = props.postId
  const create=function(){
    const payload={
      content : userComment.value,
    }
    commentStore.createComment(postId,payload)
    userComment.value=''
    setTimeout(() => {
      commentStore.getComment()
    }, 200);
  }

  const del = function(commentId){
    commentStore.deleteComment(postId,commentId)
    setTimeout(() => {
      commentStore.getComment()
    }, 200);
  }

  onMounted(()=>{
    commentStore.getComment()
  })
  </script>
  
  <style scoped>
  .commentContent{
    height: 38px;
    align-items: center;
    display: inline-block;
  }
  </style>