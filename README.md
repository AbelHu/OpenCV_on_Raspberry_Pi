
# Video Streaming with RapsberryPI Using gStreamer

## Rapsberry PI -> Desktop PC

### Rapsberry PI：
```shell
raspivid -fps 26 -h 450 -w 600 -vf -n -t 0 -b 200000 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay ! gdppay ! tcpserversink host=10.172.2.127 port=5000
```

### Desktop PC:
```shell
gst-launch-0.10 -v tcpclientsrc host=10.172.2.127 port=5000 ! gdpdepay ! rtph264depay ! ffdec_h264 ! ffmpegcolorspace ! autovideosink sync=false
```

## Desktop PC -> Desktop PC

### Desktop PC:
```shell
gst-launch-1.0 -v autovideosrc ! videoconvert ! videoscale ! video/x-raw,format=I420,width=800,height=600,framerate=25/1 ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5000
```

### Desktop PC:
```shell
gst-launch-1.0 -v udpsrc port=5000 ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! autovideosink
```
