<template>
  <div class="container my-5 create-post-container">
    <h1>{{ route.params.postId != null ? '게시글 수정 페이지' : '게시글 생성 페이지' }}</h1>
    <div class="card mt-4">
      <div class="card-body">
        <form @submit.prevent="submitForm">
          <div class="mb-3">
            <label for="category" class="form-label">카테고리 선택</label>
            <select name="category" id="category" class="form-select" v-model="categoryId" required>
              <option disabled value="0">--카테고리 선택--</option>
              <option v-for="category in store.categoryList" :key="category.id" :value="category.id">{{ category.name }}</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="title" class="form-label">제목</label>
            <input type="text" class="form-control" id="title" placeholder="제목" v-model="title" required>
          </div>
          <div class="mb-3">
            <label for="content" class="form-label">내용</label>
            <textarea name="content" id="content" cols="30" rows="10" placeholder="내용" class="form-control" v-model="content" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary w-100">{{ route.params.postId != null ? 'Update' : 'Submit' }}</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { usePostStore } from '@/stores/postStore'
import { useRouter, useRoute } from 'vue-router'

const store = usePostStore()
const router = useRouter()
const route = useRoute()
const categoryId = ref(0)
const title = ref('')
const content = ref('')

const submitForm = async () => {
  const payload = {
    category: categoryId.value,
    title: title.value,
    content: content.value,
  }

  if (route.params.postId != null) {
    if (window.confirm('게시글 정보를 수정합니다.')) {
      await store.updatePost(route.params.postId, payload)
      alert('게시글이 수정되었습니다.')
    }
  } else {
    if (window.confirm('게시글을 작성합니다.')) {
      await store.createPost(payload)
      alert('게시글이 작성되었습니다.')
    }
  }

  router.push({ name: 'community-home' })
}

onMounted(() => {
  if (route.params.postId != null) {
    const post = store.postList.find(ele => ele.id == route.params.postId)
    if (post) {
      categoryId.value = post.category.id
      title.value = post.title
      content.value = post.content
    }
  }
})
</script>

<style scoped>
.create-post-container {
  max-width: 800px;
  margin: 0 auto;
}

.card {
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card-body {
  padding: 20px;
}

.form-label {
  font-weight: bold;
}

.btn-primary {
  background-color: #3498db;
  border-color: #3498db;
}

.btn-primary:hover {
  background-color: #2980b9;
  border-color: #2980b9;
}
</style>
