import os

def batch_rename_photos(folder_path, prefix='photo', start_index=1):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    
    # 计数器，用于生成新的索引
    index = start_index
    
    # 遍历文件夹中的每个文件
    for file in files:
        # 检查文件是否为 JPG 或 JPEG 格式
        if file.lower().endswith(('.jpg', '.jpeg')):
            # 构建新文件名
            new_name = f"{prefix}_{index}.jpg"
            # 构建文件的完整路径
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)
            # 重命名文件
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")
            # 更新索引
            index += 1

# 要重命名的文件夹路径
folder_path = "/path/to/your/folder"

# 调用函数进行批量重命名
batch_rename_photos(folder_path)
