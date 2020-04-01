$(document).ready(function ($) {
    let lastDonePage =  '';
    let nextPage = '/api/timeline';
    let nextPageLoadDone = true;

    let addTimelineItems = function(items) {
        items.forEach((timelineItem) => {
            $('#covid-timeline')
                .append(`<div class="covid-timeline-block cssanimations">
                    <div class="covid-timeline-img bg-info d-flex justify-content-center align-items-center ${$('#covid-timeline').children().length < 1 ? 'bounce-in' : 'is-hidden'}">
                        <i class="fa fa-clock-o text-light"></i>
                    </div>
        
                    <div class="covid-timeline-content ${$('#covid-timeline').children().length < 1 ? 'bounce-in' : 'is-hidden'}">
                        <h2>${timelineItem.title}</h2>
                        <p class="text-justify">${timelineItem.text}</p>
                        <a href="${timelineItem.details_link}" class="covid-read-more btn btn-info" target="_blank">Read more</a>
                        <span class="covid-date">${new Date(timelineItem.entry_timestamp).toLocaleString()}</span>
                    </div>
                </div>`);
        });
    };

    let getTimelineItems = function(url) {
        $.get(url, function (data) {
            if (data.results.length > 0) {
                addTimelineItems(data.results);
            }
            lastDonePage = url;
            nextPage = data.next;
        });
    };

    $(document).ajaxStart(function () {
        nextPageLoadDone = false;
    });

    $(document).ajaxStop(function () {
        nextPageLoadDone = true;
    });

    $(window).scroll(function () {
        $('.covid-timeline-block').each(function () {
            if ($(this).offset().top <= $(window).scrollTop() + $(window).height() * 0.75 && $(this).find('.covid-timeline-img').hasClass('is-hidden')) {
                $(this).find('.covid-timeline-img, .covid-timeline-content').removeClass('is-hidden').addClass('bounce-in');
            }
        });
    });

    $(window).scroll(function () {
        if ($(document).height() - $(this).height() - 150 < $(this).scrollTop()) {
            if(nextPage && nextPageLoadDone && lastDonePage != nextPage) {
                getTimelineItems(nextPage);
            }
        }
    });

    getTimelineItems(nextPage);
});