# Widgets

## Buttons

[Subscribe to our newsletter](#){ .md-button .md-button--primary }

[Subscribe to our newsletter](#){ .md-button }

[Send :fontawesome-solid-paper-plane:](#){ .md-button }

## Grid of cards (md_in_html)

### grid-3 (HTML only)

<div class="grid grid-3" markdown="1">
  <div class="card no-border">
    <h3 class="card__title">Card 1</h3>
    <p>This is the first card's content.</p>
  </div>
  <div class="card no-border">
    <h3 class="card__title">Card 2</h3>
    <p>This is the second card's content.</p>
  </div>
  <div class="card no-border">
    <h3 class="card__title">Card 3</h3>
    <p>This is the third card's content.</p>
  </div>
</div>

<div class="grid grid-3" markdown="1">
  <div class="card">
    <h3 class="card__title">Card 1</h3>
    <p>This is the first card's content.</p>
  </div>
  <div class="card">
    <h3 class="card__title">Card 2</h3>
    <p>This is the second card's content.</p>
  </div>
  <div class="card">
    <h3 class="card__title">Card 3</h3>
    <p>This is the third card's content.</p>
  </div>
</div>


<div class="grid grid-3">
    <div>
    Column 1
    </div>
    <div>
    Column 2
    </div>
    <div>
    Column 3
    </div>
</div>

```
<div class="grid grid-3">
    <div>
    Column 1
    </div>
    <div>
    Column 2
    </div>
    <div>
    Column 3
    </div>
</div>
```

### generic grids

<div class="grid" markdown>

=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

``` title="Content tabs"
=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

</div>

### card grids

/// warning | Warning

First div must not be indented

///

<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>

```
<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>
```

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on GitHub

    [:octicons-arrow-right-24: License](#)

</div>

```
<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License](#)

</div>
```

<div class="grid" markdown>

:fontawesome-brands-html5: __HTML__ for content and structure
{ .card }

:fontawesome-brands-js: __JavaScript__ for interactivity
{ .card }

:fontawesome-brands-css3: __CSS__ for text running out of boxes
{ .card }

> :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>

```
<div class="grid" markdown>

:fontawesome-brands-html5: __HTML__ for content and structure
{ .card }

:fontawesome-brands-js: __JavaScript__ for interactivity
{ .card }

:fontawesome-brands-css3: __CSS__ for text running out of boxes
{ .card }

> :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>
```

## Content Tabs

### simple

=== "Tab A"
    In a different tab set.

=== "Tab B"
    More content.

```
=== "Tab A"
    In a different tab set.

=== "Tab B"
    More content.

```

### Linked tabs

=== "First"

    This is the content of my first tab!

=== "Second"

    Content of second tab

===! "First"

    Tab-names must match

    New tab set is started with `===!`

=== "Second"

    Tab-names is same as other tab above


## admonition

### blocks.adminition

/// note | note: ...
///

/// attention | attention ~ note ...
///

/// caution | caution ~ note ...
///

/// danger | danger ...
///

/// error | error ~ note ...
///

/// hint | hint ~ note ...
///

/// tip | tip ...
///

/// warning |
Warning with no Warning title!
///


/// warning | warning ...
Warning with Warning title!
///

```
# markdown

/// warning | warning ...
Warning with Warning title!
///

# to HTML

<div class="admonition warning">
<p class="admonition-title">warning ...</p>
<p>Warning with Warning title!</p>
</div>
```


/// warning | warning ...

Beware the markdown is insert and interpreted before being turned in HTML. So you must use triple ticks to see the content, unless not markdown!
```
--8<-- "abbreviations.md"
```
///

```
<div class="admonition warning">
<p class="admonition-title">warning ...</p>
<p>Beware the markdown is insert and interpreted before being turned in HTML. So you must use triple ticks to see the content, unless not markdown!
</p><div class="language-text highlight"><pre><span></span><code><span id="__span-4-1"><a id="__codelineno-4-1" name="__codelineno-4-1" href="#__codelineno-4-1"></a>*[Toc]: Table of Contents
</span><span id="__span-4-2"><a id="__codelineno-4-2" name="__codelineno-4-2" href="#__codelineno-4-2"></a>*[TOC]: Table Of Contents
</span><span id="__span-4-3"><a id="__codelineno-4-3" name="__codelineno-4-3" href="#__codelineno-4-3"></a>*[GFM]: GitHub Flavored Markdown
</span><span id="__span-4-4"><a id="__codelineno-4-4" name="__codelineno-4-4" href="#__codelineno-4-4"></a>*[FAQ]: Frequent Asked Questions
</span></code></pre></div>
</div>
```

#### Tentative


/// example | e
///

### blocks.details

/// details | note ...
///

/// details | danger ...
    type: danger
///

/// details | tip ...
    type: tip
///
/// details | question ...
    type: question
///

```
/// details | question ...
    type: question
///

# HTML rendering

<details class="question">
<summary>question ...</summary>
</details>
```

/// details | warning ...
    type: warning
    open: True

Rendering of pymdownx.blocks.details is function of type, which is a CSS class!
///

```
/// details | warning ...
    type: warning
    open: True

Rendering of pymdownx.blocks.details is function of type, which is a CSS class!
///

# HTML rendering

<details class="warning" open="open">
<summary>warning ...</summary>
<p>Rendering of pymdownx.blocks.details is function of type, which is a CSS class!</p>
</details>
```

/// details | tip ...
    type: tip
    open: True

Beware the markdown is insert and interpreted before being turned in HTML. So you must use triple ticks to see the content, unless not markdown!
```
--8<-- "abbreviations.md"
```
///

#### Tentative

/// details | examplee
Hello!
///


### Custom admonition (old style) + CSS

#### Tentative

!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

***

!!! mycustom "Custom Admonition :material-alert:"

    This is an example of a custom admonition styled with a unique look.

***

!!! pied-piper "Pied Piper"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et
    euismod nulla. Curabitur feugiat, tortor non consequat finibus, justo
    purus auctor massa, nec semper lorem quam in massa.

***


