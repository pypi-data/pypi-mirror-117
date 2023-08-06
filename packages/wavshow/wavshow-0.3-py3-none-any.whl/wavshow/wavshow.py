#!/usr/bin/env python3

import argparse
import numpy
import scipy.signal
import soundfile
import matplotlib.pyplot as plt


def plotspec(wav, fs):
    freq, time, spec = scipy.signal.spectrogram(wav, fs)
    plt.imshow(10 * numpy.log10(spec),
              aspect='auto', interpolation='nearest', origin='lower')

    # Set x axis (Time)
    locs = list(map(int, numpy.linspace(0, len(time)-1, 10)))
    plt.xticks(locs, time[locs])
    plt.xlabel('Time [s]')

    # Set y axis (Frequency)
    locs = range(0, len(freq), 16)
    plt.yticks(locs, map(int, freq[locs]))
    plt.ylabel('Frequency [Hz]')


def plotwav(wav, fs, is_variable_ylim=False):
    plt.plot(wav, 'k-')
  
    # Set x axis (Time)
    samples = numpy.fromiter(map(int, numpy.linspace(0, len(wav), 10)),
                            dtype=numpy.int32)
    seconds = list(map(lambda t: '%.2f' % t, 1.0 * samples / fs))
    plt.xticks(samples, seconds)
    plt.xlim(0, len(wav))

    # Set y axis (Amplitude)
    if is_variable_ylim:
        ylim = abs(wav).max() * 1.1
    else:
        ylim = 1
    plt.ylim(-ylim, ylim)
    plt.ylabel('Amplitude')


def plot_main(wavname, is_variable_ylim):
    print('Plot', wavname)
    plt.figure()

    # Load wave file
    obj = soundfile.SoundFile(wavname)
    wav = obj.read()
    fs = obj.samplerate
    is_multichannel = len(wav.shape) == 2

    if is_multichannel:
        plt.subplot(wav.shape[1], 1, 1)
        plt.title(wavname)
        for ch in range(wav.shape[1]):
            plt.subplot(wav.shape[1], 1, ch+1)
            plotwav(wav[:, ch], fs)

    else:
        plt.subplot(2, 1, 1)
        plt.title(wavname)
        plotwav(wav, fs, is_variable_ylim)

        plt.subplot(2, 1, 2)
        plotspec(wav, fs)


def main():
    parser = argparse.ArgumentParser(usage="""
    Plot audio data and spectrogram.
   
    Examples:
    (1) Plot a wave file "sample.wav"
        $ wavshow sample.wav
    (2) Plot multiple wave files "sample1.wav", "sample2.wav"
        $ wavshow sample1.wav sample2.wav
    (3) Plot a wave file "sample.wav" and save it as "sample01.png"
        $ wavshow sample.wav -o sample%%02d.png
""")
    parser.add_argument(
        "input", nargs='*', help="Input audio file."
    )
    parser.add_argument(
        "-o", "--output_imgfile", default=None, help="The image file name to save."
    )
    parser.add_argument(
        "--is_variable_ylim", action="store_true", default=False, 
        help="Adjusts ylim of waveform using the data"
    )
    args = parser.parse_args()


    for index, wavname in enumerate(args.input):
        plot_main(wavname, args.is_variable_ylim)

        if args.output_imgfile:
            if "%" in args.output_imgfile:
                plt.savefig(args.output_imgfile % index)
            else:
                plt.savefig(args.output_imgfile)

    plt.show()


if __name__ == '__main__':
    main()