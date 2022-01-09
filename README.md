# 物體辨識結帳
use Raspberry Pi OS & Python 3.9.2
## 簡介
<div>
    <img src="https://www.tensorflow.org/images/tf_logo_social.png" height="200"/>
    <img src="https://pbs.twimg.com/profile_images/1455857819534647296/kWvczaKh_400x400.jpg" height="200"/>
</div>

在 *raspberry pi* 上使用*tflite Object Detection*對商品進行結帳並輸出於128*64單色OLED螢幕上
## 使用的硬體配置
- raspberry pi 4B
- 樹梅派電源5.1V / 3.0A
- SanDisk Ultra Micro SCXC 128G(A1記憶卡)
- 單色OLED螢幕128*64 (驅動IC:SSD1306)
- Logitech C310 Webcam(720p)

## 安裝設定
* linux terminal輸入：

複製Repository
>git clone https://github.com/tim12367/Raspberry-Checkout.git

進入複製下來的Repository
>cd Raspberry-Checkout

執行安裝bash
>sh setup.sh

執行程式
>python detect.py

## 製作過程
- 拍攝要辨識的商品圖片
- 使用LabelImg對圖片進行影像標註
- 使用 **TensorFlow Lite Model Maker** fine-tuning EfficientDet 模型
