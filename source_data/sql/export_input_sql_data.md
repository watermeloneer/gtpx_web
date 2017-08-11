# 本地导入数据库命令

## 导出省级相关

- 导出**章节**

```

select num, course, name, level from chapters_temp where level = 1 into outfile '/Users/turkey/Projects/gtpx_web/source_data/sql/prv_chapters_left_and_chache.txt';
```

- 导出**题目**

```
select chapter, course, num, title, choices, answers, images, category, level from problems_temp where level = 1 into outfile '/Users/turkey/Projects/gtpx_web/source_data/sql/prv_problems_left_and_chache.txt';

```


## 删除

```
# 删除章节
delete from chapters_temp where level = 1;

# 删除题目
delete from problems_temp where level = 1;
```

## 导入

```
# 章节

load data local infile '/data/webroot/gtpx_web/source_data/sql/prv_chapters_left_and_chache.txt' into table chapters_temp (num, course, name, level);

# 题目

load data local infile '/data/webroot/gtpx_web/source_data/sql/prv_problems_left_and_chache.txt' into table problems_temp (chapter, course, num, title, choices, answers, images, category , level);

```