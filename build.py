"""Сборка .exe (на Windows): python build.py
Готовые .exe появятся рядом с app.py; временная папка удаляется."""
import subprocess, shutil
for name in ["StrowkeEngine", "Snake3D", "DrawDrawing", "CreateBook"]:
    subprocess.run(["pyinstaller", "--noconfirm", "--distpath", ".", "--workpath", "_tmp", f"{name}.spec"], check=True)
shutil.rmtree("_tmp", ignore_errors=True)
print("Готово: .exe лежат рядом с app.py")
