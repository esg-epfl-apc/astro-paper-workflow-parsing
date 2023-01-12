# workflow-parser

workflows expire, and need to be regularly re-computed

here we:
* find workflow refrences
* recompute them
* if needed and if possible, update to recomputed ones
* add labels of computability and when, if computable

# Example, use case

validating and rewriting ODA paper:

![image](https://user-images.githubusercontent.com/3909535/212079394-bdcf86b6-9f15-4f8d-bf85-c634702f8cc3.png)


```turtle
<https://odahub.io/ontology/org#contributesTo>
  <https://odahub.io/ontology/projects#ESG-T2.4>, 
  <https://odahub.io/ontology/projects#SmartSky-WP3>, 
  <https://odahub.io/ontology/projects#AstroORDASExplore-WPX>, 
  <https://odahub.io/ontology/projects#AstroORDASEstablish-WPX> 
```
