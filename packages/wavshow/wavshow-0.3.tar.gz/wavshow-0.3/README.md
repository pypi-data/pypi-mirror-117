# What is wavshow?
`wavshow` is a command line interface to visualize wavefiles.
You can open multiple audio (wav, flac, ...) files and visualize its waveform and spectrogram.
`wavshow` also supports saving the visualizations as image files.

![Sample](docs/sample.png "Sample")

# Usage
Once you installed this package, you can use
```
wavshow  --help
```

```
Uusage: 
    Plot audio data and spectrogram.
   
    Examples:
    (1) Plot a wave file "sample.wav"
        $ wavshow sample.wav
    (2) Plot multiple wave files "sample1.wav", "sample2.wav"
        $ wavshow sample1.wav sample2.wav
    (3) Plot a wave file "sample.wav" and save it as "sample01.png"
        $ wavshow sample.wav -o sample%02d.png

positional arguments:
  input                 Input audio file.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_IMGFILE, --output_imgfile OUTPUT_IMGFILE
                        The image file name to save.
  --is_variable_ylim    Adjusts ylim of waveform using the data
```
to show waveform and spectrogram.

# How to install
```
pip install wavshow
```
