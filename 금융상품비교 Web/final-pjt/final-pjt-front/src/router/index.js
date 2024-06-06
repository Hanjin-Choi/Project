import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/auth'

import MainPageView from '@/views/MainPageView.vue'
import MapView from '@/views/MapView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import CommunityView from '@/views/CommunityView.vue'
import ProfileView from '@/views/ProfileView.vue'
import PortfolioView from '@/views/PortfolioView.vue'
import CalculateView from '@/views/CalculateView.vue'
import CompareView from '@/views/CompareView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue'
import CreateCategoryView from '@/views/CreateCategoryView.vue'
import CreatePostView from '@/views/CreatePostView.vue'
import CommunityHome from '@/components/CommunityHome.vue'
import CategoryDetailView from '@/components/CategoryDetailView.vue'
import Recommend from '@/components/Recommend.vue'
import UserEdit from '@/components/UserEdit.vue'
import MyPage from '@/components/MyPage.vue'
import PostDetail from '@/components/PostDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'mainpage',
      component: MainPageView
    },
    {
      path : '/signup',
      name : 'signup',
      component : SignUpView
    },
    {
      path : '/portfolio/:userName',
      name : 'portfolio',
      component : PortfolioView,
    },
    {
      path : '/login',
      name : 'login',
      component : LogInView,
    },
    {
      path : '/profile',
      component : ProfileView,
      children : [
        {
          path : '',
          name : 'profile',
          component : MyPage,
        },
        {
          path : '/edit',
          name : 'profile-edit',
          component : UserEdit,
        },
        {
          path : '/recommend',
          name : 'profile-recommend',
          component : Recommend,
        },
      ]
    },
    {
      path : '/compare',
      name : 'compare',
      component : CompareView,
    },
    {
      path : '/compare/:fin_prdt_cd',
      name : 'compareDetail',
      component : ProductDetailView,
    },
    {
      path : '/calculate',
      name : 'calculate',
      component : CalculateView
    },
    {
      path : '/map',
      name : 'map',
      component : MapView
    },
    {
      path : '/Community',
      name : 'community',
      component : CommunityView,
      children: [
        { path: '', name: 'community-home', component: CommunityHome },
        { path: '/:categoryName', name:'eachCategory', component: CategoryDetailView },
        { path:'/community/:postId', name:'postDetail',component:PostDetail},
        {path:'/community/:postId/update', name:'postUpdate',component:CreatePostView},
      ]
    },
    {
      path : '/category',
      name : 'category',
      component : CreateCategoryView
    },
    {
      path : '/createPost',
      name : 'createPost',
      component : CreatePostView
    },
  ]
})

router.beforeEach((to, from) => {
  const store=useUserStore()
  if ((to.name === 'signup' || to.name === 'login') && store.isAuthenticated) {
    window.alert('로그인 중입니다.')
    return { name :'mainpage' }
  }

  if (from.name === 'portfolio' && store.isAuthenticated && !store.user) {
    return false
  }

  if ((
    to.name === 'compare'
    || to.name === 'community'
    || to.name === 'community-home'
    || to.name === 'postDetail'
    || to.name === 'postUpdate'
    || to.name === 'createPost'
    || to.name === 'compareDetail'
    || to.name === 'profile'
    || to.name === 'profile-edit'
    || to.name === 'profile-recommend'
    || to.name === 'portfolio'
  ) && !store.isAuthenticated) {
    window.alert('로그인이 필요합니다.')
    return { name: 'login' }
  }

  if ((to.name === 'category') && (!store.isAuthenticated || !store.user || !store.user.user.is_superuser)) {
    window.alert('관리자 계정이 아닙니다.')
    return { name: 'mainpage' }
  }
})

export default router
