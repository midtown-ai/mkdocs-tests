# PDF hook


## hook

 {% pdf "https://arxiv.org/pdf/2411.14251v1" %}

### HTML Object

<object data="https://arxiv.org/pdf/2411.14251v1" type="application/pdf" width="100%" height="600px">
    <p>Your browser does not support PDFs. Please download the PDF: 
       <a href="path/to/your/file.pdf">Download PDF</a>.
    </p>
</object>

```
<object data="https://arxiv.org/pdf/2411.14251v1" type="application/pdf" width="100%" height="600px">
    <p>Your browser does not support PDFs. Please download the PDF: 
       <a href="path/to/your/file.pdf">Download PDF</a>.
    </p>
</object>
```

## PDFs plugins

/// warning | Warning
mkdocs-pdf creates an embed tag which is deprecated and replace with 'object' or 'iframe'
///

/// warning | Warning

Github does not support PDF with URL that are redirected. Use the final URL!
///

```
![Alt text](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210101201653/PDF.pdf){ type=application/pdf }
```

Redirect (Not supported on github!)

![Alt text](https://arxiv.org/pdf/2411.14251v1.pdf){ type=application/pdf }

Without redirect

![Alt text](https://arxiv.org/pdf/2411.14251v1){ type=application/pdf }

![Alt text](https://arxiv.org/pdf/2411.14251v1){ type=application/pdf style="min-height:100vh;width:100%" }


