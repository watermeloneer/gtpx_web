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
    function chapterListtest() {
        var response = {
            "count": 10,
            "next": null,
            "previous": null,
            "results": [
                {
                    "num": 0,
                    "name": "安全操作技术（图片）"
                },
                {
                    "num": 1,
                    "name": "叉车部件识别（图片）"
                },
                {
                    "num": 2,
                    "name": "叉车零部件（图片）"
                },
                {
                    "num": 3,
                    "name": "法规与标准知识"
                },
                {
                    "num": 4,
                    "name": "基础知识"
                },
                {
                    "num": 5,
                    "name": "交通标志（图片）"
                },
                {
                    "num": 6,
                    "name": "仪表识别（图片）"
                },
                {
                    "num": 7,
                    "name": "安全法知识"
                },
                {
                    "num": 8,
                    "name": "专业知识"
                },
                {
                    "num": 9,
                    "name": "安全知识"
                }
            ]
        };
        var chapterlist = response.results;
        for(var i=0;i<chapterlist.length;i++){
            $("#chapterlist").append('<option value="'+ chapterlist[i].num +'">'+ chapterlist[i].name+'</option>');
        }
        $('#chapterlist option:first').attr('selected','selected');
    }
    function submitInfotest() {
        $("#titleOption").empty();
        var resopnse = {
            "count": 24,
            "next": "http://192.168.0.103:8000/problem/list/?category=1&chapter=1&page=2",
            "previous": null,
            "results": [
                {
                    "course": "叉车司机(N2)",
                    "chapter": "安全操作技术（图片）",
                    "title": "2、根据以下现象选择正确的观点？(单选题)",
                    "choices": [
                        "A、车入车库需手动开门",
                        "B、车辆检修需停稳",
                        "C、检修时，叉齿需降至地面",
                        "D、检修需关闭发动机"
                    ],
                    "answers": "A",
                    "images": "http://192.168.0.103:8000/static/upload/yhpicture/nj_cz_t2_tp97.jpg",
                    "category": "单选题"
                }
            ]
        }
        var imgSrc = resopnse.results[0].images;
        var Option = resopnse.results[0].choices;
        var answer = resopnse.results[0].answers;
        nextTitle = resopnse.next;
        previousTitle = resopnse.previous;
        count = resopnse.count;
        if(nextTitle != null){
            categoryNum = GetRequesttitle(nextTitle);
            var titleNum = GetRequest(nextTitle) - 1;
        }else{
            categoryNum = GetRequesttitle(previousTitle);
            var titleNum = GetRequest(previousTitle) + 1;
        }
        $('#titleImage').attr('src',imgSrc);
        for(var i = 0; i<Option.length; i++){
            $("#titleOption").append('<li class="clearfix"><span>'+ Option[i] +'</span></li>');
        }

        $('#answer').text('正确答案：'+ answer);
        $('#titleNum').text('第 ' + titleNum + ' 题：');

    }


})

/*
 页面点击函数
 */

function selectAll(index) {
    controlBtn(index);
    console.log(chapter);
    var url = '/problem/list/?page=1&&chapter=' + chapter;
    submitInfo(url);
}//全部
function selectSingle(index) {
    controlBtn(index);
    var url = '/problem/list/?page=1&&category=0&&chapter=' + chapter;
    submitInfo(url);
}//单选题
function selectMulti(index) {
    controlBtn(index);
    var url = '/problem/list/?page=1&&category=1&&chapter=' + chapter;
    submitInfo(url);
}//多选题
function selectJuage(index) {
    controlBtn(index);
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
    $("#titleImage").empty();
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

/*
 头部按钮样式控制
 */

function controlBtn(index) {
    $("#welmainbtn button:eq(" + index + ")").addClass('topicTypebtn_active').removeClass("topicTypebtn");
    $("#welmainbtn button:eq(" + index + ")").siblings().addClass('topicTypebtn').removeClass("topicTypebtn_active");
}





