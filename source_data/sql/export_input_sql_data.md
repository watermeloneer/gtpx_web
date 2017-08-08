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

