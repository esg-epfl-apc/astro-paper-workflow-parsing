Subject:
Re: Viewing Cashed Graph
From:
"Volodymyr Savchenko [EPFL]" <Volodymyr.Savchenko@epfl.ch>
Date:
26.06.23, 18:30
To:
Stian Soiland-Reyes <soiland-reyes@manchester.ac.uk>, Meznah Aloqalaa <meznah.aloqalaa@postgrad.manchester.ac.uk>
CC:
Carole Goble <carole.goble@manchester.ac.uk>, Neronov Andrii <andrii.neronov@epfl.ch>

Hi Meznah, Stian,

thanks for your replies and looking into it!
I am on a conference until Wednesday but I try to reply as possible.

I will put the answers from all emails here, but I almost feel like this would better fit in some document where we could put issues and so. I'd use github or overleaf?

> These effectively S-expressions are powerful,

Yes, that was the idea, in form to avoid pile of brackets at the end.

> but of course need some kind of schema/documentation to be understood elsewhere. Here the arguments depends on the named function, which are defined elsewhere, presumably within the code?

Tool name + version defines (presumably) globally unique name of a pure function. But of course this can not be guaranteed since version is set by the developer, so along with such a graph there is a always a list of references to modules with definitions (in practices most of them are references to github repositories, with revisions). I can send you this.
Module is like this https://github.com/volodymyrss/dda-ddosa/blob/master/ddosa.py#L3220 . Modules contain only domain-specific code (and only this code) which is convoluted and subject to lot's of experiments and changes, so please don't judge code quality.

> Or are we able to get some of the names for those arguments as well? Presumably a different version of a tool might occasionally expect a different number of arguments? 

Different version might have different number, but for most purposes different version is a different function.

Here are the formal parameters for the root function in this graph:

https://github.com/volodymyrss/dda-ddosa/blob/2078cf0cd18309e3e18457e22e744467b70b556d/ddosa.py#L3221C5-L3225

> Do each tool/function just have one output?

Only one output in this case, but it's structured. So if it is needed to extract part of it, there is just another function takes structured output as input and produces something smaller and more limited.
When mapping is done, output can be a list, I will send an example.

There is a complexity here that I did not want that ScWData would depend on the function producing list of ScWData in the same way as e.g. ibis_isgr_energy.v6.1_extras depends on ScWData.
So they are represent in a different same way, this format seems less convenient for this different kind of relation.
 
> The format helps though, I was able even to load it in ClojureScript by just changing ‘ to “ and None to nil, while Python loads it directly as-is.  

Yes, it makes analysis easier. Also the way it's formatted, making diff between files with similar graphs like that is useful (though I do not do that often anymore).

> I see it’s recursing with the same types in the nesting. This “list” indicates a dependency that happens after the function, or subtasks that happen before, or something to be iterated over when calling the function?

It's list of parameters values, in some cases it was convenient. In fact, it does not have very deep meaning. Iteration is done with mapping function, see below.

> If we were expressing this in PROV or Turtle, then the nesting may be unrolled using identifiers (to avoid blank nodes), but as it is there are no timestamps or job identifiers, right?  Nor any indication if a step was cached, right? Could that be logged from elsewhere?

After the ii_lc_extract (this DAG is it's provenance) product is complete every node which can be cached is cached. Each cached node from the graph you see has it's own graph stored along with it, a subgraph of this graph.
What can be cached is decided by each cache, there is a hierarchy of them (in-memory cache, cache on local some node scratch, cluster fs cache, distributed fs cache).
The DAG expression itself here is not representing details of storage. Side-effect like stored data are addressed by caches or compute level.

> I still think the graph is interesting to keep as-is, it could be post-processed to for instance look for the version of the tools used. Are the complete one still the same overall structure? Any indication of the iteration? Feel free to share a big one!
MA> I completely agree with Stian about sharing the big one!

It's the same structure except it uses mapping functions, i.e. functions which take as an argument a list and another function and return a list. For storing this is split in two DAGs: one representing function which is being mapped. Function is also represented DAG but "factorized" by some parameters. E.g. this graph I sent you can be transformed to a graph representing function by replacing (2499..., ScWData.v1) to a formal parameter.

I could send you the entire 100s of Mbs of these data but there will be lot's of repetitions. I will send some of that, but I will also show how this mapping is represented.

> But can a pattern or schema be shown to identify the relations between the entity and the attributes? For example, the attached picture from your paper shows one science window.

> Can we say that the file that you sent reflects one Science window?  ScWData.v1

There are 3 terminal nodes:

1. ("249900160010.001", "ScWData.v1")  (it's two nodes but here as it makes sense to see them as a singular node representing a small sub-graph)

2. "ICRoot...."

3. SourceCatalog...

All of them all raw data with unique IDs within this namespace, or equivalently nullary functions.

> Can we have a graph from it, as one attached?

Sure, see at the end.


Here’s what I managed to get when converting the DAG to PROV:

https://openprovenance.org/store/documents/6604

 

 

You can convert to Turtle etc there, I loaded from the PROV-JSON output.

 

 

> It’s a quick hack which I would fail my students on, as I treat the blue activity as the same as the output from that activity – but due to the caching they are essentially the same thing in this case (and the DAG does not record any of the hashes).  To make it more correct PROV I would add an entity for each result as well as split out the script as a Plan.
> Generated with https://gist.github.com/stain/83dc40820a54ccfd99745b38a006bb70 -- I use the same caching assumption as you, so the UUIDv5 identifiers are based solely on sha1-hashing the name of the script and the arguments they are given.

Very nice thanks! I was making PROV out of it on different occasions in the last 5 years or so, but it did not end up too relevant at the time, so I do not know if I have a working code at the moment.

I will look into your example and adapt as needed.

> I am not sure if the intermediate lists are needed in here, the above could be simplified by doing “used” directly to each item,

Yes, pretty much.

> but then you don’t know the argument order.
python tuple is ordered so the order is fixed as long as tool definition can be converted from it.



MA> I attached this Word document. We would like to have a complete use case.
MA> If you could provide us with the workflow parameters that are related to this science window
MA> As it is usually described on the MMODA page!
MA> Also, could you identify elements of the Science Window in the table?

I will do it, yes.

file:///home/savchenk/graph.png

On 26.06.23 13:08, Stian Soiland-Reyes wrote:
>
> Thanks!
>
>  
>
> These effectively S-expressions are powerful, but of course need some kind of schema/documentation to be understood elsewhere. Here the arguments depends on the named function, which are defined elsewhere, presumably within the code? Or are we able to get some of the names for those arguments as well? Presumably a different version of a tool might occasionally expect a different number of arguments?  Do each tool/function just have one output?
>
>  
>
>  
>
> The format helps though, I was able even to load it in ClojureScript by just changing ‘ to “ and None to nil, while Python loads it directly as-is.  
>
>  
>
>  
>
> I see it’s recursing with the same types in the nesting. This “list” indicates a dependency that happens after the function, or subtasks that happen before, or something to be iterated over when calling the function?
>
>  
>
> If we were expressing this in PROV or Turtle, then the nesting may be unrolled using identifiers (to avoid blank nodes), but as it is there are no timestamps or job identifiers, right?  Nor any indication if a step was cached, right? Could that be logged from elsewhere?
>
>  
>
> I still think the graph is interesting to keep as-is, it could be post-processed to for instance look for the version of the tools used. Are the complete one still the same overall structure? Any indication of the iteration? Feel free to share a big one!
>
>  
>
> -- 
> Stian Soiland-Reyes, The University of Manchester
>
> https://www.esciencelab.org.uk/
> https://orcid.org/0000-0001-9842-9718
> Please note that I may work flexibly – whilst it suits me to email now, I do not expect a response or action outside of your own working hours.
>
> From: Savchenko Volodymyr <volodymyr.savchenko@epfl.ch>
> Sent: Monday, June 26, 2023 9:47 AM
> To: Meznah Aloqalaa <meznah.aloqalaa@postgrad.manchester.ac.uk>
> Cc: Carole Goble <carole.goble@manchester.ac.uk>; Stian Soiland-Reyes <soiland-reyes@manchester.ac.uk>; Neronov Andrii <andrii.neronov@epfl.ch>
> Subject: Re: Viewing Cashed Graph
>
>  
>
> Hi Mezanh,
>
> I am not sure if you want the entire structure, it's quite big, even when using sub-graphs. Let me know though how much do you want.
>
> For now, I attach a graph for a single small product, as an example.
>
> This is a custom format resembling function expressions like so:
>
> ("analysis" arg1, arg2,...,  function)
>
> or
>
> ("list" arg1, arg2,...)
>
> where "argX" can be another expression.
>
> This was done almost 15 years ago, if you can recommend another format for readable expression of this, let me know, I can convert. I could convert, for example, to turtle, but it's less readable it seems.
>
> Best Wishes
>
> Volodymyr
>
>  
>
>  
>
> On 23.06.23 21:44, Meznah Aloqalaa wrote:
>
>     Hi
>
>      
>
>     I hope you are doing fine.
>
>      
>
>     I intend to analyse the Directed Acyclic Graph(ACG).
>
>      
>
>     For that, how could we view this graph? Would you be able to share it with us?
>
>      
>
>     I could understand it is cashed, so it changed occasionally.
>
>      
>
>     Can we view multiple versions of it?
>
>      
>
>      
>
>     Thanks
>
>     Mezanh
>
>  
> -- 
> https://volodymyrsavchenko.com/ [volodymyrsavchenko.com]


-- 
https://volodymyrsavchenko.com/

