# BZCTL

 - This tool can be downloaded with ``` pip install bzctl ```
 
 - It adds dirs named ``` ~/bzctl ``` and ``` ~/bzctl/config ```
 
 - Simply check ``` bzctl -h ```
 
 - # Uses

 - bzctl token --prefix {prefix} --save_token {token}

 - bzctl host --save_host {host}
 
 - bzctl run --image imagename --version imageversion --argument --argument ..
 
 - bzctl delete --image imagename
 
 - bzctl delete-all
 
 - # Example
 
 - ``` bzctl token --prefix Bearer --save_token eyJhbGciOi..... ```

 - ``` bzctl host --save_host http://127.0.0.1:8080/ ```

 - ``` bzctl run --image geth2 --version v0.0.1 --http --http.corsdomain https://remix.ethereum.org --http.api personal,eth,net,web3```
 
 - ``` bzctl delete --image geth2 ```
 
 - ``` bzctl delete-all ```
