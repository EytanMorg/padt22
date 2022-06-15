FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y openssh-server unzip nano
RUN mkdir /var/run/sshd
RUN echo 'root:SuperSterkWachtwoord' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

EXPOSE 22

RUN adduser --disabled-password --gecos "flagUser," flaguser
RUN echo 'flaguser:XbrP4@oO2u3$kcS' | chpasswd

RUN apt-get update && apt-get install -y python3  python3-pip
RUN pip3 install stegano

COPY story/ /story/
COPY userHome/ /home/flaguser/
COPY motd.txt /etc/motd

RUN chmod -R 700 /story/backend/
RUN chown -R flaguser:flaguser /home/flaguser/
RUN chmod -R 705 /story/frontend/
RUN chmod -x /etc/update-motd.d/*

RUN rm /etc/legal
RUN systemctl disable motd-news.timer

RUN ln -s /story/frontend/frontend.py /usr/local/bin/Janet
RUN ln -s /story/frontend/frontend.py /usr/local/bin/janet

RUN echo 'Janet' >> /home/flaguser/.profile
RUN echo 'PrintlastLog no' >> /etc/ssh/sshd_config

CMD /usr/sbin/sshd && python3 /story/backend/backend.py
