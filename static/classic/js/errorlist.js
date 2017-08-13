/**
 * Created by zdzmac on 2017/8/13.
 */

$(function () {
    errorlist.takeTitlepk();
})


window_errorpk = [];
window_current = 1;
var errorlist = {
    takeTitlepk : function () {
       $.ajax({
           url:'/exams/error/list/',
           type:'GET',
           success:function (response) {
               window_errorpk = response;
               errorlist.takeTitle(window_errorpk[0],0);
           }
       })
    },
    takeTitle:function (pk,num) {
        $.ajax({
            url:'/problem/'+pk,
            type:'GET',
            success:function (response) {
                var errortitle = response;
                takeTitle(errortitle,num)
            }
        })
    }
}

function takeTitle(response,num) {
    $("#titleOption").empty();
    $("#modal1").css("display","none");
    var imgSrc = response.images;
    var Option = response.choices;
    var answer = response.answers;
    var titlestr = response.title;
    var titleType = response.category;
    $('#answer').text('正确答案：'+ answer);
    if(imgSrc != null){
        $('#titleImage').css('display','block');
        $('#titleImage').attr('src',imgSrc);
    }else{
        $('#titleImage').css('display','none');
    }
    for(var i = 0; i<Option.length; i++){
        $("#titleOption").append('<li class="clearfix">'+ Option[i] +'</li>');
    }
    $("#title").text(titlestr + '--' + titleType);
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

function switchFirst() {
    window_current = 1;
    var pk = window_errorpk[0];
    errorlist.takeTitle(pk,0);
}

function switchPre() {
    window_current = window_current - 1;
    var num = window_current - 1;
    if(num >=0){
        var pk = window_errorpk[num];
        errorlist.takeTitle(pk,num);
    }
}

function switchNext() {
    window_current = window_current - (-1);
    var num = window_current - 1;
    if(num < window_errorpk.length){
        var pk = window_errorpk[num];
        errorlist.takeTitle(pk,num);
    }
}

function switchLast() {
    window_current = window_errorpk.length;
    var num = window_current - 1;
    var pk = window_errorpk[num];
    errorlist.takeTitle(pk,num);
}


