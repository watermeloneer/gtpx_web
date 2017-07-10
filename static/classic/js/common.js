/**
 * Created by zdzmac on 2017/7/8.
 */
$(function () {
    /*
     页面初始化执行函数
     */
    dataList = '';
    chapter = "";
    chapterList();
    getChapterNumber();
    //$("#chapterlist option:first").prop("selected", 'selected');
    //$('#chapterlist').find('option').eq(0).attr("selected","selected");
});

/*
 页面点击函数
 */

function selectAll(index) {
    controlBtn(index);
    var url = '/problem/list/?chapter=' + chapter +'&category=0';
    submitInfo(url);
}//全部
function selectSingle(index) {
    controlBtn(index);
    var url = '/problem/list/?page=1&category=0&chapter=' + chapter;
    submitInfo(url);
}//单选题
function selectMulti(index) {
    controlBtn(index);
    var url = '/problem/list/?page=1&category=2&chapter=' + chapter;
    submitInfo(url);
}//多选题
function selectJuage(index) {
    controlBtn(index);
    var url = '/problem/list/?page=1&category=1&chapter=' + chapter;
    submitInfo(url);
}//判断题
function switchLast() {
    var url = '/problem/list/?page='+ count +'&category=' + categoryNum +'&chapter=' + chapter;
    submitInfo(url);
}//最后一题
function switchFirst() {
    var url = '/problem/list/?chapter='+chapter+'&category='+categoryNum;
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
                }else{
                    $(".wel-main").css("display","block");
                    $(".notitle").css("display","none");
                    var imgSrc = resopnse.results[0].images;
                    var Option = resopnse.results[0].choices;
                    var answer = resopnse.results[0].answers;
                    var titlestr = resopnse.results[0].title;
                    var titles  = titlestr.substr(1);
                    var title = titles.split("、");
                    nextTitle = resopnse.next;
                    previousTitle = resopnse.previous;
                    count = resopnse.count;
                    if(nextTitle != null){
                        categoryNum = GetRequesttitle(nextTitle);
                        var titleNum = GetRequest(nextTitle) - 1;
                    }else{
                        categoryNum = GetRequesttitle(previousTitle);
                        var titleNum = GetRequest(previousTitle) - (-1);
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
                    $("#title").text(title);
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
        url:"/problem/chapters/list",
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
 解析url中的page值，显示题号
 */
function GetRequest(url) {
    var url = url;
    if (url.indexOf("?") != -1)
    {
        var str = url.substr(1);
        strs = str.split("=");
    }
    if(strs[3] == undefined){
        return strs[2];

    }else{
         return strs[3];

    }

}

/*
正则解析url
 */

function GetQueryString(name,url)
{
     var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
     var r = url.substr(1).match(reg);
     if(r!=null)return  unescape(r[2]); return null;
}

/*
 解析url中的题型值
 */
function GetRequesttitle(url) {
    var url = url;
    if (url.indexOf("?") != -1)
    {
        var str = url.substr(1);
        strss = str.split("=");
    }
    console.log(strss[3]);
    if(strss[3] == undefined){
        var value = strss[1].replace(/[^0-9]/ig,"");
         return value;

    }else{
        var value = strss[1].replace(/[^0-9]/ig,"");
         return value;

    }

}

/*
 头部按钮样式控制
 */

function controlBtn(index) {
    $("#welmainbtn button:eq(" + index + ")").addClass('topicTypebtn_active').removeClass("topicTypebtn");
    $("#welmainbtn button:eq(" + index + ")").siblings().addClass('topicTypebtn').removeClass("topicTypebtn_active");
}





