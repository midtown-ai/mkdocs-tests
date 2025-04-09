# Basics

## Icons, Smileys and highlights/marks

fontawesome (53,663 icons) - https://fontawesome.com/search

 * : fontawesome - class - name :   <!> to find the class look at the  HTML
 * `<i class="fa-brands fa-html5">` turns into `:fontawesome-brands-html5:` which renders as :fontawesome-brands-html5: 


materialdesign (7447 icons) - https://pictogrammers.com/library/mdi/

 * https://pictogrammers.com/library/mdi/icon/clock-fast/
 * turns into `:material-clock-fast:` rendered :material-clock-fast:

octicons - https://primer.style/foundations/icons

 * https://primer.style/foundations/icons/arrow-right-24
 * turns into  `:octicons-arrow-right-24:` or :octicons-arrow-right:

simpleicons - https://simpleicons.org/

***

:smile: and :heart: those ==emojis are awesome,== isn't it?

***

text below rule



## Links & Tooltips & Abbreviations & footnotes

### links

 * open pdf - https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210101201653/PDF.pdf
 * open web - page https://www.google.com

 [:octicons-arrow-right-24: Google](https://www.google.com "Go to Google")


Work:

 * https://www.ggogle.com
 * [markdown link to code-block](./blocks.md#code-block)
 * [in-page Reference-Style external Links][markdown syntax]
 * [in-page Reference-Style internal Links][glossary link]
 * [markdown syntax]
 * [glossary link] and [GloSSAry Link]

```
 * [snippets admonition][ablation]
 * direct snippets [ablation] and [accuracy]
```

[markdown syntax]: https://daringfireball.net/projects/markdown/syntax#link "title"
[glossary link]: /blocks.md#code-block "title"

```
Deprecated by snippets

 * [include-markdown links toto]
 * [include-markdown links_a titi] = include of include!
{% include '../includes/links.md' %}
```

Fail:

```
 * [#big] just to anchor (fails)
 * [in-page Reference-Style no match][no match]
```

### tooltips

:material-information-outline:{ title="Important information" }

[Hover me using inline syntax](https://example.com "I'm a tooltip!")

```
[Hover me using external reference link][example]
```

[Hover me using internal reference link][example2]

  [example2]: https://example.com "I'm a tooltip!"

### abbreviations

 Do these abbreviations work: CSS, W3C, and not HTML ? What about FAQ, Faq, TOC, Toc, and GFM?
 Yes if you hover the acronym !

/// danger| beware
abbreviations are case sensitive
///

In-page abbreviations
*[CSS]: Custom Style Sheet
*[W3C]:  World Wide Web Consortium

Disabled reference abbreviations
*[HTML]: 'H'

### footnotes

Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]

[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.

[^2]:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


SOME TEXT BEFORE THE BOTTOM OF THE PAGE

