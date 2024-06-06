<template>
    <form @submit.prevent="search">
        <label class="form-label" for="city">광역시/도</label>
        <br>
        <select class="form-select" v-model="city" id="city">
            <option v-for="city in cityInfo">{{city.name}}</option>
        </select>
        <br>
        <label class="form-label" for="area">시 / 군 / 구</label>
        <br>
        <select class="form-select" v-model="area" id="area">
            <option v-for="area in arealist[0].area">{{ area }}</option>
        </select>
        <br>
        <label class="form-label" for="bank">은행</label>
        <br>
        <select class="form-select" v-model='bank' id="bank">
            <option v-for="bank in bankInfo">{{ bank }}</option>
        </select>
        <br>
        <hr>
        <button type="submit" class="btn btn-primary">검색</button>
    </form>
</template>


<script setup>
import { computed, ref, watch } from 'vue';
const cityInfo =ref([
{name:'서울특별시',area:['종로구','중구','용산구','성동구','광진구','동대문구','중랑구',
'성북구','강북구','도봉구','노원구','은평구','서대문구','마포구',
'양천구','강서구','구로구','금천구','영등포구',
'동작구','관악구','서초구','강남구','송파구','강동구']},
{name:'부산광역시',area:['중구','서구','동구','영도구','부산진구',
'동래구','남구','북구','해운대구','사하구',
'금정구','강서구','연제구','수영구','사상구','기장군']},
{name:'대구광역시', area:['중구','서구','동구','남구','북구','수성구','달서구','달성군']},
{name:'인천광역시', area:['중구','동구','미추홀구','연수구','남동구','부평구','계양구','서구','강화군','옹진군']},
{name:'광주광역시', area:['동구','서구','남구','북구','광산구']},
{name:'대전광역시', area:['동구','중구','서구','유성구','대덕구']},
{name:'울산광역시', area:['중구','남구','동구','북구','울주군']},
{name:'세종특별자치시', area:['']},
{name:'경기도', area:['수원시','성남시','의정부시','안양시','부천시','광명시','평택시',
    '동두천시','안산시','고양시','과천시','구리시','남양주시','오산시','시흥시','군포시','의왕시','하남시','용인시',
    '파주시','이천시','안성시','김포시','화성시','광주시','양주시','포천시','여주시','연천군','가평군','양평군',
]},
{name:'강원특별자치도', area:['춘천시','원주시','강릉시','동해시','태백시','속초시','삼척시','홍천군','횡성군','영월군','평창군','정선군','철원군','화천군','양구군','인제군','고성군','양양군']},
{name:'충청북도', area:['청주시','충주시','제천시','보은군','옥천군','영동군','증평군','진천군','괴산군','음성군','단양군']},
{name:'충청남도', area:['천안시','공주시','당진시','보령시','아산시','서산시','논산시','계룡시','금산군','부여군','서천군','청양군','홍성군','예산군','태안군']},
{name:'전라북도', area:['전주시','군산시','익산시','정읍시','남원시','김제시','완주군','진안군','무주군','장수군','임실군','순창군','고창군','부안군']},
{name:'전라남도', area:['목포시','여수시','순천시','나주시','광양시','담양군','곡성군','구례군','고흥군','보성군','화순군','장흥군','강진군','해남군','영암군','무안군','함평군','영광군','장성군','완도군','진도군','신안군']},
{name:'경상북도', area:['포항시','경주시','김천시','안동시','구미시','영주시','영천시','상주시','문경시','경산시','군위군','의성군','청송군','영양군','영덕군','청도군','고령군','성주군','칠곡군','예천군','봉화군','울진군','울릉군']},
{name:'경상남도', area:['창원시','진주시','통영시','사천시','김해시','밀양시','거제시','양산시','의령군','함안군','창녕군','고성군','남해군','하동군','산청군','함양군','거창군','합천군']},
{name:'제주특별자치도', area:['제주시','서귀포시']},
])
const bankInfo = ref([
    '국민은행','KEB하나은행','SC제일은행','신한은행','외환은행','우리은행','한국시티은행',
    '경남은행','광주은행','대구은행','부산은행','전북은행','제주은행',
    '기업은행','농협','수협','한국산업은행','한국수출입은행',
])

const city = ref('서울특별시')
const bank = ref('신한은행')
const arealist = computed(() => {
    return cityInfo.value.filter(elem => elem.name ===city.value)
})
const area = ref(arealist.value[0].area[0])
watch(city,()=>{area.value =arealist.value[0].area[0]})

const msg=ref('')
const emit=defineEmits(['msg'])
const search =function(){
    msg.value = `${city.value} ${area.value} ${bank.value}`
    emit('msg',msg.value)
}
</script>

<style scoped>
.select {
    display: inline-block;
}
.map{
    display: inline-block;
}

</style>