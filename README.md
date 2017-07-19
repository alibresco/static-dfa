# static-dfa
## A proof by implementation that static webpages can parse a Type-3 regular grammar

A fully function dfa engine using nothing but static webpages
Specify your dfa in a .dfa file in the root directory (see examples),
and then send web queries with each token of your input seperated by `/`

For example, to determine whether or not the binary number `1001` is divisible by two
send a query to `alibresco.github.io/static-dfa/div2/1/0/0/1` and it will return
`success` or `failure` accordingly.