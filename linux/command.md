# 个人使用命令大全

### dmesg
**基本语法**
```bash
dmesg [选项]
```

|选项|作用|示例|
|----|----|----|
|无选项|输出全部内核缓冲区日志|`dmesg`|
|`-H/--human`|人类可读格式，带时间戳和颜色高亮|`dmesg -H`|
|`-T/--ctime`|用系统本地时间显示日志时间(而非启动后的秒数)|`dmesg -T` <span style="color: red;">**常用**</span>|
|`-w/--follow`|实时监控新的内核日志(类似 `tail -f`)|`dmesg -w`|
|`-l <级别>`|过滤指定日志级别，支持 `emerg`/`alert`/`crit`/`err`/`warn`/`info`/`debug`|`dmesg -l err`(只看错误日志)|
|`-k/--kernel`|只显示内核相关日志|`dmesg -k`|
|`-u/--userspace`|只显示用户空间相关日志|`dmesg -u`|
|`-c/--clear`|输出日志后清空内核缓冲区|`dmesg -c`|
|`--color=always`|强制输出颜色高亮(便于区分不同级别日志)|`dmesg -T --color=always`|

**排查硬盘识别问题**
```python
dmesg -T | grep -i sda
```

**只查看错误和警告日志**
```python
dmesg -l err, warn
```

### tree
**基本语法**
```bash
tree [选项] [目录路径]
```
**安装**
下面为Ubuntu/Debian安装方法：
```bash
sudo apt install tree
```

常用参数：
|参数|功能|
|----|----|
|-d|仅显示目录，不显示文件|
|-L N|限制显示层级为 N（N 为正整数）|
|-a|显示所有文件（含隐藏文件）|
|-f|显示完整的文件 / 目录路径|
|-p|显示文件 / 目录的权限|
|-o 文件名|将输出写入指定文件|