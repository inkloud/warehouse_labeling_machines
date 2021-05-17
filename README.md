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
2. launch ```.\python-3.9.4-embed-amd64\get-pip.py```
3. Check the ```launch_server.ps1``` file and the correct port set 
4. Copy the complete path of ```launch_server.ps1``` as the params of the last command
5. create a link of ```launcher.cmd``` and put it in the folder ```C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup```. This guarantee that the printer is launching at the pc reboot
