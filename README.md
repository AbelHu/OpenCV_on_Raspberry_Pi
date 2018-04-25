
# Video Streaming with RapsberryPI Using gStreamer

## Rapsberry PI -> Desktop PC

### Rapsberry PI：
```shell
raspivid -n -t 0 -rot 180 -w 960 -h 720 -fps 30 -b 6000000 -o - | gst-launch-1.0 -e -vvvv fdsrc ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=10.156.91.78 port=5000
```

### Desktop PC:
```shell
gst-launch-1.0 -e -v udpsrc port=5000 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! fpsdisplaysink sync=false text-overlay=false
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
