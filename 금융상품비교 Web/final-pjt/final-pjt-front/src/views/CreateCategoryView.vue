<template>
  <div class="container mt-4">
    <h1>Create Category</h1>
    <div class="card">
      <div class="card-body">
        <form @submit.prevent="submit">
          <div class="mb-3">
            <label for="category" class="form-label">Category Name</label>
            <input type="text" id="category" class="form-control" v-model="categoryName">
          </div>
          <button class="btn btn-primary">submit</button>
        </form>
      </div>
    </div>
    <ul class='list-group list-group-flush'>
      <li class="list-group-item d-flex justify-content-between" v-for="category in store.categoryList"><span class="my-auto">{{ category.name }}</span><span class="btn btn-danger" @click="deleteCategory(category.id)">DELETE</span></li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { usePostStore } from '@/stores/postStore'

const store = usePostStore()
const categoryName = ref('')

const submit = function () {
  if (window.confirm('카테고리 작성')) {
    store.createCategory({
      name: categoryName.value
    })
    setTimeout(() => {
      store.getCategory()
    }, 200)
    categoryName.value = ''
  }
}

const deleteCategory = function (categoryId) {
  store.deleteCategory(categoryId)
  setTimeout(() => {
    store.getCategory()
  }, 200)
}
</script>

<style scoped>
button {
  width: 100%;
}
</style>