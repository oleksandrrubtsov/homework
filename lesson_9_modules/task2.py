import sys


print("Original sys.path:")
print(sys.path)


new_path = "/lesson_9_modules/task1.py"
sys.path.append(new_path)


print("\nlesson_9_module/task1.py sys.path:")
print(sys.path)

 
