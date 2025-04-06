# 文件分类器

一个功能强大的跨平台 Python 实用程序，可根据扩展名、文件夹名称或时间戳自动组织文件和文件夹。

## 功能特点

- **多种分类方法**：
  - **基于扩展名**：根据文件扩展名将文件分类到不同类别
  - **基于时间**：按创建时间、修改时间或访问时间组织文件
  - **文件夹分类**：根据常见命名模式对文件夹进行分类

- **文件类别**：
  - 文档 (PDF, DOC, TXT 等)
  - 图片 (JPG, PNG, GIF 等)
  - 音频 (MP3, WAV, FLAC 等)
  - 视频 (MP4, AVI, MKV 等)
  - 压缩文件 (ZIP, RAR, 7Z 等)
  - 代码 (PY, JAVA, HTML 等)
  - 可执行文件 (EXE, MSI, APP 等)
  - 其他 (未归入上述类别的扩展名)

- **文件夹类别**：
  - Projects：开发和项目相关文件夹
  - Backups：备份和存档内容
  - Documents：文档和报告文件夹
  - Media：照片、视频、音乐文件夹
  - Downloads：下载文件夹
  - Applications：软件和应用程序
  - Data：数据集和数据库
  - Web：网络相关内容
  - Dated：带有日期模式的文件夹（自动检测）
  - Versioned：带有版本模式的文件夹（自动检测）
  - Uncategorized：不匹配任何模式的文件夹

- **操作模式**：
  - 移动（默认）：将文件/文件夹移动到目标目录
  - 复制：创建副本而不是移动
  - 符号链接：创建指向原始文件/文件夹的符号链接
  - 预览模式：显示将要执行的操作而不实际进行更改

- **跨平台兼容性**：
  - 在 Windows、macOS 和 Linux 上运行

## 系统要求

- Python 3.6 或更高版本
- 不需要额外库（仅使用标准库）

## 安装

下载脚本并使其可执行：

```bash
chmod +x file_classifier.py
```

或直接用 Python 运行：

```bash
python file_classifier.py [选项]
```

## 使用方法

### 基本用法

```bash
python file_classifier.py 源目录 [目标目录]
```

如果未指定 `目标目录`，文件将在名为 `./classified` 的新目录中组织。

### 常用选项

```
-l, --symlinks       创建符号链接而不是移动文件
-c, --copy           复制文件而不是移动
-d, --dry-run        显示将要执行的操作而不实际执行
-f, --folders        在分类中包含文件夹
```

### 分类方法

```
-e, --extensions     按文件扩展名分类（默认行为）
-t, --time           按时间属性组织
```

### 基于时间的组织选项

```
--time-attr {modified,created,accessed}
                     使用的时间属性（默认：modified）
--time-format 格式
                     目录的时间格式（默认：'%Y-%m' 表示年-月）
```

## 示例

### 基于扩展名的组织

```bash
# 按扩展名对下载文件夹中的所有文件进行分类
python file_classifier.py ~/Downloads ~/Organized

# 分类文件和文件夹，创建副本而不是移动
python file_classifier.py ~/Documents ~/Organized -f -c

# 创建符号链接而不是移动文件
python file_classifier.py ~/Pictures ~/Organized -l

# 预览将要执行的操作而不进行任何更改
python file_classifier.py ~/Desktop -d
```

### 基于时间的组织

```bash
# 按修改时间（年-月）组织文件
python file_classifier.py ~/Documents ~/TimeOrganized -t

# 按创建日期组织，使用年-月-日格式
python file_classifier.py ~/Photos ~/Chronological -t --time-attr created --time-format "%Y-%m-%d"

# 按访问时间组织文件和文件夹
python file_classifier.py ~/Downloads ~/AccessOrganized -t --time-attr accessed -f
```

## 常见问题

**问：如果目标目录中已存在文件或文件夹会怎样？**
答：脚本将跳过它并记录警告消息。

**问：组织会保留目录结构吗？**
答：不会，所有文件都会被平铺到相应的类别目录中。对于层次结构组织，可以考虑使用具有层次格式的基于时间的组织，如 `%Y/%m/%d`。

**问：我可以自定义文件类别吗？**
答：可以，您可以编辑脚本中的 `FILE_CATEGORIES` 字典来添加或修改类别。

## 许可证

此实用程序根据 MIT 许可证发布。随意使用、修改和分发。
