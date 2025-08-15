# Course notes for Metagenomics Bioinformatics at MGnify (2025) course

## Authoring
To edit the materials, you can just add/edit Markdown files (using normal markdown or [Quarto flavoured Markdown](https://quarto.org/docs/authoring/markdown-basics.html)) in the `sessions/` directory.

To preview your changes, you need to [install Quarto](https://quarto.org/docs/get-started/).

And run `quarto preview .` in this directory.

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

### Callout blocks
Quarto supports [callout blocks](https://quarto.org/docs/authoring/callouts.html) to make certain text stand out.
There are defaults like "tip", "note", "warning".
We also have custom callouts for "step" and "question". 
They can be used like this:

````markdown
# A section
This is some ordinary text.
::: {.callout-tip}
This is a tip
:::

::: {.callout-tip}
# Hint!
This is a tip with a custom title
:::

::: {.callout-step .callout-tip}
# Run MultiQC
This is a special "step" callout detailing what the participant should do next,
e.g.
```bash
run --some --code
```
:::

And finally
::: {.callout-question .callout-tip}
This is a question the participant should think about?
:::

````
