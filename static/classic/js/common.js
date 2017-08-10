/**
 * Created by zdzmac on 2017/7/8.
 */
$(function () {
    level = $("#leveldata").val();
    dataList = '';
    chapter = "";
    categoryNum = 0;
    chapterList();
    getChapterNumber();
    //$("#chapterlist option:first").prop("selected", 'selected');
    //$('#chapterlist').find('option').eq(0).attr("selected","selected");
});

/*
 页面点击函数
 */

//$("#chapterlist option:first").prop("selected", 'selected');
//$('#chapterlist').find('option').eq(0).attr("selected","selected");

/*
 页面点击函数
 */
function selectAll(index) {
    controlBtn(index);
    categoryNum = -1;
    var url = '/problem/list/?chapter=' + chapter + '&level=' + level;
    submitInfo(url);
}//全部
function selectSingle(index) {
    controlBtn(index);
    categoryNum = 0;
    var url = '/problem/list/?page=1&category=0&chapter=' + chapter + '&level=' + level;
    submitInfo(url);
}//单选题
function selectMulti(index) {
    controlBtn(index);
    categoryNum = 2;
    var url = '/problem/list/?page=1&category=2&chapter=' + chapter + '&level=' + level;
    submitInfo(url);
}//多选题
function selectJuage(index) {
    controlBtn(index);
    categoryNum = 1;
    var url = '/problem/list/?page=1&category=1&chapter=' + chapter + '&level=' + level;
    submitInfo(url);
}//判断题
function switchLast() {
    if(categoryNum == -1){
        var url = '/problem/list/?page='+ count +'&chapter=' + chapter + '&level=' +
            level;
    }else{
        var url = '/problem/list/?page='+ count +'&category=' + categoryNum +'&chapter=' + chapter + '&level=' +
            level;
    }
    submitInfo(url);
}//最后一题
function switchFirst() {
    var url = '/problem/list/?chapter='+chapter+'&category='+categoryNum + '&level=' + level;
    submitInfo(url);
}//第一题
function switchPre() {
    if(previousTitle != null){
        submitInfo(previousTitle);
    }
}//上一题
function switchNext() {
    if(nextTitle != null){
        submitInfo(nextTitle);
    }
}//下一题

/*
 获取选中章节
 */
function getChapterNumber() {
    chapter = $('#chapterlist option:selected').val();
    if(chapter == undefined){
        chapter = 0;
    }else{
    }
    selectAll(0);
    return chapter;
}

/*
 切换题目
 */
function submitInfo(url) {
    $("#modal1").css("display","block");
    $.ajax({
            type:"GET",
            url:url,
            success : function (resopnse) {
                $("#titleOption").empty();
                if(resopnse.count == 0){
                    $(".notitle").css("display","block");
                    $(".wel-main").css("display","none");
                    $("#modal1").css("display","none");
                }else{
                    $(".wel-main").css("display","block");
                    $(".notitle").css("display","none");
                    var imgSrc = resopnse.results[0].images;
                    var Option = resopnse.results[0].choices;
                    var answer = resopnse.results[0].answers;
                    var titlestr = resopnse.results[0].title;
//                        var titles  = titlestr.substr(1);
//                        var title = titles.split("、");
//                        var titlesub = "";
//                        for(var i =1; i<title.length;i++){
//                            titlesub+=title[i];
//                        }
                    nextTitle = resopnse.next;
                    previousTitle = resopnse.previous;
                    count = resopnse.count;
                    if(nextTitle != null){
                        var titleNum = GetRequest(nextTitle,'page') - 1;
                    }else if(previousTitle != null && nextTitle == null){
                        var titleNum = GetRequest(previousTitle,'page') - (-1);
                    }else {
                        var titleNum = 1;
                    }
                    if(imgSrc != null){
                        $('#titleImage').css('display','block');
                        $('#titleImage').attr('src',imgSrc);
                    }else{
                        $('#titleImage').css('display','none');
                    }
                    for(var i = 0; i<Option.length; i++){
                        $("#titleOption").append('<li class="clearfix"><span>'+ Option[i] +'</span></li>');
                    }
                    $("#title").text(titlestr);
                    $('#answer').text('正确答案：'+ answer);
                    $('#totalcount').text('总共：'+ count + '题');
                    $('#titleNum').text('第 ' + titleNum + ' 题：');
                    $("#modal1").css("display","none");
                }

            }
        }
    )
}


/*
 获取章节列表
 */
function chapterList() {
    $.ajax({
        type:"GET",
        url:"/problem/chapters/list?level=" + level ,
        success: function (response) {
            var chapterlist = response.results;
            for(var i=0;i<chapterlist.length;i++){
                $("#chapterlist").append('<option value="'+ chapterlist[i].num +'">'+ chapterlist[i].name+'</option>');
            }
            // $('#chapterlist option:first').attr('selected','selected');
            // $('#chapterlist').find('option').eq(0).attr("selected","selected");
            // chapter = 0;
        }
    })
}


/*
 正则解析url方法二
 */
function GetRequest(url,param) {
    var urlarr = url.split("?");
    var urlstr = urlarr[1]; //获取url中"?"符后的字串
    var urlpage = urlstr.split("&");
    var paramvalue = '';
    for(var i=0;i<urlpage.length;i++){
        var arr = urlpage[i].split("=");
        if(arr[0] == param){
            paramvalue = arr[1];
        }
    }
    return paramvalue;
}
/*
 头部按钮样式控制
 */

function controlBtn(index) {
    $("#welmainbtn button:eq(" + index + ")").addClass('topicTypebtn_active').removeClass("topicTypebtn");
    $("#welmainbtn button:eq(" + index + ")").siblings().addClass('topicTypebtn').removeClass("topicTypebtn_active");
}





