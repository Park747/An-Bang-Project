var HOME_PATH = windows.HOME_PATH || '.';


const building = [
    {'name': '고른햇살', 'latitude': 37.589388, 'longitude': 127.029079},
    {'name': '디어브래드', 'latitude': 37.587407, 'longitude': 127.028772}
]

var map = new naver.maps.Map('map', {
    center: new naver.maps.LatLng(37.5864913, 127.0288802),
    zoom: 10
});

var markers = [],
    infoWindows = [];

for (var item in building){
    var marker = new naver.maps.Marker({
        map: map,
        position: new naver.maps.LatLng(item['latitude'], item['longitude']),
        title: item['name'],
        icon: {
            url: HOME_PATH
        }
    });

    var infoWindow = new naver.maps.infoWindow({
        content: '<a href="https://map.naver.com/v5/entry/place/19886403?c=14140824.0342372,4521316.3551291,15,0,0,0,dh&placePath=%3Fentry=plt"><div style="width:150px;text-align:center;padding:10px;">"'+ item['name'] +'"</div></a>'
    });

    markers.push(marker);
    infoWindows.push(infoWindow);
}

naver.maps.Event.addListener(map, 'idle', function() {
    updateMarkers(map, markers);
});

function updateMarkers(map, markers) {

    var mapBounds = map.getBounds();
    var marker, position;

    for (var i = 0; i < markers.length; i++) {

        marker = markers[i]
        position = marker.getPosition();

        if (mapBounds.hasLatLng(position)) {
            showMarker(map, marker);
        } else {
            hideMarker(map, marker);
        }
    }
}

function showMarker(map, marker) {

    if (marker.setMap()) return;
    marker.setMap(map);
}

function hideMarker(map, marker) {

    if (!marker.setMap()) return;
    marker.setMap(null);
}

// 해당 마커의 인덱스를 seq라는 클로저 변수로 저장하는 이벤트 핸들러를 반환합니다.
function getClickHandler(seq) {
    return function(e) {
        var marker = markers[seq],
            infoWindow = infoWindows[seq];

        if (infoWindow.getMap()) {
            infoWindow.close();
        } else {
            infoWindow.open(map, marker);
        }
    }
}

for (var i=0, ii=markers.length; i<ii; i++) {
    naver.maps.Event.addListener(markers[i], 'click', getClickHandler(i));
}

var marker = new naver.maps.Marker({
    position: new naver.maps.LatLng(37.3595704, 127.105399),
    map: map
});
