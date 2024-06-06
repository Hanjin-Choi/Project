<template>
    <div>
        <h1>My Page</h1>
        <table class="table">
            <thead>
                <tr>
                <th scope="col"></th>
                <th scope="col"></th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <th scope="row">이름</th>
                <td colspan="2">{{ user.user.username }}</td>
                </tr>
                <tr>
                <th scope="row">Email</th>
                <td colspan="2">{{ user.user.email }}</td>
                </tr>
                <tr>
                <th scope="row">나이</th>
                <td colspan="2">{{ user.age }}</td>
                </tr>
                <tr>
                <th scope="row">자산</th>
                <td colspan="2">{{ user.asset }}</td>
                </tr>
                <tr>
                <th scope="row">연봉</th>
                <td colspan="2">{{ user.salary }}</td>
                </tr>
                <tr>
                <th scope="row">투자 성향</th>
                <td colspan="2">{{ user.ivst_taste }}</td>
                </tr>
                <tr>
                <th scope="row">최애 은행</th>
                <td colspan="2">{{ user.favorite}}</td>
                </tr>
            </tbody>
        </table>
        <h3>가입 상품 리스트</h3>
        <GraphItem v-for="product in prdtList" :product="product"/>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/auth'
import { useFinanceStore } from '@/stores/financeStore'
import GraphItem from '@/components/GraphItem.vue'

const user = useUserStore().user
const store = useFinanceStore()

const prdtList = ref([])

user.prdt_list.slice(1, -1).split(',').forEach(productId => {
    if (productId !== '') {
        prdtList.value.push(store.financeProductList.find(element => element.id == productId))
    }
})
</script>

<style scoped>

</style>