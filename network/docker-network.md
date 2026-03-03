What is Network interface:
Network Interface = Wifi adapter, Eternet port,
in linux it is called eth0, wlan0, enp3s0    

lets see:
```sh
ip addr
```
What does docker do :
1. create a virtual cable (veth pair) on HOST
2. 
```sh
                ┌───────────────────────────┐
                │        Container A        │
                │                           │
                │   lo (127.0.0.1)          │
                │   eth0  172.17.0.2        │
                └─────────────┬─────────────┘
                              │
                              │  veth pair (virtual cable)
                              │
                ┌─────────────┴─────────────┐
                │         Host Machine      │
                │                           │
                │        docker0 bridge     │
                │        172.17.0.1         │
                └─────────────┬─────────────┘
                              │
                              │
                      ┌───────┴──────── ┐
                      │   Container B   │
                      │                 │
                      │  eth0 172.17.0.3│
                      └─────────────────┘

A eth0 → veth → docker0 → veth → B eth0
```