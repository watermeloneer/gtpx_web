/**
 * Created by zdzmac on 2017/8/9.
 */

$(document).ready(function () {
    examInit.titleInit();
    pkList = $("#titlePK").val();
    var str = pkList.split(',');
    console.log(str[0]);
    $(".em-percent").click(function () {
        $(".em-modal").animate({height:"60vh"});
        $(".em-modal-header").show("1000");
        $(".em-mask").show();
    })
    $(".em-error").click(function () {
        $(".em-modal").animate({height:"60vh"});
        $(".em-modal-header").show("1000");
        $(".em-mask").show();
    })
    $(".em-right").click(function () {
        $(".em-modal").animate({height:"60vh"});
        $(".em-modal-header").show("1000");
        $(".em-mask").show();
    })

    $(".title-btn").click(function () {
        var titleNum = $(this).text();
        console.log(titleNum);
    })
})

var titleList = new Array();
var starttime = new Date("2017/11/20");
setInterval(function () {
    var nowtime = new Date();
    var time = starttime - nowtime;
    var minute = parseInt(time / 1000 / 60 % 60);
    var seconds = parseInt(time / 1000 % 60);
    $('.timespan').html(minute + ":" + seconds);
}, 1000);



var examInit = {
    titleInit:function () {
        var htmlStr = "";
        var str = [];
        for(var i = 0;i < 100;i++){
            str[i] = '<div class="btn-docker">'+'<span class="title-btn">'+ (i+1) +'</span>'+'</div>';
            htmlStr = str.join("");
        }
        $(".em-modal-contain").append(htmlStr);
    }
}

function maskClick() {
    $(".em-modal").animate({height:"0"});
    $(".em-modal-header").hide();
    $(".em-mask").hide();
}
