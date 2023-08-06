% BOTD(1) BOTD version 56
% Bart Thate 
% Aug 2021

# NAME
BOTD - 24/7 channel daemon

# DESCRIPTION

BOTD is a pure python3 IRC chat bot that can run as a background daemon for
24/7 a day presence in a IRC channel, it can be used to display RSS
feeds, act as a UDP to IRC relay and you can program your own commands for it.

BOTD an attempt to achieve OS level integration of bot technology directly
into the operating system. A solid, non hackable bot version, that can offer
"display in your irc channel" functionality to the unix programmer. BOTD
runs on both BSD and Linux, is placed in the Public Domain, and, one day,
will be the thing you cannot do without ;]

# SYNOPSIS

| botctl \<cmd>\ [options] [key=value] [key==value]
 
# CONFIGURATION
| botctl cfg server=localhost channel=\#bot nick=bot
| botctl m=irc,rss
| botctl pwd \<nick\> \<password\>
| botctl cfg password=\<outputofpwd\>
| botctl cfg users=true 
| botctl met \<userhost\>
| botctl rss \<url\>

