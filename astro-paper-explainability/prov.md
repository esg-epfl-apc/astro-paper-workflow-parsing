Here’s what I managed to get when converting the DAG to PROV:

https://openprovenance.org/store/documents/6604

 

 

You can convert to Turtle etc there, I loaded from the PROV-JSON output.

 

 

It’s a quick hack which I would fail my students on, as I treat the blue activity as the same as the output from that activity – but due to the caching they are essentially the same thing in this case (and the DAG does not record any of the hashes).  To make it more correct PROV I would add an entity for each result as well as split out the script as a Plan.

 

Generated with https://gist.github.com/stain/83dc40820a54ccfd99745b38a006bb70 -- I use the same caching assumption as you, so the UUIDv5 identifiers are based solely on sha1-hashing the name of the script and the arguments they are given.

 

I am not sure if the intermediate lists are needed in here, the above could be simplified by doing “used” directly to each item, but then you don’t know the argument order.

 