# Subspace Module

This involves a runthrough of the main function of subspace. We recommend going through the code if you want to understand the full extent of this module as there are alot of functions

## Register a Module
To register a module, you can use the following command

```
c model.openai register tag=sup api_key=sk-...
```

or

```
c register model.openai tag=sup api_key=sk-...
```

Please make sure you specify a unique tag, as it will not go through if someone else has that name on the subnet. When you deploy the module, the module will be serving locally on your machine and will be accessed by the network.


## Update a Module

To update a module, you can use the following command. At the moment you can update the module's name and address. Please not if you update the name, you will need to restart the server with the new name. This is currently something we want to avoid in the future by having to rename the server without killing it 

```

c update_module model.openai name=model.openai::fam1 address=124.545.545:8080
```



## Check Stats

To check the stats of a module, you can use the following command

```
c stats
```

If you want to sync the stats with the network, you can use the following.

```
c stats update=True
```



## Transfer Tokens

To tranfer tokens to a module, you can use the following command

```
c transfer model.openai 100 model.openai.2
```
or you an specify the address, this is the safer way to do it, as you can accidentally send it to the wrong address if the name has changed on the network.

```
c transfer ADDRESS_FROM model.openai 100 ADDRESS_TO
```

## Stake Tokens

To stake on a module, you can use the following command

```
c stake model.openai amount=100
```

To unstake on a module, you can use the following command

```
c unstake model.openai amount=100
```

### Staking on another Module with your Tokens

To stake on another module with your tokens, you can use the following command. 

```

c stake key=model.openai amount=100 module_key=model.openai.2
```

### Unstaking on another Module with your Tokens

To unstake on another module with your tokens, you can use the following command

```
c unstake key=model.openai amount=100 module_key=model.openai.2
```

## Start Local Node

To start a local node, you can use the following command

```
c start_node alice chain=main
```
This starts a node with the name alice on the main chain. You can also specify the chain to be main or dev.














