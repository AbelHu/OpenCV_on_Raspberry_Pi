
# Video Streaming with RapsberryPI Using gStreamer

## Desktop PC -> Desktop PC

### Desktop PC(sender):
```shell
gst-launch-1.0 -v autovideosrc ! videoconvert ! videoscale ! video/x-raw,format=I420,width=800,height=600,framerate=25/1 ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5000
```

### Desktop PC(receiver):
```shell
gst-launch-1.0 -v udpsrc port=5000 ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! autovideosink
```

## Rapsberry PI -> Desktop PC (Windows)

### Rapsberry PI：
```shell
raspivid -n -t 0 -rot 180 -w 960 -h 720 -fps 30 -b 6000000 -o - | gst-launch-1.0 -e -vvvv fdsrc ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=10.172.2.59 port=5000
```

### Desktop PC:
```shell
gst-launch-1.0 -e -v udpsrc port=5000 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! fpsdisplaysink sync=false text-overlay=false
```

## Rapsberry PI -> AzS managed Linux VM (Ubuntu 16.04 LTS)

### Rapsberry PI：
```shell
raspivid -n -t 0 -rot 180 -w 960 -h 720 -fps 10 -b 6000000 -o - | gst-launch-1.0 -e -v fdsrc do-timestamp=true ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=10.156.91.65 port=5000
```

### AzS managed Linux VM:
```shell
gst-launch-1.0 -e -v udpsrc port=5000 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! fpsdisplaysink sync=false text-overlay=false
```