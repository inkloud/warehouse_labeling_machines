### API
``` POST/PUT localhost:5001/label_writer_450/printPDF ```
Print PDF Base64 encoded.

Body:
```
{
    label: [{
        stream: ...
    },
    {
        stream: ...
    }],
    orderId: ...,
    startingBox: ...
}
```

- label: labes's json array. Inside every json item must be a field called ```stream``` that is the Base64 ancoded stream. 
- orderID: the order id. This field is mandatory to.
- startingBox: represents which package of the shipment you start printing from. Let's take an example which is easier. Suppose there is a 5-package shipment. The first two are printed. In this case ```staringBox``` is set to 0. To print the other three the data must be set to two. It might sound strange but trust me! Using startingBox correctly it will be possible to take advantage of the possibility of reprinting

``` POST/PUT localhost:5001/label_writer_450/reprintPDF ```

Reprint all the selected order labels.

Body:
```
{
    orderId: ...,
}
```
### Launch
To launch the server execute ```launch_server.ps1```

### Deployment 

1. Download the repo
2. double click on installer.cmd and say yes on open admin console
3. restart the pc and see the service active using https://localhost:5001/label_writer_450/


### Printer configuration

1. After installation of Zebra printer with default driver, manually add a printer with driver Generic-Text Only in the same port of Zebra Printer
2. Change paper format to:
    Width: 6inch
    Height: 4inch
3. In Printer Properties in Windows set:
    Orientation: Orizontal


##### Useful for deployment
chrome.exe --user-data-dir="C:/Chrome dev session" --disable-web-security
Set-ExecutionPolicy unrestricted

#### NB 
New script for deployment with https protocol. 
