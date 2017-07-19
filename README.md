<h1>static-dfa</h1>
<h2>A proof by implementation that static webpages can parse a Type-3 regular grammar<h2>
<h3>https://alibresco.github.io/static-dfa</h3>

<p>A fully function dfa engine using nothing but static webpages</p>
<p>Specify your dfa in a `.dfa` file in the root directory (see examples),
and then send web queries with each token of your input seperated by `/`</p>
<p></p>
<p>For example, to determine whether or not the binary number `1001` is divisible by two
send a query to https://alibresco.github.io/static-dfa/div2/1/0/0/1 and it will return
`success` or `failure` accordingly.</p>

<h2>FAQ</h2>
<h3>Can static webpages parse context free grammars? Are they Turing Complete?</h3>
<p>Almost certainly not. It seems like there's not way to store anything 
equivalent to a stack (or two in the case of TMs) as you traverse the symlinks,
but I'm always open to new ideas.</p>
<h3>Should I make a static webpage in production to parse regular expressions?</h3>
<p>What else would you use?</p>