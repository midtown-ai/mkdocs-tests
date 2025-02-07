# CSS


## CSS selector

```
# HTML

<div class="container">
  <img src="image1.png" class="theme-image light-mode" alt="Matching Image">
</div>

# Matching CSS selector

.container img.theme-image.light-mode {
    /* Styles specific to images inside .container */
}
```

## Keyframe and icons

 :fontawesome-brands-twitter: :fontawesome-brands-twitter:{ .twitter-blue .font42px}

 :fontawesome-brands-youtube: :fontawesome-brands-youtube:{ .youtube-red .fading-in-and-out }
 <div class="fading-in-and-out">Fading text!</div>

 :fontawesome-solid-arrow-up: :fontawesome-solid-arrow-up:{ .bouncing-vertically }
 <div class="bouncing-vertically">Bouncing text!</div>

 :fontawesome-solid-arrow-right: :fontawesome-solid-arrow-right:{ .bouncing-horizontally } Text
 <div class="bouncing-horizontally">Bouncing text!</div>

 :fontawesome-brands-html5: :fontawesome-brands-html5:{ .flipping }
 <div class="flipping">Flipping text!</div>

 :fontawesome-solid-bell: :fontawesome-solid-bell:{ .shaking .red }
 :fontawesome-regular-bell: :fontawesome-regular-bell:{ .shaking .red }
 <div class="shaking">Shaking text!</div>

 :fontawesome-solid-arrows-spin: :fontawesome-solid-arrows-spin:{ .spinning-clockwise }
 :fontawesome-solid-spinner: :fontawesome-solid-spinner:{ .spinning-counter-clockwise }

 :fontawesome-solid-heart: :fontawesome-solid-heart:{ .heartbeating } :fontawesome-solid-heart:{ .heartbeating .red }

 :fontawesome-regular-heart: :fontawesome-regular-heart:{ .heartbeating } :fontawesome-regular-heart:{ .heartbeating .red }

 :fontawesome-regular-face-kiss-wink-heart: :fontawesome-regular-face-kiss-wink-heart:{ .heartbeating } :fontawesome-regular-face-kiss-wink-heart:{ .heartbeating .red }

 :octicons-heart-fill-24: :octicons-heart-fill-24:{ .heartbeating } :octicons-heart-fill-24:{ .heartbeating .red }
 <div class="heartbeating">Headbeating text!</div>


## Attribute list

/// warning |
```
# attr_list
{: #id1 .class1 id=id2 class="class2 class3" .class4 }
results in
id="id2" class="class2 class3 class4"
```
///

 More at: https://python-markdown.github.io/extensions/attr_list/

### markdown to attr

[Subscribe to our newsletter](#){ .md-button }

```
<p><a class="md-button" href="#">Subscribe to our newsletter</a></p>
```

[Subscribe to our newsletter](#){ .md-button .md-button--primary }

```
<p><a class="md-button md-button--primary" href="#">Subscribe to our newsletter</a></p>
```

**hello**{ .red }


```
<p><strong class="red">hello</strong></p>
```

| set on td    | set on em   |
|--------------|-------------|
| *a* { .foo } | *b*{ .foo } |

```
<table>
<thead>
<tr>
<th>set on td</th>
<th>set on em</th>
</tr>
</thead>
<tbody>
<tr>
<td class="foo"><em>a</em></td>
<td><em class="foo">b</em></td>
</tr>
</tbody>
</table>
```

### Failed tentatives

**bold**{:1}
...
**bold**{:1}

{:1: .myclass lang=fr}

<strong>bonjour</strong>

<div>
<strong>hello</strong> { .red }
</div>

FOOTER
