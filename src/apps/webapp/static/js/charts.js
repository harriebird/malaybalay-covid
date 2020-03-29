
$(document).ready(function () {
    console.log('ready');

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

        barangayPum = {values: [], labels: [], type: 'pie'};
        barangayPui = {values: [], labels: [], type: 'pie'};

        caseScatter = {x: [], y: [], text:[], mode: 'markers', type: 'scatter'};

        data.cases.forEach((barCase) => {
            if(barCase.pum > 0) {
                barangayPum.values.push(barCase.pum);
                barangayPum.labels.push(barCase.barangay.name);
            }

            if(barCase.pui > 0) {
                barangayPui.values.push(barCase.pui);
                barangayPui.labels.push(barCase.barangay.name);
            }

            caseScatter.x.push(barCase.pum);
            caseScatter.y.push(barCase.pui);
            caseScatter.text.push(barCase.barangay.name);
        });

        Plotly.newPlot('baragay-pum-pie', [barangayPum], {title: 'Barangay PUM Pie Chart'}, {responsive: true, font: {family: 'Roboto'}});
        Plotly.newPlot('baragay-pui-pie', [barangayPui], {title: 'Barangay PUI Pie Chart'}, {responsive: true});


        let topPums = [...data.cases];
        let topPuis = [...data.cases];
        topPums.sort((a, b) => b.pum - a.pum);
        topPuis.sort((a, b) => b.pui - a.pui);

        topPums = topPums.slice(0, 10);
        topPuis = topPuis.slice(0, 10);

        topPums.forEach((topPum, i) => {
            $('#top-10-pum > ul:last-child')
                .append(`<li class="list-group-item d-flex justify-content-between align-items-center list-group-item-action">
                    ${i+1}. ${topPum.barangay.name}
                    <span class="badge badge-warning">${topPum.pum} PUM${topPum.pum > 1 ? 's' : ''}</span>`);
        });

        topPuis.forEach((topPui, i) => {
            $('#top-10-pui > ul:last-child')
                .append(`<li class="list-group-item d-flex justify-content-between align-items-center list-group-item-action">
                    ${i+1}. ${topPui.barangay.name}
                    <span class="badge badge-danger">${topPui.pui} PUI${topPui.pui > 1 ? 's' : ''}</span>`);
        });

        $('#top-10-pum  h3').text('TOP 10 PUM BARANGAYS');
        $('#top-10-pui  h3').text('TOP 10 PUI BARANGAYS');

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
    });

    $.get('/api/bulletin/daily', function (data) {
        let pumTotal = {x: [], y: [], name: 'Total PUM'};
        let pumCompleted = {x: [], y: [], name: 'Completed'};
        let pumCleared = {x: [], y: [], name: 'Cleared'};
        let pumOngoing = {x: [], y: [], name: 'Ongoing'};

        let puiTotal = {x: [], y: [], name: 'Total PUI'};
        let puiAdmitted = {x: [], y: [], name: 'Admitted'}
        let puiCleared = {x: [], y: [], name: 'Cleared'};
        let puiHome = {x: [], y: [], name: 'Home Quarantine'};
        let puiCompleted = {x: [], y: [], name: 'Completed'};

        data.forEach((dailyStat) => {
            let statDate = new Date(dailyStat.log_time).toLocaleDateString();
            pumTotal.x.push(statDate);
            pumTotal.y.push(dailyStat.pum_total);
            pumCompleted.y.push(dailyStat.pum_completed);
            pumCleared.y.push(dailyStat.pum_cleared);
            pumOngoing.y.push(dailyStat.pum_ongoing);

            puiTotal.y.push(dailyStat.pui_total);
            puiAdmitted.y.push(dailyStat.pui_admitted);
            puiCleared.y.push(dailyStat.pui_cleared);
            puiHome.y.push(dailyStat.pui_home);
            puiCompleted.y.push(dailyStat.pui_completed);
        });

        pumCompleted.x = pumTotal.x;
        pumCleared.x = pumTotal.x;
        pumOngoing.x = pumTotal.x;

        puiTotal.x = pumTotal.x;
        puiAdmitted.x = pumTotal.x;
        puiCleared.x = pumTotal.x;
        puiHome.x = pumTotal.x;
        puiCompleted.x = pumTotal.x;

        Plotly.newPlot('overall-pum-chart', [pumTotal, pumCompleted, pumCleared, pumOngoing], {title: 'PUM Daily Chart'}, {responsive: true});
        Plotly.newPlot('overall-pui-chart', [puiTotal, puiAdmitted, puiCleared, puiHome, puiCompleted], {title: 'PUI Daily Chart'}, {responsive: true});
    });

});

