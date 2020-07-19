#!/usr/bin/env python3

r"""matrix-nio-send.py.

0123456789012345678901234567890123456789012345678901234567890123456789012345678
0000000000111111111122222222223333333333444444444455555555556666666666777777777

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

Typical images to send are: JPG, JPEG, IMG, PNG, or SVG.

Arbitrary files can be sent (e.g. .pdf, .doc, .txt, .mp3, .mp4) too.

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
be used to easily publish messages from the command line.


# Dependencies

- Python 3.8 or higher (3.7 will NOT work) installed
- matrix-nio must be installed, see https://github.com/poljar/matrix-nio
  pip3 install --user --upgrade matrix-nio
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
$ # now you are ready to run program for a second time and send a msg
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

usage: matrix-nio-send.py [-h] [-d] [-t CREDENTIALS] [-r ROOM]
                          [-m MESSAGE [MESSAGE ...]] [-i IMAGE [IMAGE ...]]
                          [-a AUDIO [AUDIO ...]] [-f FILE [FILE ...]] [-w]
                          [-z] [-c] [-p SPLIT] [-k CONFIG] [-n] [-e]
                          [-s STORE]

On first run this program will configure itself. On further runs this program
implements a simple Matrix sender. It sends one or multiple text message to a
Matrix room. The messages can be of format "text", "html", "markdown" or
"code".matrix-nio must be installed.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Print debug information
  -t CREDENTIALS, --credentials CREDENTIALS
                        On first run, information about homeserver, user,
                        room id, etc. will be written to a credentials file.
                        By default, this file is "credentials.json". On
                        further runs the credentials file is read to permit
                        logging into the correct Matrix account and sending
                        messages to the preconfigured room. If this option is
                        provided, the provided file name will be used as
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
                        exclamation mark to be escaped with a
                        blackslash.
  -m MESSAGE [MESSAGE ...], --message MESSAGE [MESSAGE ...]
                        Send this message. If not specified, and no input
                        piped in from stdin, then message will be read from
                        stdin, i.e. keyboard.This option can be used multiple
                        time to send multiple messages. If there is data is
                        piped into this program, then first data from the
                        pipe is published, then messages from this option are
                        published.
  -i IMAGE [IMAGE ...], --image IMAGE [IMAGE ...]
                        Send this image.This option can be used multiple time
                        to send multiple images. First images are send, then
                        text messages are send.
  -a AUDIO [AUDIO ...], --audio AUDIO [AUDIO ...]
                        Send this audio file.This option can be used multiple
                        time to send multiple audio files. First audios are
                        send, then text messages are send.
  -f FILE [FILE ...], --file FILE [FILE ...]
                        Send this file (e.g. PDF, DOC).This option can be
                        used multiple time to send multiple files. First
                        files are send, then text messages are send.
  -w, --html            Send message as format "HTML". If not specified,
                        message will be sent as format "TEXT". E.g. that
                        allows some text to be bold, etc. Only a subset of
                        HTML tags are accepted by Matrix.
  -z, --markdown        Send message as format "MARKDOWN". If not specified,
                        message will be sent as format "TEXT". E.g. that
                        allows sending of text formated in MarkDown language.
  -c, --code            Send message as format "CODE". If not specified,
                        message will be sent as format "TEXT". If both --html
                        and --code are specified then --code takes priority.
                        This is useful for sending ASCII-art or tabbed output
                        like tables as a fixed-sized font will be used for
                        display.
  -p SPLIT, --split SPLIT
                        If set, split the message(s) into multiple messages
                        wherever the string specified with --split
                        occurs.E.g. One pipes a stream of RSS articles into
                        the program and the articles are separated by three
                        newlines. Then with --split set to "\n\n\n" each
                        article will be printed in a separate message.By
                        default, i.e. if not set, no messages will be split.
  -k CONFIG, --config CONFIG
                        Location of a config file. By default, no config file
                        is used. If this option is provided, the provided
                        file name will be used to read configuration from.
  -n, --notice          Send message as notice. If not specified, message
                        will be sent as text.
  -e, --encrypted       Send message end-to-endencrypted. If not specified,
                        message will be sent unencrypted.
  -s STORE, --store STORE
                        Path to directory to be used as "store" for encrypted
                        messaging.Must be specified if -e is used. By
                        default, this directory is "store". It is not needed
                        for unencrypted messaging.If this option is provided,
                        the provided directory name will be used as store
                        directory instead of the default one.
```

# For Developers

- Don't change tabbing, spacing, or formating as file is automatically
  linted with autopep8 --aggressive
- Long lines are ignored by linter
- pylama:format=pep8:linters=pep8:ignore=E501

# Things to do, things missing

- adding end-to-end encryption, ee2e
- should multiple -r be allowed to send to several rooms?

# Final Remarks

- Enjoy!
- Pull request are welcome

"""


from nio import AsyncClient, LoginResponse, UploadResponse
from markdown import markdown
from PIL import Image
import textwrap
import traceback
import logging
import argparse
import getpass
import select
import sys
import os
import re  # regular expression
import json
import asyncio
import aiofiles
import aiofiles.os
import magic

# matrix-nio-send
PROG_WITHOUT_EXT = os.path.splitext(os.path.basename(__file__))[0]
# matrix-nio-send.py
PROG_WITH_EXT = os.path.basename(__file__)
CREDENTIALS_FILE_DEFAULT = "credentials.json"
# e.g. ~/.config/matrix-nio-send/
CREDENTIALS_DIR_LASTRESORT = ("~/.config/" +
                              os.path.splitext(os.path.basename(__file__))[0])
# directory to be used by end-to-end encrypted protocol for persistent storage
STORE_DIR_DEFAULT = "store"
# e.g. ~/.local/share/matrix-nio-send/
STORE_PATH_LASTRESORT = ("~/.local/share/" +
                         os.path.splitext(os.path.basename(__file__))[0])
# the store path and store dir will be concatenated to result in:
# e.g. ~/.local/share/matrix-nio-send/store/ as actual persistent store dir


def write_credentials_to_disk(homeserver, user_id, device_id, access_token,
                              room_id, credentials_file) -> None:
    """Write the required login details to disk.

    This file can later be used for logging in
    without using a password.

    Arguments:
    ---------
        homeserver : str
            URL of homeserver, e.g. "https://matrix.example.org"
        user_id : str
            full user id, e.g. "@user:example.org"
        device_id : str
            device id, 10 uppercase letters
        access_token : str
            access token, long cryptographic access token
        room_id : str
            name of room where message will be sent to,
            e.g. "!SomeRoomIdString:example.org"
            user must be member of the provided room
        credentials_file : str
            name/path of file where to store
            credentials information

    """
    # open the credentials file in write-mode
    with open(credentials_file, "w") as f:
        # write the login details to disk
        json.dump(
            {
                # e.g. "https://matrix.example.org"
                "homeserver": homeserver,
                # device ID, 10 uppercase letters
                "device_id": device_id,
                # e.g. "@user:example.org"
                "user_id": user_id,
                # e.g. "!SomeRoomIdString:example.org"
                "room_id": room_id,
                # long cryptographic access token
                "access_token": access_token
            },
            f
        )


def read_credentials_from_disk(credentials_file) -> None:
    """Read the required login details from disk.

    It can then be used to log in without using a password.

    Arguments:
    ---------
    credentials_file : str
        name/path of file to read credentials information from

    """
    # open the file in read-only mode
    with open(credentials_file, "r") as f:
        return(json.load(f))


def determine_credentials_file() -> str:
    """Determine the true filename of credentials file.

    Returns filename with full path or None.

    This function checks if a credentials file exists. If no, it will ask
    user questions regrading login, store the info in a newly created
    credentials file and exit.

    If a credentials file exists, it will read it, log into Matrix,
    send a message and exit.

    The credential file will be looked for the following way:
    a) if a path (e.g. "../cred.json") is specified with -t it will be looked
       for there. End of search.
    b) if only a filename without path (e.g. "cred.json") is specified
       first look in the current local directory, if found use it
    c) if only a filename without path (e.g. "cred.json") is specified
       and it cannot be found in the current local directory, then
       look for it in directory $HOME/.config/matrix-nio-send/
    TLDR: on first run it will be written to current local directory
       or to path specified with --credentials command line argument.
       On further reads, program will look in currently local directory
       or in path specified with --credentials command line argument.
       If not found there (and only filename without path given),
       as a secondary choice program will look for it in
       directory $HOME/.config/matrix-nio-send.py/

    """
    credentials_file = pargs.credentials  # default location
    if (not os.path.isfile(pargs.credentials)) and (
            pargs.credentials == os.path.basename(pargs.credentials)):
        logger.debug("Credentials file does not exist locally. "
                     "File name has no path.")
        credentials_file = CREDENTIALS_DIR_LASTRESORT + "/" + pargs.credentials
        logger.debug("Trying path {credentials_file} as last resort. "
                     "Suggesting to look for there.")
        if os.path.isfile(credentials_file):
            logger.debug("We found the file. It exists in the last resort "
                         f"directory {credentials_file} "
                         "Suggesting to use this one.")
        else:
            logger.debug("File does not exists either in the last resort "
                         "directory or the local directory. "
                         "File not found anywhere. One will have to be "
                         "created. So we suggest the local directory.")
            credentials_file = pargs.credentials
    else:
        if os.path.isfile(pargs.credentials):
            logger.debug("Credentials file existed. "
                         "So this is the one we suggest to use. "
                         "file: {credentials_file}")
        else:
            logger.debug("Credentials file was specified with full path. "
                         "So we suggest that one. "
                         "file: {credentials_file}")
    # The returned file (with or without path)  might or might not exist.
    # But if it does not exist, it is either a full path, or local.
    # We do not want to return the last resort path if it does not exist,
    # so that when it is created it is created where specifically specified
    # or in local dir (but not in last resort dir ~/.config/...)
    return credentials_file


def determine_store_file() -> str:
    """Determine the true full directory name of store directory.

    Returns filename with full path (a dir) or None.

    If -e encrypted is NOT turned on return None.

    The store path will be looked for the following way:
    a) if a path (e.g. "../store") is specified with -s it will be looked
       for there. End of search.
    b) if only a dirname without path (e.g. "store") is specified
       first look in the current local directory, if found use it
    c) if only a dirname without path (e.g. "store") is specified
       and it cannot be found in the current local directory, then
       look for it in directory $HOME/.local/share/matrix-nio-send/
    TLDR: The program will look in currently local directory
       or in path specified with --store command line argument.
       If not found there (and only dirname without path given),
       as a secondary choice program will look for it in
       directory $HOME/.local/share/matrix-nio-send/

    """
    if not pargs.store:
        return None
    if not pargs.encrypted:
        return None
    if pargs.store != os.path.basename(pargs.store):
        logger.debug("A store was specified in command-line. "
                     f"It will be used. store: {pargs.store}")
        if not os.path.isdir(pargs.store):
            logger.info("Could not find existing store directory anywhere. "
                        "A new one will be created. "
                        "It will need to be verified.")
        return pargs.store
    logger.debug("No path was specified, just a directory name.")
    if os.path.isdir(pargs.store):
        logger.debug("Found an existing store in local dir. "
                     "It will be used.")
        return pargs.store
    if os.path.isdir(STORE_PATH_LASTRESORT + "/" + pargs.store):
        logger.debug("Found an existing store dir in "
                     f"{STORE_PATH_LASTRESORT} dir. "
                     "It will be used.")
        return STORE_PATH_LASTRESORT + "/" + pargs.store
    logger.info("Could not find existing store directory anywhere. "
                "A new one will be created. "
                "It will need to be verified.")
    logger.info("The store directory will be created in the local "
                f"directory. Consider moving it to {STORE_PATH_LASTRESORT} "
                "for a more consistent experience.")
    return pargs.store  # prefer to create in the local directory


def determine_rooms(room_id) -> list:
    """Determine the room to send to.

    Arguments:
    ---------
    room_id : room from credentials file

    Look at room from credentials file and at rooms from command line
    and prepares a definite list of rooms.

    Return list of rooms to send to. Returned list is never empty.

    """
    if not pargs.room:
        logger.debug("Room id was provided via credentials file. "
                     "No rooms given in commans line.  "
                     f"Setting rooms to \"{room_id}\".")
        return [room_id]  # list of 1
    else:
        rooms = []
        for room in pargs.room:
            room_id = room.replace(r'\!', '!')  # remove possible escape
            rooms.append(room_id)
        logger.debug("Room(s) were provided via command line. "
                     "Overwriting room id from credentials file "
                     f"with rooms \"{rooms}\" "
                     "from command line.")
        return rooms


async def create_credentials_file(credentials_file) -> None:
    """Log in, create credentials file, log out and exit."""
    text = f'''
            Credentials file \"{pargs.credentials}\" was not found.
            First time use? Setting up new credentials?
            Asking for homeserver, user, password and
            room id to create a credentials file.'''
    print(textwrap.fill(textwrap.dedent(text).strip(), width=79))
    homeserver = "https://matrix.example.org"
    homeserver = input(f"Enter URL of your homeserver: [{homeserver}] ")
    if not (homeserver.startswith("https://")
            or homeserver.startswith("http://")):
        homeserver = "https://" + homeserver
    user_id = "@user:example.org"
    user_id = input(f"Enter your full user ID: [{user_id}] ")
    device_name = PROG_WITHOUT_EXT
    device_name = input(f"Choose a name for this device: [{device_name}] ")
    if device_name == "":
        device_name = PROG_WITHOUT_EXT  # default
    room_id = "!SomeRoomIdString:example.org"
    room_id = input(f"Enter your room ID: [{room_id}] ")
    client = AsyncClient(homeserver, user_id)
    pw = getpass.getpass()
    resp = await client.login(pw, device_name=device_name)
    # check that we logged in succesfully
    if (isinstance(resp, LoginResponse)):
        # when writing, always write to primary location (e.g. .)
        write_credentials_to_disk(homeserver, resp.user_id, resp.device_id,
                                  resp.access_token, room_id,
                                  pargs.credentials)
        text = f'''
                Log in using a password was successful.
                Credentials were stored in file \"{pargs.credentials}\".
                Run program \"{PROG_WITH_EXT}\" again to
                login with credentials and to send a message.
                If you plan on having many credential files, consider
                moving them to directory \"{CREDENTIALS_DIR_LASTRESORT}\".'''
        print(textwrap.fill(textwrap.dedent(text).strip(), width=79))
    else:
        logger.info(f"The program {PROG_WITH_EXT} failed. "
                    "Most likely wrong credentials were entered."
                    "Sorry.")
        logger.info(f"homeserver=\"{homeserver}\"; user=\"{user_id}\"; "
                    f"room_id=\"{room_id}\""
                    f"Failed to log in: {resp}")
    await client.close()
    sys.exit(1)


async def send_file(client, rooms, file):
    """Process file.

    Upload file to server and then send link to rooms.
    Works and tested for .pdf, .txt, .ogg, .wav.
    All these file types are treated the same.

    Arguments:
    ---------
    client : Client
    rooms : list
        list of room_id-s
    file : str
        file name of file from --file argument

    This is a working example for a PDF file.
    It can be viewed or downloaded from:
    https://matrix.example.com/_matrix/media/r0/download/
        example.com/SomeStrangeUriKey # noqa
    {
        "type": "m.room.message",
        "sender": "@someuser:example.com",
        "content": {
            "body": "example.pdf",
            "info": {
                "size": 6301234,
                "mimetype": "application/pdf"
                },
            "msgtype": "m.file",
            "url": "mxc://example.com/SomeStrangeUriKey"
        },
        "origin_server_ts": 1595100000000,
        "unsigned": {
            "age": 1000,
            "transaction_id": "SomeTxId01234567"
        },
        "event_id": "$SomeEventId01234567789Abcdef012345678",
        "room_id": "!SomeRoomId:example.com"
    }

    """
    if not rooms:
        logger.info("No rooms are given. This should not happen. "
                    "This file is being droppend and NOT sent.")
        return
    if not os.path.isfile(file):
        logger.debug(f"File {file} is not a file. Doesn't exist or "
                     "is a directory."
                     "This file is being droppend and NOT sent.")
        return

    # # restrict to "txt", "pdf", "mp3", "ogg", "wav", ...
    # if not re.match("^.pdf$|^.txt$|^.doc$|^.xls$|^.mobi$|^.mp3$",
    #                os.path.splitext(file)[1].lower()):
    #    logger.debug(f"File {file} is not a permitted file type. Should be "
    #                 ".pdf, .txt, .doc, .xls, .mobi or .mp3 ... "
    #                 f"[{os.path.splitext(file)[1].lower()}]"
    #                 "This file is being droppend and NOT sent.")
    #    return

    # 'application/pdf' "plain/text" "audio/ogg"
    mime_type = magic.from_file(file, mime=True)
    # if ((not mime_type.startswith("application/")) and
    #        (not mime_type.startswith("plain/")) and
    #        (not mime_type.startswith("audio/"))):
    #    logger.debug(f"File {file} does not have an accepted mime type. "
    #                 "Should be something like application/pdf. "
    #                 f"Found mime type {mime_type}. "
    #                 "This file is being droppend and NOT sent.")
    #    return

    # first do an upload of file
    # see https://matrix-nio.readthedocs.io/en/latest/nio.html#nio.AsyncClient.upload # noqa
    # then send URI of upload to room

    file_stat = await aiofiles.os.stat(file)
    async with aiofiles.open(file, "r+b") as f:
        resp, maybe_keys = await client.upload(
            f,
            content_type=mime_type,  # application/pdf
            filename=os.path.basename(file),
            filesize=file_stat.st_size)
    if (isinstance(resp, UploadResponse)):
        logger.debug("File was uploaded successfully to server. "
                     f"Response is: {resp}")
    else:
        logger.info(f"The program {PROG_WITH_EXT} failed to upload. "
                    "Please retry. This could be temporary issue on "
                    "your server. "
                    "Sorry.")
        logger.info(f"file=\"{file}\"; mime_type=\"{mime_type}\"; "
                    f"filessize=\"{file_stat.st_size}\""
                    f"Failed to upload: {resp}")

    content = {
        "body": os.path.basename(file),  # descriptive title
        "info": {
            "size": file_stat.st_size,
            "mimetype": mime_type,
        },
        "msgtype": "m.file",
        "url": resp.content_uri,
    }

    try:
        for room_id in rooms:
            await client.room_send(
                room_id,
                message_type="m.room.message",
                content=content
            )
            logger.debug(f"This file was sent: \"{file}\" "
                         f"to room \"{room_id}\".")
    except Exception:
        logger.debug(f"File send of file {file} failed. "
                     "Sorry. Here is the traceback.")
        logger.debug(traceback.format_exc())


async def send_image(client, rooms, image):
    """Process image.

    Arguments:
    ---------
    client : Client
    rooms : list
        list of room_id-s
    image : str
        file name of image from --image argument

    This is a working example for a JPG image.
    It can be viewed or downloaded from:
    https://matrix.example.com/_matrix/media/r0/download/
        example.com/SomeStrangeUriKey # noqa
    {
        "type": "m.room.message",
        "sender": "@someuser:example.com",
        "content": {
            "body": "someimage.jpg",
            "info": {
                "size": 5420,
                "mimetype": "image/jpeg",
                "thumbnail_info": {
                    "w": 100,
                    "h": 100,
                    "mimetype": "image/jpeg",
                    "size": 2106
                },
                "w": 100,
                "h": 100,
                "thumbnail_url": "mxc://example.com/SomeStrangeThumbnailUriKey"
            },
            "msgtype": "m.image",
            "url": "mxc://example.com/SomeStrangeUriKey"
        },
        "origin_server_ts": 12345678901234576,
        "unsigned": {
            "age": 268
        },
        "event_id": "$skdhGJKhgyr548654YTr765Yiy58TYR",
        "room_id": "!JKHgyHGfytHGFjhgfY:example.com"
    }

    """
    if not rooms:
        logger.info("No rooms are given. This should not happen. "
                    "This image is being droppend and NOT sent.")
        return
    if not os.path.isfile(image):
        logger.debug(f"Image file {image} is not a file. Doesn't exist or "
                     "is a directory."
                     "This image is being droppend and NOT sent.")
        return

    # "bmp", "gif", "jpg", "jpeg", "png", "pbm", "pgm", "ppm", "xbm", "xpm",
    # "tiff", "webp", "svg",

    if not re.match("^.jpg$|^.jpeg$|^.gif$|^.png$|^.svg$",
                    os.path.splitext(image)[1].lower()):
        logger.debug(f"Image file {image} is not an image file. Should be "
                     ".jpg, .jpeg, .gif, or .png. "
                     f"[{os.path.splitext(image)[1].lower()}]"
                     "This image is being droppend and NOT sent.")
        return

    # 'application/pdf' "image/jpeg"
    mime_type = magic.from_file(image, mime=True)
    if not mime_type.startswith("image/"):
        logger.debug(f"Image file {image} does not have an image mime type. "
                     "Should be something like image/jpeg. "
                     f"Found mime type {mime_type}. "
                     "This image is being droppend and NOT sent.")
        return

    im = Image.open(image)
    (width, height) = im.size  # im.size returns (width,height) tuple

    # first do an upload of image
    # see https://matrix-nio.readthedocs.io/en/latest/nio.html#nio.AsyncClient.upload # noqa
    # then send URI of upload to room

    file_stat = await aiofiles.os.stat(image)
    async with aiofiles.open(image, "r+b") as f:
        resp, maybe_keys = await client.upload(
            f,
            content_type=mime_type,  # image/jpeg
            filename=os.path.basename(image),
            filesize=file_stat.st_size)
    if (isinstance(resp, UploadResponse)):
        logger.debug("Image was uploaded successfully to server. "
                     f"Response is: {resp}")
    else:
        logger.info(f"The program {PROG_WITH_EXT} failed to upload. "
                    "Please retry. This could be temporary issue on "
                    "your server. "
                    "Sorry.")
        logger.info(f"file=\"{image}\"; mime_type=\"{mime_type}\"; "
                    f"filessize=\"{file_stat.st_size}\""
                    f"Failed to upload: {resp}")

    # TODO compute thumbnail, upload thumbnail to Server
    # TODO add thumbnail info to `content`

    content = {
        "body": os.path.basename(image),  # descriptive title
        "info": {
            "size": file_stat.st_size,
            "mimetype": mime_type,
            "thumbnail_info": None,  # TODO
            "w": width,  # width in pixel
            "h": height,  # height in pixel
            "thumbnail_url": None,  # TODO
            # "thumbnail_file": None,
        },
        "msgtype": "m.image",
        "url": resp.content_uri,
        # "file": {
        #    # image/jpeg
        #    "mimetype": mime_type,
        #    # e.g. "mxc://example.com/someStrangeUriKey",
        #    "url": resp.content_uri,
        #    "v": "v2"
    }

    try:
        for room_id in rooms:
            await client.room_send(
                room_id,
                message_type="m.room.message",
                content=content
            )
            logger.debug(f"This image file was sent: \"{image}\" "
                         f"to room \"{room_id}\".")
    except Exception:
        logger.debug(f"Image send of file {image} failed. "
                     "Sorry. Here is the traceback.")
        logger.debug(traceback.format_exc())


async def send_message(client, rooms, message):
    """Process message.

    Format messages according to instructions from command line arguments.
    Then send all messages to all rooms.

    Arguments:
    ---------
    client : Client
    rooms : list
        list of room_id-s
    message : str
        message to send as read from -m, pipe or keyboard
        message is without mime formatting

    """
    if not rooms:
        logger.info("No rooms are given. This should not happen. "
                    "This text message is being droppend and NOT sent.")
        return
    # remove leading AND trailing newlines to beautify
    message = message.strip("\n")

    if message == "" or message.strip() == "":
        logger.debug(
            "The message is empty. "
            "This message is being droppend and NOT sent.")
        return

    if pargs.notice:
        content = {"msgtype": "m.notice"}
    else:
        content = {"msgtype": "m.text"}

    if pargs.code:
        logger.debug("Sending message in format \"code\".")
        formatted_message = "<pre><code>" + message + "</code></pre>"
        content["format"] = "org.matrix.custom.html"  # add to dict
        content["formatted_body"] = formatted_message
    elif pargs.markdown:
        logger.debug("Converting message from MarkDown into HTML. "
                     "Sending message in format \"markdown\".")
        # e.g. converts from "-abc" to "<ul><li>abc</li></ul>"
        formatted_message = markdown(message)
        content["format"] = "org.matrix.custom.html"  # add to dict
        content["formatted_body"] = formatted_message
    elif pargs.html:
        logger.debug("Sending message in format \"html\".")
        formatted_message = message  # the same for the time being
        content["format"] = "org.matrix.custom.html"  # add to dict
        content["formatted_body"] = formatted_message
    else:
        logger.debug("Sending message in format \"text\".")
    content["body"] = message

    try:
        for room_id in rooms:
            await client.room_send(
                room_id,
                message_type="m.room.message",
                content=content
            )
            logger.debug(f"This message was sent: \"{message}\" "
                         f"to room \"{room_id}\".")
    except Exception:
        logger.debug("Image send failed. Sorry. Here is the traceback.")
        logger.debug(traceback.format_exc())


def get_messages_from_pipe() -> list:
    """Read input from pipe if available.

    Return [] if no input available on pipe stdin.
    Return ["some-msg"] if input is availble.
    Might also return [""] of course if "" was in pipe.
    Currently there is at most 1 msg in the returned list.
    """
    messages = []
    stdin_ready = select.select([sys.stdin, ], [], [], 0.0)[0]
    if not stdin_ready:
        logger.debug("stdin is not ready. "
                     "A pipe could be used, but pipe could be empty, "
                     "stdin could also be a keyboard.")
    else:
        logger.debug("stdin is ready. Something "
                     "is definitely piped into program from stdin."
                     "Reading message from stdin pipe.")
    if ((not stdin_ready) and (not sys.stdin.isatty())) or stdin_ready:
        if not sys.stdin.isatty():
            logger.debug("Pipe was definitely used, but pipe might be empty. "
                         "Trying to read from pipe in any case.")
        message = ""
        try:
            for line in sys.stdin:
                message += line
            logger.debug("Using data from stdin pipe as message.")
            messages.append(message)
        except EOFError:  # EOF when reading a line
            logger.debug("Reading from stdin resulted in EOF. This can happen "
                         "when a pipe was used, but the pipe is empty. "
                         "No message will be generated.")
    return messages


def get_messages_from_keyboard() -> list:
    """Read input from keyboard but only if no other messages are available.

    If there is a message provided via --message argument, no message
    will be read from keyboard.
    If there is a message provided via stdin input pipe, no message
    will be read from keyboard.
    In short, we only read from keyboard as last resort, if no messages are
    specified or provided anywhere.

    Return [] if no input available on keyboard.
    Return ["some-msg"] if input is availble on keyboard.
    Might also return [""] of course if "" keyboard entry was empty.
    Currently there is at most 1 msg in the returned list.
    """
    messages = []
    if pargs.message:
        logger.debug("Don't read from keyboard because there are "
                     "messages provided in arguments with -m.")
        return messages  # return empty list because mesgs in -m
    stdin_ready = select.select([sys.stdin, ], [], [], 0.0)[0]
    if not stdin_ready:
        logger.debug("stdin is not ready. "
                     "A pipe could be used, but pipe could be empty, "
                     "stdin could also be a keyboard.")
    else:
        logger.debug("stdin is ready. Something "
                     "is definitely piped into program from stdin."
                     "Reading message from stdin pipe.")
    if ((not stdin_ready) and (sys.stdin.isatty())):
        # because sys.stdin.isatty() is true
        logger.debug("No pipe was used, so read input from keyboard."
                     "Reading message from keyboard")
        try:
            message = input("Enter message to send: ")
            logger.debug("Using data from stdin keyboard as message.")
            messages.append(message)
        except EOFError:  # EOF when reading a line
            logger.debug("Reading from stdin resulted in EOF. "
                         "Reading from keyboard failed. "
                         "No message will be generated.")
    return messages


async def send_messages_and_files(client, rooms, messages):
    """Send text messages and files.

    First images, audio, etc, then text messaged.

    Arguments:
    ---------
    client : Client
    rooms : list of room_ids
    messages : list of messages to send

    """
    if pargs.image:
        for image in pargs.image:
            await send_image(client, rooms, image)

    if pargs.audio:
        for audio in pargs.audio:
            # audio file can be sent like other files
            await send_file(client, rooms, audio)

    if pargs.file:
        for file in pargs.file:
            await send_file(client, rooms, file)

    for message in messages:
        await send_message(client, rooms, message)


async def process_arguments_and_input(client, rooms):
    """Process arguments and all input.

    Process all input: text messages, etc.
    Prepare a list of messages from all sources and then send them.

    Arguments:
    ---------
    client : Client
    rooms : list of room_ids

    """
    messages_from_pipe = get_messages_from_pipe()
    messages_from_keyboard = get_messages_from_keyboard()
    if not pargs.message:
        messages_from_commandline = []
    else:
        messages_from_commandline = pargs.message

    logger.debug(f"Messages from pipe:         {messages_from_pipe}")
    logger.debug(f"Messages from keyboard:     {messages_from_keyboard}")
    logger.debug(f"Messages from command-line: {messages_from_commandline}")

    messages_all = messages_from_commandline + \
        messages_from_pipe + messages_from_keyboard  # keyboard at end

    # loop thru all msgs and split them
    if pargs.split:
        # pargs.split can have escape characters, it has to be de-escaped
        decoded_string = bytes(pargs.split, "utf-8").decode("unicode_escape")
        logger.debug(f"String used for splitting is: \"{decoded_string}\"")
        messages_all_split = []
        for m in messages_all:
            messages_all_split += m.split(decoded_string)
    else:  # not pargs.split
        messages_all_split = messages_all

    await send_messages_and_files(client, rooms, messages_all_split)


async def main() -> None:
    """Create credentials, or use credentials to log in and send messages."""
    credentials_file = determine_credentials_file()
    store_file = determine_store_file()  # noqa # TODO
    # TODO: how to handle store_file from here on

    if not os.path.isfile(credentials_file):
        logger.debug("Credentials file does not exist.")
        await create_credentials_file(credentials_file)
    else:
        logger.debug("Credentials file does exist.")
        credentials = read_credentials_from_disk(credentials_file)
        client = AsyncClient(credentials['homeserver'])
        client.access_token = credentials['access_token']
        client.user_id = credentials['user_id']
        client.device_id = credentials['device_id']
        room_id = credentials['room_id']
        logger.debug("Logged in using stored credentials from "
                     f"credentials file \"{credentials_file}\".")

        # Now we can send messages as the user
        rooms = determine_rooms(room_id)
        logger.debug(f"Rooms are: {rooms}")
        await process_arguments_and_input(client, rooms)
        await client.close()


if __name__ == "__main__":  # noqa # ignore mccabe if-too-complex
    logging.basicConfig()  # initialize root logger, a must
    # set log level on root
    if "DEBUG" in os.environ:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    # Construct the argument parser
    ap = argparse.ArgumentParser(
        description="On first run this program will configure itself. "
        "On further runs this program implements a simple Matrix sender. "
        "It sends one or multiple text message to a Matrix room. "
        "The messages can be of format \"text\", \"html\", \"markdown\" "
        "or \"code\"."
        "matrix-nio must be installed.")
    # Add the arguments to the parser
    ap.add_argument("-d", "--debug", required=False,
                    action="store_true", help="Print debug information")
    # -c is already used for --code, -t as abbreviation for "trust"
    ap.add_argument("-t", "--credentials", required=False, type=str,
                    default=CREDENTIALS_FILE_DEFAULT,
                    help="On first run, information about homeserver, "
                    "user, room id, etc. will be written to a credentials "
                    "file. By default, this file "
                    f"is \"{CREDENTIALS_FILE_DEFAULT}\". "
                    "On further runs the credentials file is read to "
                    "permit logging into the correct Matrix account "
                    "and sending messages to the preconfigured room. "
                    "If this option is provided, the provided file name "
                    "will be used as credentials file instead of the "
                    "default one. ")
    ap.add_argument("-r", "--room", required=False,
                    action="extend", nargs="+", type=str,
                    help="Send to this room or these rooms. None, one or "
                    "multiple rooms can be specified. "
                    "The default room is provided "
                    "in credentials file. If a room (or multiple ones) "
                    "is (or are) provided in the arguments, then it "
                    "(or they) will be used "
                    "instead of the one from the credentials file. "
                    "The user must have access to the specified room "
                    "in order to send messages there. Messages cannot "
                    "be sent to arbitrary rooms. When specifying the "
                    "room id some shells require the exclamation mark "
                    "to be escaped with a blackslash.")
    # allow multiple messages , e.g. -m "m1" "m2" or -m "m1" -m "m2"
    # message is going to be a list of strings
    # e.g. message=[ 'm1', 'm2' ]
    ap.add_argument("-m", "--message", required=False,
                    action="extend", nargs="+", type=str,
                    help="Send this message. If not specified, and no "
                    "input piped in from stdin, then message "
                    "will be read from stdin, i.e. keyboard."
                    "This option can be used multiple time to send "
                    "multiple messages. If there is data is piped "
                    "into this program, then first data from the "
                    "pipe is published, then messages from this "
                    "option are published.")
    # allow multiple messages , e.g. -i "i1.jpg" "i2.gif"
    # or -m "i1.png" -i "i2.jpeg"
    # image is going to be a list of strings
    # e.g. image=[ 'i1.jpg', 'i2.png' ]
    ap.add_argument("-i", "--image", required=False,
                    action="extend", nargs="+", type=str,
                    help="Send this image."
                    "This option can be used multiple time to send "
                    "multiple images. First images are send, "
                    "then text messages are send.")
    # allow multiple audio files , e.g. -i "a1.mp3" "a2.wav"
    # or -m "a1.mp3" -i "a2.m4a"
    # audio is going to be a list of strings
    # e.g. audio=[ 'a1.mp3', 'a2.m4a' ]
    ap.add_argument("-a", "--audio", required=False,
                    action="extend", nargs="+", type=str,
                    help="Send this audio file."
                    "This option can be used multiple time to send "
                    "multiple audio files. First audios are send, "
                    "then text messages are send.")
    # allow multiple files , e.g. -i "a1.pdf" "a2.doc"
    # or -m "a1.pdf" -i "a2.doc"
    # file is going to be a list of strings
    # e.g. file=[ 'a1.pdf', 'a2.doc' ]
    ap.add_argument("-f", "--file", required=False,
                    action="extend", nargs="+", type=str,
                    help="Send this file (e.g. PDF, DOC)."
                    "This option can be used multiple time to send "
                    "multiple files. First files are send, "
                    "then text messages are send.")
    # -h already used for --help, -w for "web"
    ap.add_argument("-w", "--html", required=False,
                    action="store_true", help="Send message as format "
                    "\"HTML\". If not specified, message will be sent "
                    "as format \"TEXT\". E.g. that allows some text "
                    "to be bold, etc. Only a subset of HTML tags are "
                    "accepted by Matrix.")
    # -m already used for --message, -z because there were no letters left
    ap.add_argument("-z", "--markdown", required=False,
                    action="store_true", help="Send message as format "
                    "\"MARKDOWN\". If not specified, message will be sent "
                    "as format \"TEXT\". E.g. that allows sending of text "
                    "formated in MarkDown language.")
    ap.add_argument("-c", "--code", required=False,
                    action="store_true", help="Send message as format "
                    "\"CODE\". If not specified, message will be sent "
                    "as format \"TEXT\". If both --html and --code are "
                    "specified then --code takes priority. This is "
                    "useful for sending ASCII-art or tabbed output "
                    "like tables as a fixed-sized font will be used "
                    "for display.")
    # -s is already used for --store, -i for sPlit
    ap.add_argument("-p", "--split", required=False, type=str,
                    help="If set, split the message(s) into multiple messages "
                    "wherever the string specified with --split occurs."
                    "E.g. One pipes a stream of RSS articles into the "
                    "program and the articles are separated by three "
                    "newlines. "
                    "Then with --split set to \"\\n\\n\\n\" each article "
                    "will be printed in a separate message."
                    "By default, i.e. if not set, no messages will be split.")
    # -c is already used for --code, -k as it sounds like c
    ap.add_argument("-k", "--config", required=False, type=str,
                    help="Location of a config file. By default, no "
                    "config file is used. "
                    "If this option is provided, the provided file name "
                    "will be used to read configuration from. ")
    ap.add_argument("-n", "--notice", required=False,
                    action="store_true", help="Send message as notice. "
                    "If not specified, message will be sent as text.")
    ap.add_argument("-e", "--encrypted", required=False,
                    action="store_true", help="Send message end-to-end"
                    "encrypted. "
                    "If not specified, message will be sent unencrypted.")
    # -n already used for --markdown, -e for "nOtice"
    ap.add_argument("-s", "--store", required=False, type=str,
                    default=STORE_DIR_DEFAULT,
                    help="Path to directory to be "
                    "used as \"store\" for encrypted messaging."
                    "Must be specified if -e is used. "
                    "By default, this directory "
                    f"is \"{STORE_DIR_DEFAULT}\". "
                    "It is not needed for unencrypted messaging."
                    "If this option is provided, the provided directory name "
                    "will be used as persistent storage directory instead of "
                    "the default one.")

    pargs = ap.parse_args()
    if pargs.debug:
        # set log level on root logger
        logging.getLogger().setLevel(logging.DEBUG)
        logging.getLogger().info("Debug is turned on.")
    logger = logging.getLogger(PROG_WITHOUT_EXT)

    if pargs.encrypted:
        logger.info("This feature is not implemented yet. "
                    "Please help me implement it. If you feel motivated "
                    "please write code and submit a Pull Request. "
                    "Your contribution is appreciated. Thnx!")
        sys.exit(1)
    if pargs.config:
        logger.info("This feature is not implemented yet. "
                    "Please help me implement it. If you feel motivated "
                    "please write code and submit a Pull Request. "
                    "Your contribution is appreciated. Thnx!")
        sys.exit(1)

    if pargs.encrypted and ((not pargs.store) or (pargs.store == "")):
        logger.error("If --encrypt is used --store must be set too. "
                     "Specify --store and run program again.")
        sys.exit(1)

    if not pargs.encrypted:
        pargs.store = None

    try:
        asyncio.get_event_loop().run_until_complete(main())
    except Exception:
        logger.info(f"The program {PROG_WITH_EXT} failed. "
                    "Sorry. Here is the traceback.")
        logger.info(traceback.format_exc())
        # traceback.print_exc(file=sys.stdout)
        sys.exit(1)
    except KeyboardInterrupt:
        logger.debug("Keyboard interrupt received.")
        sys.exit(1)

# EOF
