# 国通培训项目接口

## 1. 题目接口

接口地址：

`/problem/list/`

    **需要登录**


> 参数说明：

| 参数名| 类型|  可选(默认值)|  说明 |
| ---| ---| ---| ---|
|   chapter| int=0| 必须| 章节，默认为0为第一章|
|   category| int=[0, 1, 2, 3]| 可选|题目类型，0=单选题, 1=判断题 2=多选题 3=图片题, 不传表示全部类型|
|   page| int=1| 必需| 题目序号|


> 返回结果示例：

```json
{
    "count": 25,
    "next": "http://127.0.0.1:8000/problem/list/?category=2&chapter=1&page=2",
    "previous": null,
    "results": [
        {
            "course": "叉车司机(N2)",
            "chapter": "叉车部件识别（图片）",
            "title": "4、某集装箱堆高用10T叉车辅助作业，叉车司机想叉取堆垛在上面的空箱，由于车速过快，制动不及，将上面的集装箱空箱撞倒，造成箱子损坏。事故原因分析：（ ）(多选题)",
            "choices": [
                "A、车速过快",
                "B、带病出车",
                "C、措施不当",
                "D、未注意观察"
            ],
            "answers": "AC",
            "images": null,
            "category": "多选题"
        }
    ]
}

```

> 返回结果说明：

| 字段| 类型| 说明|
| ---| ---| ---|
| count| int| 该查询条件下题目总数|
| next| str| 下一题|
| previous| str| 上一题|
| course| str| 课程名|
| chapter| str| 章节名|


