# 数据导入导出


# 新建培训项目

- 导出

```
SELECT num, name FROM courses_temp WHERE num > 8 INTO OUTFILE '/Users/turkey/Projects/gtpx_web/source_data/sql/2017-11-15/courses.txt';
```

- 导入

```
load data local infile '/data/webroot/gtpx_web/source_data/sql/2017-11-15/courses.txt' into table courses_temp (num, name);
```


# 章节信息

- 导出

```
select num, course, name, level from chapters_temp where level = 1 and course in (9, 10, 11) into outfile '/Users/turkey/Projects/gtpx_web/source_data/sql/2017-11-15/prv_course_9_10_11.txt';
```

- 导入

```
load data local infile '/data/webroot/gtpx_web/source_data/sql/2017-11-15/prv_course_9_10_11.txt' into table chapters_temp (num, course, name, level);
```

# 题目信息

- 导出

```
select chapter, course, num, title, choices, answers, images, category, level from problems_temp where level = 1 and course in (9, 10, 11)into outfile '/Users/turkey/Projects/gtpx_web/source_data/sql/2017-11-15/prv_problems_9_10_11.txt';
```

- 导入

```
load data local infile '/data/webroot/gtpx_web/source_data/sql/2017-11-15/prv_problems_9_10_11.txt' into table problems_temp (chapter, course, num, title, choices, answers, images, category , level);

``