setup Hyper-v Enable
Win+R 
code: optionalfeatures

multipass get local.driver
multipass delete <instance-name>
multipass purge

muitipass setup :
```sh
Get-Service multipass
Start-Service multipass
multipass list
multipass networks
multipass set local.bridged-network="Wi-Fi"
multipass launch --name bridge-test --bridged
```