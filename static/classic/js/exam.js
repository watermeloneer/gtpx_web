/**
 * Created by zdzmac on 2017/8/9.
 */

$(document).ready(function () {
    titleList = new Array(100);
    for(var i=0;i<100;i++){
        titleList[i] = "";
    }
    examInit.titleInit(titleList);
    examInit.pkListInit();
    load = 0;
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
})
var time = 2700000;
setInterval(function () {
    var nowtime = new Date();
    if(time >= 1000 ){
        time = time - 1000;
    }else{
        time = 0;
    }
    var minute = parseInt(time / 1000 / 60 % 60);
    var seconds = parseInt(time / 1000 % 60);
    $('.timespan').html(minute + ":" + seconds);
}, 1000);



var examInit = {
    titleInit:function (arr) {
        $(".em-modal-contain").empty();
        var htmlStr = "";
        var str = [];
        for(var i = 0;i < arr.length;i++){
            if(arr[i].useranswers == undefined || arr[i].useranswers == ""){
                str[i] = '<div class="btn-docker">'+'<span class="title-btn ans-btn">'+ (i+1) +'</span>'+'</div>';
                htmlStr = str.join("");
            }else{
                if(arr[i].useranswers == arr[i].answers){
                    str[i] = '<div class="btn-docker">'+'<span class="title-btn-right ans-btn">'+ (i+1) +'</span>'+'</div>';
                    htmlStr = str.join("");
                }else if(arr[i].useranswers != arr[i].answers){
                    str[i] = '<div class="btn-docker">'+'<span class="title-btn-error ans-btn">'+ (i+1) +'</span>'+'</div>';
                    htmlStr = str.join("");
                }
            }
        }
        $(".em-modal-contain").append(htmlStr);
        $(".ans-btn").click(function () {
            examInit.maskClick();
            if(load == 0){
                load = 1;
                var titleNum = $(this).text();
                var pk = scope_pklist[titleNum-1];
                examInit.titleBtn(pk,titleNum);
            }
        })
    },
    pkListInit:function () {
        var url = '/exams/problems/list/';
        $.ajax({
            type:"GET",
            url:url,
            success:function (response) {
                scope_pklist = response;
                examInit.titleBtn(scope_pklist[0],1);
            }
        })
    },
    maskClick:function () {
        $(".em-modal").animate({height:"0"});
        $(".em-modal-header").hide();
        $(".em-mask").hide();
    },
    titleBtn:function (pk,titleNum) {
        var num = titleNum -1;
        if(titleList[num] == ""){
            var url = '/problem/'+pk;
            $.ajax({
                type:"GET",
                url:url,
                success:function (response) {
                    takeTitle(response,num);
                }
            })
        }else{
            if(num < 100){
                takeTitle(titleList[num],num);
            }

        }
    }
}


function  switchNext() {
    var title = $('#titleNum').text();
    var titlenum = title.replace(/[^0-9]/ig,"");
    var errorTitleNum = 0;
    var rightTitleNum = 0;
    if(titlenum <= 100){
        var answer = "";
        $(".clearfix").each(function(){
            if($(this).hasClass('answer-active')){
                var index = $(this).index();
                switch (index){
                    case 0:
                        answer =  answer + 'A'
                        break;
                    case 1:
                        answer =  answer + 'B'
                        break;
                    case 2:
                        answer =  answer + 'C'
                        break;
                    case 3:
                        answer =  answer + 'D'
                        break;

                }
            }
        })
        if(titleList[titlenum - 1].useranswers == undefined || titleList[titlenum - 1].useranswers == ""){
            titleList[titlenum - 1].useranswers = answer;
        }
        for(var i = 0; i<=99; i++){
            if(titleList[i].useranswers == undefined || titleList[i].useranswers == ""){

            }else{
                if(titleList[i].useranswers == titleList[i].answers){
                    rightTitleNum = rightTitleNum + 1;
                }else {
                    errorTitleNum = errorTitleNum + 1;
                }

            }
        }
        var total = rightTitleNum + errorTitleNum;
        $("#em-right").text(rightTitleNum);
        $("#em-error").text(errorTitleNum);
        $("#em-percent").text(total + '/100');
        $("#em-right1").text(rightTitleNum);
        $("#em-error1").text(errorTitleNum);
        $("#em-percent1").text(total + '/100');
        var pk = scope_pklist[titlenum];
        var nexttitle = titlenum - (-1);
        examInit.titleBtn(pk, nexttitle);
        examInit.titleInit(titleList);
    }
}

function takeTitle(response,num) {
    titleList[num] = response;
    sessionStorage.titleList = titleList;
    $("#titleOption").empty();
    $("#modal1").css("display","none");
    var imgSrc = response.images;
    var Option = response.choices;
    var answer = response.answers;
    var titlestr = response.title;
    if(response.useranswers == undefined || response.useranswers == ""){
        $('#useranswer').text("");
        $('#answer').text("");
    }else{
        var useranswer = response.useranswers;
        $('#useranswer').text('已选答案：'+ useranswer);
        $('#answer').text('正确答案：'+ answer);
    }
    if(imgSrc != null){
        $('#titleImage').css('display','block');
        $('#titleImage').attr('src',imgSrc);
    }else{
        $('#titleImage').css('display','none');
    }
    for(var i = 0; i<Option.length; i++){
        $("#titleOption").append('<li class="clearfix">'+ Option[i] +'</li>');
    }
    $("#title").text(titlestr);
    $('#titleNum').text('第 ' + (num+1) + ' 题：');
    $("#modal1").css("display","none");
    load = 0;
    $('.clearfix').click(function () {
        if($(this).hasClass('answer-active') == false){
            $(this).addClass('answer-active');
        }else{
            $(this).removeClass('answer-active');
        }
    })
}


function emSubmit() {
    var grade = $("#em-right").text();
    alert('测试分数：'+grade+"分    三秒后返回首页");
    setTimeout(function () {
        window.location.href = '/'
    },3000)
}
