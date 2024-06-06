<template>
    <div class="container mt-4">
        <div class="row">
            <h1>주변 은행 한눈에 보기</h1>
            <hr>
            <div class="select col-2">
                <Mapselect @msg="search"/>
            </div>
            <div class="mapview container col-10">
                <div id="map"></div>
            </div>
        </div>
    </div>
</template>


<script setup>

import { computed, ref, watch, onMounted } from 'vue';
import Mapselect from '@/components/Mapselect.vue';
const keyword = ref('')
const MAP_API=import.meta.env.VITE_KAKAO_API_KEY
const location=ref(null)
let map = null;
let infowindow = null
onMounted(() => {
  if (window.kakao && window.kakao.maps) {
    initMap();
  } else {
    const script = document.createElement('script');
    /* global kakao */
    script.onload = () => kakao.maps.load(initMap);
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${MAP_API}&libraries=services`;
    document.head.appendChild(script);
  }
});

const initMap = () => {
  const container = document.getElementById('map');
  const options = {
    center: new kakao.maps.LatLng(37.50126474, 127.039581),
    level: 3,
  };
  var markerPosition  = new kakao.maps.LatLng(37.5012647456244, 127.03958123605); 
  var marker = new kakao.maps.Marker({
    position: markerPosition
});
  // 지도 객체를 등록합니다.
  // 지도 객체는 반응형 관리 대상이 아니므로 initMap에서 선언합니다.
  map = new kakao.maps.Map(container, options);
//  
  marker.setMap(map);

  var iwContent = '<div style="padding:5px;">SSAFY!</div>', // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
    iwPosition = new kakao.maps.LatLng(37.5012647456244, 127.03958123605), //인포윈도우 표시 위치입니다
    iwRemoveable = true; // removeable 속성을 ture 로 설정하면 인포윈도우를 닫을 수 있는 x버튼이 표시됩니다
var infowindow = new kakao.maps.InfoWindow({
    map: map, // 인포윈도우가 표시될 지도
    position : iwPosition, 
    content : iwContent,
    removable : iwRemoveable
});
infowindow.open(map, marker); 
};
const search=function(args){
    keyword.value = args
    console.log(map.value)
    // 장소 검색 객체를 생성합니다
    var ps = new kakao.maps.services.Places(); 
    infowindow = new kakao.maps.InfoWindow({zIndex:1})
// 키워드로 장소를 검색합니다
    ps.keywordSearch(keyword.value, placesSearchCB); 

}  
// 키워드 검색 완료 시 호출되는 콜백함수 입니다
    function placesSearchCB (data, status, pagination) {
        if (status === kakao.maps.services.Status.OK) {

            // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
            // LatLngBounds 객체에 좌표를 추가합니다
            var bounds = new kakao.maps.LatLngBounds();

            for (var i=0; i<data.length; i++) {
                displayMarker(data[i]);    
                bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
            }       
            console.log(bounds)
            // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
            map.setBounds(bounds);
        } 

// 지도에 마커를 표시하는 함수입니다
    function displayMarker(place) {
    
    // 마커를 생성하고 지도에 표시합니다
    var marker = new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(place.y, place.x) 
    });

    // 마커에 클릭이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function() {
        // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
        infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
        infowindow.open(map, marker);
    });
}

}
</script>

<style scoped>
.select {
    display: inline-block;
    border-right: 1px solid skyblue;
}
.mapview{
    display: inline-block;
}
#map {
  width: 100%;
  height: 600px;
}
</style>