In this repo, we try to implement the diagram found below that comes from the DDD book from Eric Evans.
![Sequence Diagram representing transfer of fund between two accounts](https://github.com/abeaufays/ddd_example/blob/main/ddd_example/bank_transfer_layers/schema_layers.jpg?raw=true)

We are using Django as the ORM.

## Comments
### About injecting Unit of work into domain functions
On one hand, it make sense to consider "making a persisting change to the model" as a domain concept, but on another hand "polluting" the domain layer with a `UnitOfWork` parameter feels clunky ?

We could also see it as marking a function as "mutable for the domain" where others would by default not have any side effect.

Maybe something can be done with a decorator to inject the `UnitOfWork` in a more "pythonic" way ? 