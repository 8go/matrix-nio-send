[![Built with matrix-nio](
https://img.shields.io/badge/built%20with-matrix--nio-brightgreen)](
https://github.com/poljar/matrix-nio)

# matrix-nio-send

- simple but convenient app to send Matrix text messages as well as
  text, image, audio, video or other arbitrary files.
- it uses the `matrix-nio` SDK, hence the name `matrix-nio-send`,
  see https://github.com/poljar/matrix-nio/

# Summary

This program is a simple but convenient app to send Matrix
messages. Text as well as images can be sent.
It is a CLI program to be be used from the command line.
There is no GUI and there are no windows.

Use cases for this program could be
a) a bot or part of a bot,
b) to send alerts,
c) combine it with cron to publish periodic data,
d) send yourself daily/weekly reminders via a cron job
e) a trivial way to fire off some instant messages from the command line
f) to automate sending via programs and scripts
g) a "blogger" who frequently sends messages and images to the same
   room(s) could use it
h) a person could write a diary or run a gratitutde journal by
   sending messages to her/his own room

This program on the first run creates a credentials.json file.
The credentials.json file stores: homeserver, user id,
access token, device id, and room id. On the first run
it asks some questions, creates the token and device id
and stores everything in the credentials.json file.

From the second time the program is run, and on all
future runs it will use the homeserver, user id
and access token found in the credentials file to log
into the Matrix account. Now this program can be used
to easily send simple text messages, images, and so forth
to the preconfigured room.
The messages can be provided
a) in the command line (-m or --message)
b) read from the keyboard
c) piped into the program through a pipe from stdin (|)

It supports 4 text formats:
a) text: default
b) html:  HTML formated text
c) markdown: MarkDown formatted text
d) code: used a block of fixed-sized font, ideal for ASCII art or
   tables, bash outputs, etc.

Typical images that can be sent are: .jpg, .gif, .png or .svg.

Arbirtary files like .txt, .pdf, .doc, audio files like .mp3
or video files like .mp4 can also be sent.

Since the credentials file holds an access token it
should be protected and secured. One can use different
credential files for different users or different rooms.

On creation the credentials file will always be created in the local
directory, so the users sees it right away. This is fine if you have
only one or a few credential files, but for better maintainability
it is suggested to place your credentials files into directory
$HOME/.config/matrix-nio-send.py/. When the program looks for
a credentials file it will first look in local directory and then
as secondary choice it will look in directory
$HOME/.config/matrix-nio-send.py/.

If you want to re-use an existing device id and an existing
access token, you can do so as well, just manually edit the
credentials file. However, for end-to-end encryption this will
not work.

The program can accept verification request and verify other devices
via emojis. Do do so use the --verify option and the program will
await incoming verification request and act accordingly.

In summary, TLDR: first run sets everything up, thereafter it can
be used to easily publish messages from the command line. Thereafter
one can also send images, audio, files or verify devices for end-to-end
encryption. End-to-end encryption is enabled by default and
cannot be turned off.


# Dependencies

- Python 3.8 or higher (3.7 will NOT work) installed
- matrix-nio must be installed, see https://github.com/poljar/matrix-nio
  pip3 install --user --upgrade matrix-nio[e2e]
- python3 package markdown must be installed to support MarkDown format
  pip3 install --user --upgrade markdown
- python3 package python_magic must be installed to support image sending
  pip3 install --user --upgrade python_magic
- this file must be installed, and should have execution permissions
  chmod 755 matrix-nio-send.py


# Examples of calling `matrix-nio-send`

```
$ matrix-nio-send.py #  first run; this will configure everything
$ # this created a credentials.json file
$ # optionally, if you want you can move it to the app config directory
$ mkdir $HOME/.config/matrix-nio-send.py # optional
$ mv credentials.json $HOME/.config/matrix-nio-send.py/
$ # Now you are ready to run program for a second time
$ # Let us verify the device/room to where we want to send messages
$ # The other device will issue a "verify by emoji" request
$ matrix-nio-send.py --verify
$ # Now program both configured and verified, let us send the first message
$ matrix-nio-send.py -m "First message!"
$ matrix-nio-send.py --debug # turn debugging on
$ matrix-nio-send.py --help # print help
$ matrix-nio-send.py # this will ask user for message to send
$ matrix-nio-send.py --message "Hello World!" # sends provided message
$ echo "Hello World" | matrix-nio-send.py # pipe input msg into program
$ matrix-nio-send.py -m msg1 -m msg2 # sends 2 messages
$ matrix-nio-send.py -m msg1 msg2 msg3 # sends 3 messages
$ df -h | matrix-nio-send.py --code # formatting for code/tables
$ matrix-nio-send.py -m "<b>BOLD</b> and <i>ITALIC</i>" --html
$ matrix-nio-send.py -m "- bullet1" --markdown
$ matrix-nio-send.py --credentials usr1room2 # select credentials file
$ matrix-nio-send.py -m "hi" --room '!YourRoomId:example.org'
$ # some shells require the ! of the room id to be escaped with \
$ matrix-nio-send.py -m "hi" --room r"\!YourRoomId:example.org"
$ # send 2 images and 1 text
$ matrix-nio-send.py -i photo1.jpg photo2.img -m "Do you like my 2 photos?"
$ # send 1 image and no text
$ matrix-nio-send.py -i photo1.jpg -m ""
$ # send 1 audio and 1 text to 2 rooms
$ matrix-nio-send.py -a song.mp3 -m "Do you like this song?" \
    -r "!someroom1:example.com" "!someroom2:example.com"
$ # send a .pdf file and a video with a text
$ matrix-nio-send.py -f example.pdf video.mp4 -m "Here are the promised files"
```

# Usage
```
usage: matrix-nio-send.py [-h] [-d] [-t CREDENTIALS] [-r ROOM [ROOM ...]]
                          [-m MESSAGE [MESSAGE ...]] [-i IMAGE [IMAGE ...]]
                          [-a AUDIO [AUDIO ...]] [-f FILE [FILE ...]] [-w]
                          [-z] [-c] [-p SPLIT] [-k CONFIG] [-n] [-e]
                          [-s STORE] [-v VERIFY]

On first run this program will configure itself. On further runs this
program implements a simple Matrix sender. It sends one or multiple text
message to one or multiple Matrix rooms. The text messages can be of format
"text", "html", "markdown" or "code". Images, audio or arbitrary files can
be sent as well. Emoji verification is built-in which can be used to verify
devices. End-to-end encryption is enabled by default and cannot be turned
off. matrix-nio (https://github.com/poljar/matrix-nio) and end-to-end
encryption packages must be installed. See dependencies in source code (or
README.md). For even more explications run this program with the --help
option or read the full documentation in the source code.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Print debug information
  -t CREDENTIALS, --credentials CREDENTIALS
                        On first run, information about homeserver, user,
                        room id, etc. will be written to a credentials file.
                        By default, this file is "credentials.json". On
                        further runs the credentials file is read to permit
                        logging into the correct Matrix account and sending
                        messages to the preconfigured room. If this option
                        is provided, the provided file name will be used as
                        credentials file instead of the default one.
  -r ROOM [ROOM ...], --room ROOM [ROOM ...]
                        Send to this room or these rooms. None, one or
                        multiple rooms can be specified. The default room is
                        provided in credentials file. If a room (or multiple
                        ones) is (or are) provided in the arguments, then it
                        (or they) will be used instead of the one from the
                        credentials file. The user must have access to the
                        specified room in order to send messages there.
                        Messages cannot be sent to arbitrary rooms. When
                        specifying the room id some shells require the
                        exclamation mark to be escaped with a blackslash.
  -m MESSAGE [MESSAGE ...], --message MESSAGE [MESSAGE ...]
                        Send this message. If not specified, and no input
                        piped in from stdin, then message will be read from
                        stdin, i.e. keyboard. This option can be used
                        multiple time to send multiple messages. If there is
                        data is piped into this program, then first data
                        from the pipe is published, then messages from this
                        option are published.
  -i IMAGE [IMAGE ...], --image IMAGE [IMAGE ...]
                        Send this image. This option can be used multiple
                        time to send multiple images. First images are send,
                        then text messages are send.
  -a AUDIO [AUDIO ...], --audio AUDIO [AUDIO ...]
                        Send this audio file. This option can be used
                        multiple time to send multiple audio files. First
                        audios are send, then text messages are send.
  -f FILE [FILE ...], --file FILE [FILE ...]
                        Send this file (e.g. PDF, DOC, MP4). This option can
                        be used multiple time to send multiple files. First
                        files are send, then text messages are send.
  -w, --html            Send message as format "HTML". If not specified,
                        message will be sent as format "TEXT". E.g. that
                        allows some text to be bold, etc. Only a subset of
                        HTML tags are accepted by Matrix.
  -z, --markdown        Send message as format "MARKDOWN". If not specified,
                        message will be sent as format "TEXT". E.g. that
                        allows sending of text formated in MarkDown
                        language.
  -c, --code            Send message as format "CODE". If not specified,
                        message will be sent as format "TEXT". If both
                        --html and --code are specified then --code takes
                        priority. This is useful for sending ASCII-art or
                        tabbed output like tables as a fixed-sized font will
                        be used for display.
  -p SPLIT, --split SPLIT
                        If set, split the message(s) into multiple messages
                        wherever the string specified with --split occurs.
                        E.g. One pipes a stream of RSS articles into the
                        program and the articles are separated by three
                        newlines. Then with --split set to "\n\n\n" each
                        article will be printed in a separate message. By
                        default, i.e. if not set, no messages will be split.
  -k CONFIG, --config CONFIG
                        Location of a config file. By default, no config
                        file is used. If this option is provided, the
                        provided file name will be used to read
                        configuration from.
  -n, --notice          Send message as notice. If not specified, message
                        will be sent as text.
  -e, --encrypted       Send message end-to-end encrypted. Encryption is
                        always turned on and will always be used where
                        possible. It cannot be turned off. This flag does
                        nothing as encryption is turned on with or without
                        this argument.
  -s STORE, --store STORE
                        Path to directory to be used as "store" for
                        encrypted messaging. By default, this directory is
                        "./store/". Since encryption is always enabled, a
                        store is always needed. If this option is provided,
                        the provided directory name will be used as
                        persistent storage directory instead of the default
                        one. Preferably, for multiple executions of this
                        program use the same store for the same device.
  -v VERIFY, --verify VERIFY
                        Perform verification. By default, no verification is
                        performed. Possible values are: "emoji". If
                        verification is desired, run this program in the
                        foreground (not as a service) and without a pipe.
                        Verification questions will be printed on stdout and
                        the user has to respond via the keyboard to accept
                        or reject verification. Once verification is
                        complete, stop the program and run it as a service
                        again. Don't send messages or files when you verify.

```

# For Developers

- Don't change tabbing, spacing, or formating as file is automatically
  linted with autopep8 --aggressive
- pylama:format=pep8:linters=pep8

# Things to do, things missing

- help me add config file handling

# Final Remarks

- Enjoy!
- Pull request are welcome

