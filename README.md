# workflow-parser

## Purpose of this repository

This is a tool which parses an astrophysical paper with references to MMODA and creates RO-Crate objects, linked to this paper.

## Outline of the problem

workflows expire, and need to be regularly re-computed

here we want to:

* find workflow refrences
* recompute them
* if needed and if possible, update to recomputed ones
* add labels of computability and when, if computable

currently, we add a further complication: instead of just outputing a paper with a validated workflow references, we output a "live" paper with latex templating implemented [here](https://github.com/oda-hub/linked-data-latex), making it possible to recompute the paper at will.

## Dealing with remote data

Much of the "raw" data used in astronomy can not be stored in the RO-Crate directly. Instead, it is preserved and maintained by astronomical Archives, like those at ESA, ESO, etc. In principle, these archives have different kinds and degrees of "qualification" for long-term storage. 

RO-Crate would need to keep track of the references to external data with different sort of "preservation assurance".

Since for large archives, computing should happen next to the data, workflow re-execution capacity also restricted. While in principle, the data is public and can be moved, it can be only practically moved to specific large well-connected data centers, supporting particular HTP/HPC computing technologies.
For the purposes of RO-Crate, it means that remote workflow execution on qualified compute providers (typically associated with Astronomical Archives) should also be supported.

## Example, use case

validating and rewriting ODA paper:

![image](https://user-images.githubusercontent.com/3909535/212079394-bdcf86b6-9f15-4f8d-bf85-c634702f8cc3.png)

## Note on building RO-Crate from MMODA workflows

We aim to first of all rely on the request parameters to identify the product.

"Data Curation" stage is a bit opaque to RO-Crate. We could export the graph with the product for explanatory purposes, but also possibly to externalize some analysis of this graph, in particular the kind which facilitates re-use some of the sub-products.

TODO: could we please have the slides Meznah showed?
