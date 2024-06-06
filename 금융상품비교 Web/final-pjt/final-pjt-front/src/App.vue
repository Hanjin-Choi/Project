<template>
  <div>
    <Navbar />
    <RouterView />
  
  </div>
  <footer class="fixed-bottom">
    <ChatBot />
  </footer>
</template>

<script setup>
import { ref } from 'vue';
import {RouterLink,RouterView} from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import ChatBot from '@/components/ChatBot.vue';

</script>


<style scoped>
</style>