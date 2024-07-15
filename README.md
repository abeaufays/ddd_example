In this repo, we try to implement in python several example from the DDD book from Eric Evans.

# Layer example

The first example is found in the chapter 4: Isolating the domain, that talks about layers.


![Sequence Diagram representing transfer of fund between two accounts](https://github.com/abeaufays/ddd_example/blob/main/ddd_example/bank_transfer_layers/schema_layers.jpg?raw=true)

It involves layering, repositories and unit of work. 

We are using Django as the infrastructure implementation.

# General example

The second example comes from Chapter 7: Using the Language: An Extended Example.

It describes a system that will handle cargo shipping, the general model looks like this: 

![Class diagram of the cargo shipping domain](https://github.com/abeaufays/ddd_example/blob/main/ddd_example/cargo_shipping_system/class_diagram.png?raw=true)


# Comments
## About injecting Unit of work into domain functions
On one hand, it make sense to consider "making a persisting change to the model" as a domain concept, but on another hand "polluting" the domain layer with a `UnitOfWork` parameter feels clunky ?

We could also see it as marking a function as "mutable for the domain" where others would by default not have any side effect.

Maybe something can be done with a decorator to inject the `UnitOfWork` in a more "pythonic" way ? 