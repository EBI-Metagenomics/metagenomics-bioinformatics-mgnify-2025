# Course notes for Metagenomics Bioinformatics at MGnify (2023) course

## Authoring
To edit the materials, you can just add/edit Markdown files (using normal markdown or [Quarto flavoured Markdown](https://quarto.org/docs/authoring/markdown-basics.html)) in the `sessions/` directory.

To preview your changes, you need to [install Quarto](https://quarto.org/docs/get-started/).

### Converting older materials
If you're converting materials from RST format in earlier year's courses, you might find the following prompt helpful for your LLM of choice:

````
Convert the following .rst file into Quarto Markdown (.qmd).
When there is a block starting `|image2|`, turn it into a callout using `:::{.callout-step .callout-tip}`.
When there is a block starting `|image3|`, turn it into a callout using `:::{.callout-question .callout-tip}`.
For other images, put a line in saying `TODO: image`.

```
******************
My old page in rst
******************
lorem ipsum
```
````
