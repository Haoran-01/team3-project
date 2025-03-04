import os

# 指定你的文件夹路径
folder_path = "/home/mscrobotics2425laptop14/Desktop/project/team3/team3-project/src/camera/captured_images/labels2"

# 获取所有 color_*.jpg 文件
files = [f for f in os.listdir(folder_path) if f.startswith("color_") and f.endswith(".txt")]

# 按数字部分排序
files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))

# 重新编号起始值
start_index = 749

# color_0.txt
# 批量重命名
for i, old_name in enumerate(files):
    new_name = f"color_{start_index + i}.txt"
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    print(f"✅ {old_name} → {new_name}")

print("🎯 所有文件重命名完成！")
