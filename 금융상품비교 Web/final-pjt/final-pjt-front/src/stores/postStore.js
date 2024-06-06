import { ref, computed } from "vue"
import { defineStore } from "pinia"
import axios from "axios"
import { useUserStore } from '@/stores/auth'
import { useRouter } from "vue-router"

export const usePostStore = defineStore('post', () => {
  const BASE_URL = 'http://127.0.0.1:8000/posts'
  const userStore = useUserStore()
  const router=useRouter()
  const categoryList = ref(null)
  const postList = ref(null)
  const commentList = ref([])

  const getCategory = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/categories/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    .then(res => {
      console.log(res)
      categoryList.value = res.data
    })
    .catch(err => console.log(err))
  }

  const getPost = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/posts/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    .then(res => {
      console.log(res)
      postList.value = res.data
    })
    .catch(err => console.log(err))
  }

  const getComment = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/comments/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    .then(res => {
      console.log(res)
      commentList.value = res.data
    })
    .catch(err => console.log(err))
  }

  const deletePost = function(postId){
    axios({
      method :'delete',
      url : `${BASE_URL}/post/${postId}/`,
      headers : {
        Authorization :  `Token ${userStore.token}`
      }
    })
    .then(res=>{
      console.log(res)
      getPost()
      setTimeout(() => {
        router.push({name:'community-home'})
      }, 200);
    })
    .catch(err => console.log(err))
  }

  const updatePost= function(postId,payload){
    axios({
      method:'put',
      url: `${BASE_URL}/post/${postId}/`,
      headers :{
        Authorization : `Token ${userStore.token}`
      },
      data:payload,
    })
    .then(res=>{
      console.log(res)
      getPost()
      setTimeout(()=>{
        router.push({name:'postDetail',params:{'postId':postId}})
      },200)
    })
    .catch(err=> console.log(err))
  }

  const createCategory = function (categoryData) {
    axios({
      method: 'post',
      url: `${BASE_URL}/categories/create/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
      data: categoryData,
    })
    .then(res => console.log(res))
    .catch(err => console.log(err))
  }

  const createPost = function (postData) {
    axios({
      method: 'post',
      url: `${BASE_URL}/posts/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
      data: postData,
    })
    .then(res => {
      console.log(res)
      setTimeout(()=>{
        router.push({name:'community-home'})
      },200)
    })
    .catch(err => console.log(err))
  }

  const createComment = function (postId, commentData) {
    axios({
      method: 'post',
      url: `${BASE_URL}/post/${postId}/comments/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
      data: commentData,
    })
    .then(res => console.log(res))
    .catch(err => console.log(err))
  }

  const deleteCategory = function (categoryId) {
    axios({
      method: 'delete',
      url: `${BASE_URL}/categories/${categoryId}/delete/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    .then(res => console.log(res))
    .catch(err => console.log(err))
  }

  const deleteComment = function (postId,commentId){
    axios({
      method:'delete',
      url :`${BASE_URL}/post/${postId}/comment/${commentId}/`,
      headers :{
        Authorization: `Token ${userStore.token}`,
      }
    })
    .then(res=>console.log(res))
    .catch(err=>console.log(err))
  }
  // path('posts/post/<int:post_pk>/comment/<int:comment_pk>/', views.delete_comment),

  return {
    categoryList,
    postList,
    commentList,
    getCategory,
    getPost,
    getComment,
    createCategory,
    createPost,
    createComment,
    deleteCategory,
    deletePost,
    updatePost,
    deleteComment,
  }
}, { persist:true })