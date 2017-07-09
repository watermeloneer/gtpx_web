/**
 * Created by zdzmac on 2017/7/8.
 */
$(function () {
    /*
    页面初始化执行函数
     */
    dataList = '';
    chapterList();
    submitInfo();
    getChapterNumber();

})

/*
页面点击函数
 */

    function selectAll() {
        console.log(chapter);
        var url = '/problem/list/?page=1&&chapter=' + chapter;
        submitInfo(url);
    }//全部
    function selectSingle() {
        var url = '/problem/list/?page=1&&category=0&&chapter=' + chapter;
        submitInfo(url);
    }//单选题
    function selectMulti() {
        var url = '/problem/list/?page=1&&category=1&&chapter=' + chapter;
        submitInfo(url);
    }//多选题
    function selectJuage() {
        var url = '/problem/list/?page=1&&category=2&&chapter=' + chapter;
        submitInfo(url);
    }//判断题
    function switchLast() {
        var url = '/problem/list/?page='+ count +'&&category=' + categoryNum +'&&chapter=' + chapter;
        submitInfo(url);
    }//最后一题
    function switchFirst() {
        var url = '/problem/list/?page=1&&category=' + categoryNum +'&&chapter=' + chapter;
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
        selectAll();
        return chapter;
    }

/*
 切换题目
 */
    function submitInfo(url) {
        $.ajax({
                type:"GET",
                url:url,
                success : function (resopnse) {
                    var imgSrc = resopnse.results[0].images;
                    var Option = resopnse.results[0].choices;
                    var answer = resopnse.results[0].answers;
                    nextTitle = resopnse.next;
                    previousTitle = resopnse.previous;
                    var titleNum = GetRequest(nextTitle) - 1;
                    $('#titleImage').attr('src',imgSrc);
                    $("#titleOption").empty();
                    for(var i = 0; i<Option.length; i++){
                        $("#titleOption").append('<li class="clearfix"><span>'+ Option[i] +'</span></li>');
                    }

                    $('#answer').text('正确答案：'+ answer);
                    $('#titleNum').text('第 ' + titleNum + ' 题：');
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
                $("#chapterlist").remove();
                for(var i=0;i<chapterlist.length;i++){
                    $("#chapterlist").append('<option value="'+ i +'">'+ chapterlist[i]+'</option>');
                }
                $('#chapterlist option:first').attr('selected','selected');
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
        return strs[3];
    }

/*
 解析url中的题型值
 */
    function GetRequesttitle(url) {
        var url = url;
        if (url.indexOf("?") != -1)
        {
            var str = url.substr(1);
            strs = str.split("=");
        }
        return strs[1];
    }





