# Dockerfile builds an image with a chatbot (Tino) for Tinode.

FROM python:slim

ARG VERSION=0.15
ENV VERSION=0.15.7

LABEL maintainer="Gene Sokolov <gene@tinode.co>"
LABEL name="TinodeChatbot"
LABEL version=0.15.7

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

RUN pip install --no-cache-dir -q tinode-grpc

# Get tarball with the chatbot code and data.
ADD https://github.com/tinode/chat/releases/download/v$VERSION/py-chatbot.tar.gz .
# Unpack chatbot, delete archive
RUN tar -xzf py-chatbot.tar.gz \
	&& rm py-chatbot.tar.gz

# Use command line parameter `-e LOGIN_AS=user:password` to login as someone other than Tino.

CMD python chatbot.py --login-basic=toni5705:toni5705 --login-cookie=/botdata/.tn-cookie --host=pingnget.com > /var/log/chatbot.log

# Plugin port
EXPOSE 40051
EXPOSE 5000
