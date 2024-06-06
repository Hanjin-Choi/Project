<template>
  <div>
    <button @click="toggleChatbot" class="chatbot-button">
      <img src="@/assets/chatbot-icon.png" alt="Chatbot Icon">
    </button>
    <div v-if="showChatbot" class="chatbot-window" ref="chatWindow">
      <div class="chatbot-header">
        <h2>대화</h2>
        <button @click="toggleChatbot" class="close-button">×</button>
      </div>
      <div class="chatbot-body">
        <div class="message" v-for="(message, index) in messages" :key="index">
          <div class="message-content" :class="message.type">
            <p v-html="message.content"></p>
          </div>
        </div>
      </div>
      <div class="chatbot-footer">
        <input type="text" v-model="userMessage" placeholder="질문을 입력하세요..." @keyup.enter="sendMessage">
        <button @click="sendMessage">보내기</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, nextTick } from 'vue';

export default {
  name: 'App',
  setup() {
    const showChatbot = ref(false);
    const userMessage = ref('');
    const messages = ref([
      { type: 'bot', content: '안녕하세요! 무엇을 도와드릴까요?' }
    ]);

    const toggleChatbot = () => {
      showChatbot.value = !showChatbot.value;
      if (showChatbot.value) {
        nextTick(() => {
          scrollToBottom();
        });
      }
    };

    const scrollToBottom = () => {
      const chatWindow = document.querySelector('.chatbot-body');
      if (chatWindow) {
        // chatWindow.scrollTop = chatWindow.scrollHeight;
        chatWindow.scrollTo({ top: chatWindow.scrollHeight, behavior: 'smooth' })
      }
    };

    const sendMessage = async () => {
      if (userMessage.value.trim() === '') return;

      messages.value.push({ type: 'user', content: userMessage.value });

      try {
        const response = await axios.post('http://localhost:8000/chatbot/', {
          message: userMessage.value
        });
        messages.value.push({ type: 'bot', content: response.data.message });
      } catch (error) {
        console.error('Error:', error);
      } finally {
        userMessage.value = '';
        nextTick(() => {
          scrollToBottom();
        });
      }
    };

    return {
      showChatbot,
      userMessage,
      messages,
      toggleChatbot,
      sendMessage,
    };
  }
};
</script>

<style scoped>
.chatbot-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #ffffff;
  border: 1px solid blue;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
}

.chatbot-button img {
  width: 30px;
  height: 30px;
}

.chatbot-window {
  position: fixed;
  bottom: 90px;
  right: 20px;
  width: 400px;
  height: 500px;
  background: #2c3e50; /* NavBar와 같은 어두운 블루 그레이 색상 */
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

.chatbot-header {
  background: #34495e; /* NavBar 하단 경계선과 같은 색상 */
  color: #ecf0f1; /* 밝은 회색 텍스트 색상 */
  padding: 10px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.close-button {
  background: transparent;
  border: none;
  color: #ecf0f1; /* 밝은 회색 텍스트 색상 */
  font-size: 20px;
  cursor: pointer;
}

.chatbot-body {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
  background: #ffffff; /* 채팅 내용 배경색을 NavBar 하단 경계선과 같은 색상으로 설정 */
}

.message {
  margin-bottom: 10px;
}

.message-content {
  padding: 10px;
  border-radius: 5px;
  color: #000000; /* 밝은 회색 텍스트 색상 */
}

.message-content.user {
  background: #d1ffd1;
  text-align: right;
}

.message-content.bot {
  background: #d1e0ff;
  text-align: left;
}

.chatbot-footer {
  display: flex;
  padding: 10px;
  border-top: 1px solid #2c3e50; /* NavBar와 같은 어두운 블루 그레이 색상 */
}

.chatbot-footer input {
  flex: 1;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #34495e; /* NavBar 하단 경계선과 같은 색상 */
  margin-right: 5px;
}

.chatbot-footer button {
  padding: 5px 10px;
  background: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
