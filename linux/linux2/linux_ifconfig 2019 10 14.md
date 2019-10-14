# ifconfig
```
docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:b7:76:71:93  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::a00:27ff:fe32:3451  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:32:34:51  txqueuelen 1000  (Ethernet)
        RX packets 36  bytes 12433 (12.1 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 61  bytes 5713 (5.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 20  bytes 1116 (1.0 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 20  bytes 1116 (1.0 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```


#ping 172.17.0.1

```
linux實戰作業
root@kali:~# pwd
/root
root@kali:~# cd ..
root@kali:/# pwd
/
```

```
測驗:說明底下程式的意義
root@kali:/bin# cd ..
root@kali:/# cd
root@kali:~# 
```


