
$(document).ready(function () {
    console.log('ready');
    let cfg = {
        "radius": 0.02,
        "maxOpacity": .4,
        "scaleRadius": true,
        "useLocalExtrema": false,
        latField: 'lat',
        lngField: 'lng',
        valueField: 'count'
    };

    let baseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });

    let barangaysLayer = L.layerGroup();
    let pumHeatmapLayer = new HeatmapOverlay(cfg);
    let map = new L.Map('map', {
        center: new L.LatLng(8.1724, 125.1559),
        zoom: 11,
        layers: [baseLayer, barangaysLayer, pumHeatmapLayer]
    });


    let focusToBarangay = function(lat, long) {
        map.flyTo([lat, long], 16);
    }

    $.get('/api/bulletin/latest', function (data) {
        $('#log-time').text(new Date(data.log_time).toLocaleString());
        $('#pum-total').text(data.pum_total);
        $('#pum-completed').text(data.pum_completed);
        $('#pum-ongoing').text(data.pum_ongoing);
        $('#pum-cleared').text(data.pum_cleared);

        $('#pui-total').text(data.pui_total);
        $('#pui-completed').text(data.pui_completed);
        $('#pui-admitted').text(data.pui_admitted);
        $('#pui-home').text(data.pui_home);
        $('#pui-cleared').text(data.pui_cleared);



        $('.count').each(function () {
            $(this).prop('Counter', 0).animate({
                Counter: $(this).text()
            }, {
                duration: 4000,
                easing: 'swing',
                step: function (now) {
                    $(this).text(Math.ceil(now));
                }
            });
        });

        let pumHeatData = {
            max: 8,
            data: []
        };

        data.cases.forEach((barCase, i) => {
            L.marker([barCase.barangay.latitude, barCase.barangay.longitude]).addTo(barangaysLayer)
                .bindPopup(`<div class="barangay-pin">
                            <p class="font-weight-bold">${barCase.barangay.name}</p>
                            <p class="text-warning font-weight-bold">PUM: ${barCase.pum}</p>
                            <p class="text-danger font-weight-bold">PUI: ${barCase.pui}</p></div>`);

            $('#barangay-list > ul:last-child')
                .append(`<li onclick="focusToBarangay(${barCase.barangay.latitude}, ${barCase.barangay.longitude})" class="list-group-item d-flex justify-content-between align-items-center list-group-item-action">
                    ${barCase.barangay.name}
                    <span><span class="badge badge-warning mr-1">${barCase.pum}</span><span class="badge badge-danger">${barCase.pui}</span></span></li>`);

            pumHeatData.data.push({lat: barCase.barangay.latitude, lng: barCase.barangay.longitude, count: barCase.pum});
        });

        pumHeatmapLayer.setData(pumHeatData);

        let overlays = {
            'Barangays': barangaysLayer,
		    'PUM Heatmap': pumHeatmapLayer
        };

        L.control.layers({}, overlays).addTo(map);
    });

});

