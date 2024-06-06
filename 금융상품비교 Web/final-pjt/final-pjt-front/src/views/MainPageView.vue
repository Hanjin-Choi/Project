<template>
  <div class="container my-5">
    <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="3000" @click="navigateTo('compare')">
          <img src="@/assets/main/bank.jpg" class="d-block w-100 carousel-img" alt="bank">
          <p class="hover-text">예금 비교</p>
        </div>
        <div class="carousel-item" data-bs-interval="3000" @click="navigateTo('calculate')">
          <img src="@/assets/main/exchange.jpg" class="d-block w-100 carousel-img" alt="exchange">
          <p class="hover-text">환율 계산기</p>
        </div>
        <div class="carousel-item" data-bs-interval="3000" @click="navigateTo('map')">
          <img src="@/assets/main/map.jpg" class="d-block w-100 carousel-img" alt="map">
          <p class="hover-text">은행 지도</p>
        </div>
        <div class="carousel-item" data-bs-interval="3000" @click="navigateTo('community-home')">
          <img src="@/assets/main/post.png" class="d-block w-100 carousel-img" alt="post">
          <p class="hover-text">게시판</p>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <div class="d-flex justify-content-around mt-5">
      <span class="feature">
        <img src="@/assets/main/social-media.png" alt="recommend" class="feature-img">
        <div class="feature-text">당신이 선호하는 은행의 다양한 금융 상품을 분석하여, 그 중에서 가장 적합한 제품을 추천해드립니다. 이를 통해 여러분의 금융 목표와 필요에 맞는 최적의 선택을 할 수 있도록 도와드립니다.</div>
      </span>
      <span class="feature">
        <img src="@/assets/main/artificial-intelligence.png" alt="bot" class="feature-img">
        <div class="feature-text">챗봇이 당신에게 다양한 금융 제품을 상세히 설명하고, 당신의 필요와 선호도에 맞는 최적의 제품을 추천해드립니다.</div>
      </span>
      <span class="feature">
        <img src="@/assets/main/block.png" alt="adblock" class="feature-img">
        <div class="feature-text">이 웹페이지는 사용자 경험을 최우선으로 생각하여 광고 없이 깔끔하고 쾌적하게 제공됩니다. 여러분은 방해 없이 필요한 정보와 서비스를 편안하게 이용하실 수 있습니다.</div>
      </span>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const navigateTo = (routeName) => {
  router.push({ name: routeName })
}
</script>

<style scoped>
body {
  font-family: 'Roboto', sans-serif;
  background-color: #f8f9fa;
  color: #212529;
  margin: 0;
  padding: 0;
}

.container {
  max-width: 80%;
}

.carousel {
  position: relative;
}

.carousel-inner {
  position: relative;
  width: 100%;
  overflow: hidden;
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.carousel-item {
  position: relative;
  transition: transform 0.5s ease, opacity 0.5s ease;
}

.carousel-img {
  width: 100%;
  height: 600px;
  object-fit: cover;
  filter: grayscale(50%) brightness(1);
  transition: filter 0.5s, transform 0.5s;
}

.carousel-item img:hover {
  filter: grayscale(0%) brightness(0.7);
  transform: scale(1.05);
  cursor: pointer;
}

.hover-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 2.5rem;
  font-weight: 700;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
  opacity: 0;
  transition: opacity 0.5s, transform 0.5s;
}

.carousel-item:hover .hover-text {
  opacity: 1;
  transform: translate(-50%, -50%) scale(1.1);
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  border-radius: 50%;
  width: 3rem;
  height: 3rem;
}

.carousel-control-prev,
.carousel-control-next {
  filter: none;
}

.carousel-control-prev:focus,
.carousel-control-next:focus {
  outline: none;
}

p.hover-text {
  font-size: 2.5rem;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin: 0;
  padding: 0;
  text-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.feature {
  text-align: center;
}

.feature-img {
  width: 12rem;
  margin-bottom: 1rem;
}

.feature-text {
  width: 12rem;
  text-align: justify;
  color: #495057;
  font-size: 1rem;
  line-height: 1.5;
}
</style>
