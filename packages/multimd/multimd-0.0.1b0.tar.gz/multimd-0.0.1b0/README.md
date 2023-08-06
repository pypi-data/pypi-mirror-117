The `Python` module `multimd`
=============================


> **I beg your pardon for my english...**
>
> English is not my native language, so be nice if you notice misunderstandings, misspellings, or grammatical errors in my documents and codes.


About `multimd`
---------------

Working with `MD` documents of moderate size in a single file can becomes quickly painful. This project makes it possible to write separated pieces of `MD` files that will be merged to produce one single  `MD` file.


`README.md` part by part
------------------------

Thanks to `multimd`, you can write a `MD` document typing small section like parts that are easy to maintain. Let's consider the `README.md` of the `src2prod` project that was written using the following tree structure on August 22, 2021. Just note that there are only `MD` files directly inside the same folder (the purpose of `multimd` is to ease the writting of realtively small documents and not books). 

~~~
+ src2prod
    + readme
        * about.peuf
        * build.md
        * cli.md
        * example-used.md
        * only-files.md
        * prologue.md
        * readme-splitted.md
    
    * README.md
~~~

The special file `about.peuf` allows to indicate the order to use to merge the different `MD` files. Its content was the following one.

~~~
toc::
    + prologue
    + example-used
    + build
    + only-files
    + readme-splitted
    + cli
~~~

Here how `README.md` was built. We will suppose the use of the `cd` command to go inside the parent folder of `scr2prod` before launching the following script where we use instances of `Path` from `pathlib`.

~~~python
from multimd import Builder

mybuilder = Builder(
    output  = Path('README.md'),
    content = Path('readme'),
)

mybuilder.build()
~~~


Without the special `about.peuf` file
-------------------------------------

If you don't use the `about.peuf` file, the class `Builder` looks for all the `MD` files and then merges. The ordred used is the one givent by `natsorted` from the package `natsort`.