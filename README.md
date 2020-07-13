# matrix-nio-send

- simple but convenient app to send Matrix messages
- it uses the matrix-nio SDK, hence the name matrix-nio-send,
  see https://github.com/poljar/matrix-nio/

## Summary 

This program is a simple but convenient app to send Matrix
messages. It is a CLI program to be be used from the command line.
There is no GUI and windows. 

Use cases for this program could be
a) a bot or part of a bot,
b) to send alerts,
c) combine it with cron to publish periodic data,
d) send yourself daily/weekly reminders via a cron job
e) a trivial way to fire off some instant messages from the command line
f) to automate sending via programs and scripts


This program on the first run creates a credentials.json file.
The credentials.json file stores: homeserver, user id,
access token, device id, and room id. On the first run
it asks some questions, creates the token and device id
and stores everything in the credentials.json file.

From the second time the program is run, and on all
future runs it will use the homeserver, user id
and access token found in the credentials file to log
into the Matrix account. Now this program can be used
to easily send simple text messages to the preconfigured room.
The messages can be provided
a) in the command line (-m or --message)
b) read from the keyboard
c) piped into the program through a pipe from stdin (|)

It supports 4 text formats:
a) text: default
b) html:  HTML formated text
c) markdown: MarkDown formatted text
d) code: used a block of fixed-sized font, idel for ASCII art or
   tables, bash outputs, etc.

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
credentials file. 

In summary, TLDR: first run sets everything up, thereafter it can
be used to easily publish messages.

## Dependencies

- Python 3.8 or higher (3.7 will NOT work) installed
- matrix-nio must be installed, see https://github.com/poljar/matrix-nio
  pip3 install --user --upgrade matrix-nio
- python3 package markdown must be installed to support MarkDown format
  pip3 install --user --upgrade markdown
- this file must be installed, and should have execution permissions
  chmod 755 matrix-nio-send.py


## Examples of calling matrix-nio-send

```
$ matrix-nio-send.py #  first run; this will configure everything
$ # this created a credentials.json file
$ # optionally, if you want you can move it to the app config directory
$ mkdir $HOME/.config/matrix-nio-send.py # optional
$ mv credentials.json $HOME/.config/matrix-nio-send.py/
$ # now you are ready to run program for a second time and send a msg
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
$ matrix-nio-send.py --debug # turn debugging on
$ matrix-nio-send.py --help # print help

usage: matrix-nio-send.py [-h] [-d] [-t CREDENTIALS] [-r ROOM]
                              [-m MESSAGE [MESSAGE ...]] [-w] [-n] [-c]

On first run this program will configure itself. On further runs this
program implements a simple Matrix sender. It sends one or multiple text
message to a Matrix room. The messages can be of format "text", "html",
"markdown" or "code".matrix-nio must be installed.

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
  -r ROOM, --room ROOM  Send to this room. Usually the room is provided in
                        credentials file. If provided it will use this room
                        instead the one from the credentials file. The user
                        must have access to the specified room in order to
                        send messages there. Messages cannot be sent to
                        arbitrary rooms.
  -m MESSAGE [MESSAGE ...], --message MESSAGE [MESSAGE ...]
                        Send this message. If not specified, and no input
                        piped in from stdin, then message will be read from
                        stdin, i.e. keyboard.This option can be used
                        multiple time to send multiple messages. If there is
                        data is piped into this program, then first data
                        from the pipe is published, then messages from this
                        option are published.
  -w, --html            Send message as format "HTML". If not specified,
                        message will be sent as format "TEXT". E.g. that
                        allows some text to be bold, etc. Only a subset of
                        HTML tags are accepted by Matrix.
  -n, --markdown        Send message as format "MARKDOWN". If not specified,
                        message will be sent as format "TEXT". E.g. that
                        allows sending of text formated in MarkDown
                        language.
  -c, --code            Send message as format "CODE". If not specified,
                        message will be sent as format "TEXT". If both
                        --html and --code are specified then --code takes
                        priority. This is useful for sending ASCII-art or
                        tabbed output like tables as a fixed-sized font will
                        be used for display.
```

## For Developers

- Don't change tabbing, spacing, or formating as file is automatically
  linted with autopep8 --aggressive
- Long lines are ignored by linter
- pylama:format=pep8:linters=pep8:ignore=E501
- Originally forked from:
  https://github.com/poljar/matrix-nio/blob/master/examples/restore_login.py
- Further documentation related to this:
  https://matrix-nio.readthedocs.io/en/latest/examples.html


## Things to do, things missing

- associating public name with session id
- adding end-to-end encryption, ee2e

## Final Remarks

- Enjoy!
- Pull request are welcome

