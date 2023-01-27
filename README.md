# workflow-parser

workflows expire, and need to be regularly re-computed

here we want to:

* find workflow refrences
* recompute them
* if needed and if possible, update to recomputed ones
* add labels of computability and when, if computable

currently, we add a further complication: instead of just outputing a paper with a validated workflow references, we output a "live" paper with latex templating implemented [here](https://github.com/oda-hub/linked-data-latex), making it possible to recompute the paper at will.


# Example, use case

validating and rewriting ODA paper:

![image](https://user-images.githubusercontent.com/3909535/212079394-bdcf86b6-9f15-4f8d-bf85-c634702f8cc3.png)
