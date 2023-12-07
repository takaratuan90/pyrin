import subprocess
import multiprocessing  # Import module multiprocessing

def command1():
    # Lệnh hoặc công việc bạn muốn chạy ở lệnh đầu tiên
    subprocess.run(['python', '/content/pyrin/pyipad --utxoindex'])

def command2():
    # Lệnh hoặc công việc bạn muốn chạy ở lệnh thứ hai
    
    subprocess.run(['python', '/content/pyrin/pyrinminer --miningaddr pyrin:qzsc50v3h0kg9fyhxeycafsumvtz237dhhucye9ucc8jjd0f3nvnzez6hj5vu'])

if __name__ == '__main__':
    # Tạo hai tiến trình riêng biệt cho mỗi lệnh
    process1 = multiprocessing.Process(target=command1)
    process2 = multiprocessing.Process(target=command2)


    # Bắt đầu chạy các tiến trình
    process1.start()
    process2.start()

    # Chờ cho đến khi các tiến trình hoàn thành
    process1.join()
    process2.join()
