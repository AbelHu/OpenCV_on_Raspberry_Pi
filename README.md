
# Video Streaming with RapsberryPI Using gStreamer

### Rapsberry PI：
```shell
gst-launch-1.0 -v autovideosrc ! videoconvert ! videoscale ! video/x-raw,format=I420,width=800,height=600,framerate=25/1 ! jpegenc ! rtpjpegpay ! udpsink host=10.172.2.127 port=5000
```

### Desktop PC:
```shell
gst-launch-1.0 -v udpsrc port=5000 ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! autovideosink
```