
import sys
import re
import requests
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QFileDialog, QMessageBox, QTextEdit, QComboBox)
from PyQt5.QtCore import QThread, pyqtSignal
from DrissionPage import ChromiumPage


class DownloadThread(QThread):
    log_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(bool, str)

    def __init__(self, share_text, save_path):
        super().__init__()
        self.share_text = share_text
        self.save_path = save_path

    def log(self, msg):
        self.log_signal.emit(msg)

    def run(self):
        try:
            # 1. 提取链接
            self.log("正在提取链接...")
            urls = re.findall(r'https?://[^\s`\'"]+', self.share_text)
            if not urls:
                self.finished_signal.emit(False, "未找到有效链接！")
                return
            
            url = urls[0]
            self.log(f"提取到链接: {url}")

            # 2. 启动浏览器并监听
            self.log("正在启动浏览器...")
            
            # DrissionPage 会自动检测系统浏览器，直接启动即可
            Google = ChromiumPage()
            Google.listen.start("aweme/detail")
            
            self.log("正在访问页面...")
            Google.get(url)
            
            self.log("等待视频数据...")
            sjb = Google.listen.wait(timeout=30)
            
            # 3. 解析数据
            self.log("正在解析数据...")
            JS = sjb.response.body
            data = JS["aweme_detail"]
            
            caption = data["caption"]
            # 清理文件名中的非法字符
            caption_re = re.sub(r'[<>:/\\|?*"]', "", caption)
            if not caption_re:
                caption_re = f"douyin_video_{id(data)}"
            
            video_url = data["video"]["play_addr_h264"]["url_list"][1]
            self.log(f"视频地址获取成功")
            
            # 4. 下载视频
            self.log("正在下载视频...")
            res = requests.get(video_url, stream=True, timeout=120)
            
            total_size = int(res.headers.get('content-length', 0))
            downloaded = 0
            
            filepath = f"{self.save_path}/{caption_re}.mp4"
            
            with open(filepath, 'wb') as f:
                for chunk in res.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            progress = downloaded / total_size * 100
                            self.log(f"下载进度: {progress:.1f}%")
            
            # 关闭浏览器
            try:
                Google.quit()
            except:
                pass
            
            self.finished_signal.emit(True, f"视频下载成功！\n保存位置: {filepath}")
            
        except Exception as e:
            self.finished_signal.emit(False, f"出错了: {str(e)}")


class DouyinDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("抖音视频下载器")
        self.resize(650, 400)
        # 窗口居中
        self.center_window()
        
        # 主窗口
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # 1. 分享链接输入
        link_layout = QHBoxLayout()
        link_label = QLabel("分享链接:")
        self.link_edit = QLineEdit()
        self.link_edit.setPlaceholderText("请粘贴抖音分享链接...")
        self.link_edit.setFixedHeight(45)  # 设置高度
        link_layout.addWidget(link_label)
        link_layout.addWidget(self.link_edit)
        main_layout.addLayout(link_layout)
        
        # 2. 保存路径选择
        path_layout = QHBoxLayout()
        path_label = QLabel("保存路径:")
        self.path_edit = QLineEdit()
        self.path_edit.setPlaceholderText("请选择保存位置...")
        self.path_edit.setFixedHeight(45)  # 设置高度
        browse_btn = QPushButton("浏览")
        browse_btn.setFixedHeight(45)  # 设置高度
        browse_btn.clicked.connect(self.select_path)
        path_layout.addWidget(path_label)
        path_layout.addWidget(self.path_edit)
        path_layout.addWidget(browse_btn)
        main_layout.addLayout(path_layout)
        
        # 3. 浏览器选择
        browser_layout = QHBoxLayout()
        browser_label = QLabel("浏览器选择:")
        self.browser_combo = QComboBox()
        self.browser_combo.addItems(["Chrome", "Edge", "Chromium"])
        self.browser_combo.setFixedHeight(40)
        browser_layout.addWidget(browser_label)
        browser_layout.addWidget(self.browser_combo)
        main_layout.addLayout(browser_layout)
        
        # 4. 下载按钮
        self.download_btn = QPushButton("开始下载")
        self.download_btn.setFixedHeight(45)  # 设置高度
        self.download_btn.clicked.connect(self.start_download)
        main_layout.addWidget(self.download_btn)
        
        # 5. 日志输出
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.append("项目已开源")  # 预填写内容
        main_layout.addWidget(self.log_text)

    def select_path(self):
        dialog = QFileDialog(self, "选择保存位置")
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, True) 
        dialog.setOption(QFileDialog.DontUseNativeDialog, True) # 不使用系统原生对话框
        dialog.setMinimumSize(800, 600)  # 设置最小尺寸
        
        if dialog.exec_() == QFileDialog.Accepted:
            path = dialog.selectedFiles()[0]
            self.path_edit.setText(path)

    def center_window(self):
        # 获取屏幕尺寸
        screen = QApplication.primaryScreen().geometry()
        # 获取窗口尺寸
        size = self.geometry()
        # 计算居中位置
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        self.move(x, y)

    def log(self, msg):
        self.log_text.append(msg)

    def start_download(self):
        share_text = self.link_edit.text().strip()
        save_path = self.path_edit.text().strip()
        
        if not share_text:
            QMessageBox.warning(self, "警告", "请输入分享内容！")
            return
        
        if not save_path:
            QMessageBox.warning(self, "警告", "请选择保存位置！")
            return
        
        self.log_text.clear()
        self.download_btn.setEnabled(False)
        
        self.download_thread = DownloadThread(share_text, save_path)
        self.download_thread.log_signal.connect(self.log)
        self.download_thread.finished_signal.connect(self.on_download_finished)
        self.download_thread.start()

    def on_download_finished(self, success, msg):
        self.download_btn.setEnabled(True)
        if success:
            QMessageBox.information(self, "成功", msg)
        else:
            QMessageBox.critical(self, "错误", msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DouyinDownloader()
    window.show()
    sys.exit(app.exec_())
