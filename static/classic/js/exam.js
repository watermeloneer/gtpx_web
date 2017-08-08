/**
 * Created by zdzmac on 2017/8/9.
 */

$(document).ready(function () {
    examInit.titleInit();
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
